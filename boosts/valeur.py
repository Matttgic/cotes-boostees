"""Valeur d'un boost face aux références « sharp » : cote juste, EV, et fiabilité du calcul.

Pour chaque jambe (boosts/jambes.py) on cherche le MÊME pari (même match, même marché, même période,
même ligne, même côté) chez Pinnacle (probabilité juste = marge retirée, méthode power), puis, si
Pinnacle ne l'a pas, sur l'échange Betfair (via PulseScore : milieu achat/vente, seulement si l'écart
achat/vente est serré et l'argent engagé suffisant). Chaque jambe garde sa source.
- une seule jambe, ou des jambes sur des matchs différents (indépendantes) → calcul « exacte » ;
- plusieurs jambes sur le même match → produit des probabilités, calcul « approx » (le lien entre les
  conditions est ignoré : voir README) ;
- une jambe introuvable chez Pinnacle (ligne différente, marché absent, type « autre ») →
  « non évaluable », jamais d'à-peu-près.
EV = cote boostée × probabilité juste − 1.
"""
from __future__ import annotations

import re
from datetime import datetime, timedelta

from .correspondance import matchs_de, ressemblance

# sport Winamax (catégorie des cotes boostées) → sport commun de pinnacle.py
SPORTS = {"football": "football", "tennis": "tennis", "basketball": "basket", "basket": "basket",
          "hockey sur glace": "hockey", "football américain": "football_americain", "baseball": "baseball",
          "handball": "handball", "volley-ball": "volley", "volley": "volley", "rugby à xv": "rugby",
          "rugby": "rugby", "mma": "mma", "boxe": "boxe", "fléchettes": "flechettes", "esport": "esport",
          "cricket": "cricket", "tennis de table": "tennis_de_table", "snooker": "snooker"}
UNITES = {"buts": "", "sets": "SETS_", "jeux": "JEUX_", "corners": "CORNERS_"}
SCORE_MIN = 0.75


def sport_commun(sport_winamax: str | None) -> str | None:
    return SPORTS.get((sport_winamax or "").strip().lower())


def _t(s) -> datetime | None:
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


class Index:
    """Lignes Pinnacle regroupées par match, pour des recherches rapides."""

    def __init__(self, lignes: list[dict]):
        self.matchs = matchs_de(lignes)
        self.lignes: dict = {}
        for l in lignes:
            if l.get("proba_juste"):
                self.lignes.setdefault(l["match_id"], []).append(l)

    def trouver_match(self, sport: str, e1: str | None, e2: str | None, debut: datetime | None):
        """(match Pinnacle, inversé ?) le plus ressemblant, dans une fenêtre autour de l'heure du boost."""
        if not e1 or not e2:
            return None
        meilleur = None
        for m in self.matchs.values():
            if m["sport"] != sport or not m["debut"]:
                continue
            # boost sur plusieurs matchs : l'heure du boost est celle du premier
            if debut and not (debut - timedelta(hours=3) <= m["debut"] <= debut + timedelta(hours=30)):
                continue
            direct = min(ressemblance(e1, m["domicile"]), ressemblance(e2, m["exterieur"]))
            inverse = min(ressemblance(e1, m["exterieur"]), ressemblance(e2, m["domicile"]))
            score, inv = max((direct, False), (inverse, True))
            ecart = abs((m["debut"] - debut).total_seconds()) if debut else 0
            # A ressemblance identique, choisir le coup d’envoi le plus proche.
            if score >= SCORE_MIN and (meilleur is None or (score, -ecart) > (meilleur[2], -meilleur[3])):
                meilleur = (m, inv, score, ecart)
        return meilleur[:3] if meilleur else None


def _cote_equipe(match: dict, nom: str | None) -> str | None:
    if not nom:
        return None
    if nom.strip().lower() in ("nul", "match nul", "draw"):
        return "NUL"
    d, e = ressemblance(nom, match["domicile"]), ressemblance(nom, match["exterieur"])
    if max(d, e) < 0.6:
        return None
    return "DOM" if d >= e else "EXT"


def _periode(j: dict, sport: str) -> str:
    if j["periode"] == "mi_temps_1":
        return "MT1"
    if j["periode"] == "temps_reglementaire" and sport == "hockey":
        return "TEMPS_REG"
    return "MATCH"


def _mots(s: str | None) -> set[str]:
    return set(re.findall(r"[a-z]+", (s or "").lower()))


