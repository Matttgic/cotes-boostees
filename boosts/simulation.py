"""Stratégies simulées, toujours à la mise max.

- A « Tout miser » : CHAQUE cote boostée ;
- B « Filtrée » : seulement les boosts dont la valeur initiale face à Pinnacle (boosts/valeur.py) est
  d'au moins `EV_MIN_B` %, en deux variantes : B-exacte (calcul exact) et B-approx (jambes liées,
  produit des probabilités).

Règles du pari simulé :
- un pari par boost (deux boosts sur le même match = deux paris) ;
- mise = mise max affichée par le bookmaker (10, 20, 50 €…) ;
- cote = cote boostée vue au premier passage (ce que le parieur aurait pris en jouant aussitôt) ;
- règlement : `boost["reglement"]["statut"]` (gagné / perdu / remboursé), sinon « en attente ».
Un boost sans mise max connue n'est pas joué (compté à part, pour le repérer).

PROTOCOLE GELÉ (11/10/2026) : quatre stratégies suivies, réglées AVANT de connaître leurs résultats :
- A  (témoin)   : tous les boosts, mise max ;
- B             : valeur ≥ +5 % face à la cote juste (calcul exact ou ligne interpolée), mise max ;
- B0            : valeur ≥ 0 %, même calcul, mise max (plus de volume) ;
- D (hypothèse) : cotes 1,60 à 3,50, 10 € max — filtre repéré EN REGARDANT les 85 premiers résultats,
                  donc à confirmer uniquement sur les paris postérieurs au gel.
Seuls les boosts vus pour la première fois APRÈS `DATE_GEL` servent à juger (bilan « après gel »).
Les autres stratégies restent calculées pour mémoire (archives), sans être retouchées.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")
REGLES = ("gagné", "perdu", "remboursé")
EV_MIN_B = 5.0
DATE_GEL = "2026-10-11T20:00:00+00:00"
VERSION_PROTOCOLE = "gel-1"
SUIVIES = {"A": "A — témoin : tous les boosts, mise max",
           "B_valeur": "B — valeur ≥ +5 % (exacte ou interpolée), mise max",
           "B0_valeur": "B0 — valeur ≥ 0 % (exacte ou interpolée), mise max",
           "D_moderee": "D — hypothèse : cotes 1,60 à 3,50, 10 € max"}
STATUTS_FIABLES = ("exacte", "interpolee")
TRANCHES_VALEUR = [(-1e9, 0.0, "EV < 0"), (0.0, 5.0, "EV 0 à 5 %"), (5.0, 10.0, "EV 5 à 10 %"),
                   (10.0, 1e9, "EV 10 % et +")]
TRANCHES = [(1.0, 2.0, "< 2"), (2.0, 3.0, "2 – 3"), (3.0, 5.0, "3 – 5"), (5.0, 10.0, "5 – 10"),
            (10.0, 1e9, "10 et +")]


def statut(boost: dict) -> str:
    s = (boost.get("reglement") or {}).get("statut")
    return s if s in REGLES else "en attente"


def pari(boost: dict) -> dict | None:
    mise = boost.get("mise_max")
    cote = boost.get("cote_boostee_initiale") or boost.get("cote_boostee")
    if not mise or not cote:
        return None
    s = statut(boost)
    gain = {"gagné": round(mise * (cote - 1), 2), "perdu": -float(mise), "remboursé": 0.0}.get(s)
    v = boost.get("valeur_initiale") or {}
    return {"id": boost["id"], "bookmaker": boost.get("bookmaker"), "sport": boost.get("sport") or "?",
            "valeur": v.get("statut") or "non_evaluable", "ev_pct": v.get("ev_pct"),
            "horizon": "long terme (saison)" if boost.get("long_terme") else "match",
            "cote_juste": v.get("cote_juste"),
            "match": boost.get("match"), "pari": boost.get("pari"), "debut": boost.get("debut"),
            "mise": float(mise), "cote": cote, "cote_origine": boost.get("cote_origine"),
            "statut": s, "gain": gain}


def _tranche_valeur(p: dict) -> str:
    if p["ev_pct"] is None:
        return "non évaluable"
    nom = next(n for lo, hi, n in TRANCHES_VALEUR if lo <= p["ev_pct"] < hi)
    return f"{nom} ({p['valeur']})"


def filtre_b(variante: str):
    return lambda p: p["valeur"] == variante and p["ev_pct"] is not None and p["ev_pct"] >= EV_MIN_B


def _tranche(cote: float) -> str:
    return next(n for lo, hi, n in TRANCHES if lo <= cote < hi)


def _mois(debut: str | None) -> str:
    if not debut:
        return "?"
    return datetime.fromisoformat(debut).astimezone(PARIS).strftime("%Y-%m")


def _agreger(paris: list[dict]) -> dict:
    regles = [p for p in paris if p["statut"] in REGLES]
    mise = sum(p["mise"] for p in regles)
    gain = round(sum(p["gain"] for p in regles), 2)
    gagnes = sum(p["statut"] == "gagné" for p in regles)
    perdus = sum(p["statut"] == "perdu" for p in regles)
    return {"paris": len(paris), "regles": len(regles), "en_attente": len(paris) - len(regles),
            "gagnes": gagnes, "perdus": perdus, "rembourses": len(regles) - gagnes - perdus,
            "mise_totale": mise, "gain_net": gain,
            "roi_pct": round(gain / mise * 100, 1) if mise else None,
            "reussite_pct": round(gagnes / (gagnes + perdus) * 100, 1) if gagnes + perdus else None,
            "cote_moyenne": round(sum(p["cote"] for p in paris) / len(paris), 2) if paris else None,
            # indicateur sans attendre les résultats : valeur moyenne (face à la cote juste) des paris joués
            # dont la valeur était calculable avant le match
            "ev_moyenne_pct": round(sum(evs) / len(evs), 1) if (evs := [p["ev_pct"] for p in paris
                                                                      if p.get("ev_pct") is not None]) else None,
            "paris_avec_ev": len(evs)}


def bilan(base: dict[str, dict], filtre=None, nom: str = "A — toutes les cotes boostées, mise max") -> dict:
    paris, sans_mise = [], 0
    for b in base.values():
        p = pari(b)
        if p is None:
            sans_mise += 1
        elif filtre is None or filtre(p):
            paris.append(p)
    paris.sort(key=lambda p: p["debut"] or "")

    groupes = {"par_bookmaker": defaultdict(list), "par_sport": defaultdict(list),
               "par_tranche_de_cote": defaultdict(list), "par_mise": defaultdict(list),
               "par_mois": defaultdict(list), "par_valeur": defaultdict(list),
               "par_horizon": defaultdict(list)}
    for p in paris:
        groupes["par_bookmaker"][p["bookmaker"]].append(p)
        groupes["par_sport"][p["sport"]].append(p)
        groupes["par_tranche_de_cote"][_tranche(p["cote"])].append(p)
        groupes["par_mise"][f"{p['mise']:g} €"].append(p)
        groupes["par_mois"][_mois(p["debut"])].append(p)
        groupes["par_valeur"][_tranche_valeur(p)].append(p)
        groupes["par_horizon"][p["horizon"]].append(p)

    # courbe des gains et pires moments, dans l'ordre des matchs
    cumul, sommet, pire_baisse, serie, pire_serie, courbe = 0.0, 0.0, 0.0, 0, 0, []
    for p in paris:
        if p["statut"] not in REGLES:
            continue
        cumul = round(cumul + p["gain"], 2)
        sommet = max(sommet, cumul)
        pire_baisse = min(pire_baisse, cumul - sommet)
        serie = serie + 1 if p["statut"] == "perdu" else 0 if p["statut"] == "gagné" else serie
        pire_serie = max(pire_serie, serie)
        courbe.append({"debut": p["debut"], "cumul": cumul})

    return {"strategie": nom,
            "global": {**_agreger(paris), "boosts_sans_mise_max": sans_mise,
                       "pire_baisse": round(pire_baisse, 2), "pire_serie_perdante": pire_serie},
            **{k: {g: _agreger(v) for g, v in sorted(d.items())} for k, d in groupes.items()},
            "courbe": courbe, "paris": paris}


def strategies(base: dict[str, dict]) -> dict:
    from .strategies_experimentales import construire

    originelles = {"A": bilan(base),
                   "B_exacte": bilan(base, filtre_b("exacte"), f"B-exacte — EV ≥ {EV_MIN_B:g} % (calcul exact), mise max"),
                   "B_approx": bilan(base, filtre_b("approx"), f"B-approx — EV ≥ {EV_MIN_B:g} % (jambes liées), mise max")}
    return {**originelles, **construire(base),
            "B_valeur": _valeur(base, EV_MIN_B, SUIVIES["B_valeur"]),
            "B0_valeur": _valeur(base, 0.0, SUIVIES["B0_valeur"])}


# --------------------------------------------------------------------------- protocole gelé

def _instant(v):
    try:
        d = datetime.fromisoformat(str(v).replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=ZoneInfo("UTC"))
    except (TypeError, ValueError):
        return None


def entree_valeur(b: dict, seuil: float) -> float | None:
    """Cote d'entrée d'un pari « valeur » : celle notée au PREMIER calcul fiable, avant le match, si la
    valeur atteint le seuil à ce moment-là. None sinon (jamais de calcul refait avec une cote plus récente)."""
    v = b.get("valeur_initiale") or {}
    if v.get("statut") not in STATUTS_FIABLES or v.get("ev_pct") is None or float(v["ev_pct"]) < seuil:
        return None
    cote, date, debut = v.get("cote_boostee"), _instant(v.get("date")), _instant(b.get("debut"))
    if not cote or float(cote) <= 1 or date is None or debut is None or date >= debut:
        return None
    return float(cote)


def _valeur(base: dict[str, dict], seuil: float, nom: str) -> dict:
    choisis = {}
    for k, b in base.items():
        cote = entree_valeur(b, seuil)
        if cote is not None:
            choisis[k] = {**b, "cote_boostee_initiale": cote}       # copie : boosts.json n'est pas modifié
    return bilan(choisis, nom=nom)


def apres_gel(base: dict[str, dict]) -> dict[str, dict]:
    gel = _instant(DATE_GEL)
    return {k: b for k, b in base.items() if (vu := _instant(b.get("premiere_vue"))) is not None and vu >= gel}


def protocole(base: dict[str, dict]) -> dict:
    from .strategies_experimentales import construire
    recents = apres_gel(base)
    d_recent = construire(recents)["D_moderee"]
    apres = {"A": bilan(recents, nom=SUIVIES["A"]),
             "B_valeur": _valeur(recents, EV_MIN_B, SUIVIES["B_valeur"]),
             "B0_valeur": _valeur(recents, 0.0, SUIVIES["B0_valeur"]),
             "D_moderee": {**d_recent, "strategie": SUIVIES["D_moderee"]}}
    leger = lambda x: {"strategie": x["strategie"], "global": x["global"], "courbe": x["courbe"],
                       "par_bookmaker": x["par_bookmaker"], "par_valeur": x["par_valeur"]}
    return {"version": VERSION_PROTOCOLE, "date_gel": DATE_GEL, "suivies": list(SUIVIES),
            "boosts_apres_gel": len(recents), "apres_gel": {k: leger(v) for k, v in apres.items()}}