def cle_recherche(j: dict, match: dict, sport: str) -> tuple | str:
    """Critères de la ligne Pinnacle (marché, période, ligne, issue), ou la raison d'un échec."""
    periode = _periode(j, sport)
    t = j["type"]
    if t in ("resultat", "vainqueur"):
        cote = _cote_equipe(match, j["equipe"])
        if cote is None:
            return "équipe du pari introuvable dans le match"
        marche = "RESULTAT_1N2" if t == "resultat" else "VAINQUEUR"
        return (marche, periode, None, cote)
    if t == "handicap":
        cote = _cote_equipe(match, j["equipe"])
        if cote not in ("DOM", "EXT") or j["ligne"] is None:
            return "handicap incomplet"
        ligne_dom = j["ligne"] if cote == "DOM" else -j["ligne"]      # Pinnacle : handicap du domicile
        return (UNITES[j["unite"]] + "HANDICAP", periode, ligne_dom, cote)
    if t in ("total", "total_equipe"):
        if j["ligne"] is None or j["sens"] is None:
            return "total incomplet"
        issue = "PLUS" if j["sens"] == "plus" else "MOINS"
        if t == "total":
            return (UNITES[j["unite"]] + "TOTAL", periode, j["ligne"], issue)
        cote = _cote_equipe(match, j["equipe"])
        if cote not in ("DOM", "EXT"):
            return "équipe du total introuvable"
        return (UNITES[j["unite"]] + ("TOTAL_DOM" if cote == "DOM" else "TOTAL_EXT"), periode, j["ligne"], issue)
    if t == "les_deux_marquent":
        return ("BTTS", periode, None, "OUI")
    if t == "joueur":
        if not j["joueur"] or j["ligne"] is None:
            return "pari joueur incomplet"
        return ("JOUEUR", periode, j["ligne"], "PLUS" if (j["sens"] or "plus") == "plus" else "MOINS")
    return "type de pari non coté par Pinnacle"


def _egal(a, b) -> bool:
    return (a is None and b is None) or (a is not None and b is not None and abs(float(a) - float(b)) < 1e-6)


def chercher_ligne(index: Index, match: dict, cle: tuple, j: dict) -> dict | None:
    marche, periode, ligne, issue = cle
    if marche == "BTTS":                                   # Pinnacle (spécial) et Betfair (marché normal)
        for l in index.lignes.get(match["match_id"], []):
            if l["periode"] == periode and l["marche"] in ("SPECIAL:Both Teams To Score?", "BOTH_TEAMS_TO_SCORE") \
                    and l["issue"] in ("Yes", "YES"):
                return l
        return None
    for l in index.lignes.get(match["match_id"], []):
        if l["periode"] != periode or l["issue"] != issue or not _egal(l.get("ligne"), ligne):
            continue
        if marche == "BTTS":
            continue                                        # traité plus haut (issue « Yes » / « YES »)
        if marche == "JOUEUR":
            if not l["marche"].startswith("JOUEUR:") or ressemblance(j["joueur"], l.get("joueur")) < 0.8:
                continue
            stat = _mots(l["marche"][7:])
            if not stat or not (stat & _mots(j["stat"])):
                continue
            return l
        if l["marche"] == marche:
            return l
    return None


def _completer_equipe_depuis_titre(j: dict, titre: str | None) -> dict:
    """Complète une équipe manquante si l'autre correspond strictement au titre.

    Ne devine rien quand les deux équipes sont inconnues ou le titre ambigu.
    """
    if not titre or titre.count(" - ") != 1:
        return j
    domicile, exterieur = (nom.strip() for nom in titre.split(" - ", 1))
    if not re.search(r"[a-zA-ZÀ-ÿ]", domicile) or not re.search(r"[a-zA-ZÀ-ÿ]", exterieur):
        return j
    e1, e2 = j.get("equipe_1"), j.get("equipe_2")
    if bool(e1) == bool(e2):
        return j
    if e1 and ressemblance(e1, domicile) >= 0.9:
        return {**j, "equipe_2": exterieur}
    if e2 and ressemblance(e2, exterieur) >= 0.9:
        return {**j, "equipe_1": domicile}
    return j


def _jambe(j: dict, sport: str, debut, index: Index):
    """(ligne, match, ressemblance) ou la raison de l'échec."""
    trouve = index.trouver_match(sport, j["equipe_1"], j["equipe_2"], debut)
    if trouve is None:
        return f"match introuvable ({j['equipe_1']} - {j['equipe_2']})"
    match, _, score = trouve
    cle = cle_recherche(j, match, sport)
    if isinstance(cle, str):
        return cle
    l = chercher_ligne(index, match, cle, j)
    if l is None:
        return f"ligne absente ({cle[0]} {cle[1]} {cle[2]} {cle[3]})"
    return l, match, score


def evaluer(boost: dict, jambes: list[dict] | None, sources) -> dict:
    """{statut: exacte | approx | non_evaluable, cote_juste, ev_pct, raison, detail}.
    `sources` : [(nom, Index)…] dans l'ordre de préférence (un Index seul est accepté : « Pinnacle »)."""
    if isinstance(sources, Index):
        sources = [("Pinnacle", sources)]
    sport = sport_commun(boost.get("sport"))
    if not jambes:
        return {"statut": "non_evaluable", "raison": "pari non décomposé"}
    if sport is None:
        return {"statut": "non_evaluable", "raison": f"sport non suivi ({boost.get('sport')})"}
    debut = _t(boost.get("debut"))
    proba, matchs_vus, detail = 1.0, [], []
    for original in jambes:
        # Complément strict réservé à un pari simple sur une rencontre explicite.
        j = _completer_equipe_depuis_titre(original, boost.get("match")) if len(jambes) == 1 else original
        if j["type"] == "autre":
            return {"statut": "non_evaluable", "raison": "condition non cotée par les références", "detail": detail}
        raisons, res = [], None
        for nom, index in sources:
            r = _jambe(j, sport, debut, index)
            if isinstance(r, str):
                raisons.append(f"{nom} : {r}")
                continue
            res = (nom, *r)
            break
        if res is None:
            return {"statut": "non_evaluable", "raison": " ; ".join(raisons), "detail": detail}
        nom, l, match, score = res
        proba *= l["proba_juste"]
        matchs_vus.append(f"{nom}|{match['match_id']}")
        detail.append({"source": nom, "match": f"{match['domicile']} - {match['exterieur']}", "marche": l["marche"],
                       "periode": l["periode"], "ligne": l.get("ligne"), "issue": l["issue"],
                       "joueur": l.get("joueur"), "cote_reference": l["cote"], "cote_juste": l["cote_juste"],
                       "ressemblance": round(score, 2)})
    # même match (même source) pour deux jambes = conditions liées ; deux sources pour un même match
    # ne se reconnaissent pas ici, d'où la comparaison par nom de match en plus
    noms = [d["match"] for d in detail]
    lie = len(matchs_vus) != len(set(matchs_vus)) or len(noms) != len(set(noms)) or \
        len({(j["equipe_1"], j["equipe_2"]) for j in jambes}) < len(jambes)
    statut = "approx" if lie else "exacte"
    cote_juste = round(1 / proba, 3)
    ev = round((boost["cote_boostee"] * proba - 1) * 100, 1)
    ev_origine = round((boost["cote_origine"] * proba - 1) * 100, 1) if boost.get("cote_origine") else None
    return {"statut": statut, "cote_juste": cote_juste, "ev_pct": ev, "ev_origine_pct": ev_origine,
            "sources": sorted({d["source"] for d in detail}), "detail": detail}


# --------------------------------------------------------------------------- Betfair (échange)

ECART_ACHAT_VENTE_MAX = 0.05
ECART_RELATIF_MAX = 0.25
LIQUIDITE_MIN = 20.0


def reference_betfair(lignes: list[dict]) -> list[dict]:
    """Lignes Betfair traduites (boosts/pulsescore.py) → probabilité juste = milieu achat/vente,
    seulement pour les marchés complets, serrés et assez liquides (mêmes règles que cotes-value)."""
    groupes: dict[tuple, list[dict]] = {}
    for l in lignes:
        groupes.setdefault((l["cle_marche"], l["marche"], l["periode"], l.get("ligne")), []).append(l)
    out = []
    for g in groupes.values():
        probs, fiable = [], True
        for l in g:
            achat, vente = l.get("achat") or [], l.get("vente") or []
            if not achat or not vente:
                fiable = False
                break
            pb, pv = 1 / float(achat[0]["price"]), 1 / float(vente[0]["price"])
            liq = min(float(achat[0].get("liquidity") or 0), float(vente[0].get("liquidity") or 0))
            p = (pb + pv) / 2
            if pb - pv > ECART_ACHAT_VENTE_MAX or pb - pv > ECART_RELATIF_MAX * min(p, 1 - p) or liq < LIQUIDITE_MIN:
                fiable = False
                break
            probs.append(p)
        if not fiable or len(probs) < 2:
            continue
        s = max(sum(probs), 1.0)              # renormalisé seulement à la baisse (issues manquantes)
        for l, p in zip(g, probs):
            out.append({**l, "source": "Betfair", "proba_juste": round(p / s, 6), "cote_juste": round(s / p, 4)})
    return out
