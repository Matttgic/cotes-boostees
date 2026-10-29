"""Règlement des boosts par les résultats réels des sites de scores (sans IA).

Chaîne : texte du pari -> jambes (analyse_pari.py, sinon `jambes` déjà calculées) -> résultat archivé ou lu
(scores/recherche.py) -> verdict jambe par jambe.

Prudence (le bilan ne doit jamais être faussé) :
- une jambe non vérifiable (donnée absente, joueur introuvable, égalité sur une ligne entière) donne None ;
- le boost n'est réglé que si TOUTES les jambes sont tranchées, ou si l'une est perdue (le pari est alors perdu) ;
- le résultat doit être confirmé par une seconde source (scores identiques), ou venir de l'API officielle NHL ;
- deux sources en désaccord, match abandonné ou non terminé : aucun règlement ;
- un « remboursé » n'est donné que pour un pari simple (joueur absent, match annulé depuis plus de 48 h).
`reglements_manuels.json` et les verdicts existants restent prioritaires : on ne règle que les boosts sans statut.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from .analyse_pari import AVEC_NUL, analyser
from .scores.noms import equipe_proche, joueur_proche
from .scores.recherche import Recherche, _dt
from .scores.sources import SPORTS
from .simulation import REGLES

DELAI_H = 3
ANNULE_H = 48
TENNIS = ("tennis", "tennis_table", "badminton")
URLS = {"sofascore": "https://www.sofascore.com/event/{id}", "espn": "https://www.espn.com/soccer/match/_/gameId/{id}",
        "nhl": "https://api-web.nhle.com/v1/gamecenter/{id}/boxscore"}


def _cote(nom: str | None, r: dict) -> int | None:
    proche = joueur_proche if r["sport"] in TENNIS else equipe_proche
    if not nom:
        return None
    a, b = proche(nom, r["equipe_1"]), proche(nom, r["equipe_2"])
    return 1 if a and not b else 2 if b and not a else None


def _score(r: dict, periode: str, type_: str) -> list | None:
    """Score de la période demandée (domicile, extérieur), ou None si la source ne le donne pas."""
    sport = r["sport"]
    reg = r.get("score_reglementaire")
    if periode == "temps_reglementaire":
        return reg
    if periode == "match":
        if type_ == "vainqueur":
            return r.get("score")
        return reg if sport in AVEC_NUL else r.get("score")
    p = r.get("periodes") or []
    if periode == "mi_temps_1":
        return r.get("mi_temps") if sport in AVEC_NUL else None
    if periode == "mi_temps_2":
        mt = r.get("mi_temps")
        return [reg[0] - mt[0], reg[1] - mt[1]] if sport in AVEC_NUL and mt and reg else None
    if periode.startswith("tiers_temps_") and sport == "hockey":
        i = int(periode[-1]) - 1
        return p[i] if len(p) > i else None
    if periode == "set_1":
        return p[0] if p else None
    return None


def _compare(valeur: float, sens: str, ligne: float) -> str | None:
    if valeur == ligne:
        return None
    return "gagné" if (valeur > ligne) == (sens == "plus") else "perdu"


def _trouver_joueur(nom: str, joueurs: dict | None) -> dict | None:
    for n, v in (joueurs or {}).items():
        if joueur_proche(nom, n):
            return v
    return None


def _buts(j: dict, r: dict) -> tuple[str | None, str]:
    nom, ligne = j["joueur"], j["ligne"]
    n = None
    if r.get("buteurs") is not None:
        n = 0
        for b in r["buteurs"]:
            if b["csc"] or not joueur_proche(nom, b["joueur"]):
                continue
            if r["sport"] == "football" and b["minute"] is not None and b["minute"] > 90:
                continue          # prolongations : hors pari « temps réglementaire »
            if j["periode"] == "mi_temps_1" and not (b["minute"] is not None and b["minute"] <= 45):
                if b["minute"] is None:
                    return None, "minute du but inconnue"
                continue
            if j["periode"] == "mi_temps_2" and not (b["minute"] is not None and b["minute"] > 45):
                if b["minute"] is None:
                    return None, "minute du but inconnue"
                continue
            n += 1
    elif j["periode"] == "match":
        p = _trouver_joueur(nom, r.get("joueurs"))
        if p and p["stats"].get("Goals") is not None:
            n = p["stats"]["Goals"]
    if n is None:
        return None, "buteurs indisponibles"
    if n > ligne:
        return "gagné", f"{nom} : {n} but(s)"
    p = _trouver_joueur(nom, r.get("joueurs"))
    if p is None:
        return None, f"{nom} : présence non vérifiable"
    return ("perdu" if p["a_joue"] else "remboursé"), f"{nom} : {n} but, {'a joué' if p['a_joue'] else 'absent'}"


def _stats(j: dict, r: dict) -> tuple[str | None, str]:
    noms = j.get("joueurs") or [j["joueur"]]
    total = 0
    for nom in noms:
        p = _trouver_joueur(nom, r.get("joueurs"))
        if p is None:
            return None, f"{nom} introuvable dans les stats"
        if not p["a_joue"]:
            return (("remboursé", f"{nom} n'a pas joué") if len(noms) == 1 else (None, f"{nom} n'a pas joué"))
        vals = [p["stats"].get(s) for s in j["stat"].split("+")]
        if None in vals:
            return None, f"{nom} : statistique absente"
        total += sum(vals)
    v = _compare(total, j["sens"], j["ligne"])
    return v, f"{' + '.join(noms)} : {total} {j['stat']}"


def evaluer_jambe(j: dict, r: dict) -> tuple[str | None, str]:
    t = j["type"]
    if t == "joueur":
        if j.get("stat") == "Goals" and not j.get("joueurs"):
            return _buts(j, r)
        return _stats(j, r)
    if t == "les_deux_marquent":
        s = _score(r, j.get("periode") or "match", t)
        return (None, "score absent") if not s else (("gagné" if min(s) >= 1 else "perdu"), f"score {s[0]}-{s[1]}")
    unite = j.get("unite")
    if t == "total":
        if unite == "sets" and r["sport"] in TENNIS:
            s = r.get("score")
            v = sum(s) if s else None
        elif unite == "jeux":
            v = sum(sum(p) for p in r["periodes"]) if r.get("periodes") else None
        else:
            s = _score(r, j.get("periode") or "match", t)
            v = sum(s) if s else None
        if v is None:
            return None, "total indisponible"
        return _compare(v, j["sens"], j["ligne"]), f"total {v} {unite}"
    s = _score(r, j.get("periode") or "match", t)
    if s is None:
        return None, f"score de la période {j.get('periode')} indisponible"
    if t in ("resultat", "vainqueur"):
        if j["equipe"] == "nul":
            return ("gagné" if s[0] == s[1] else "perdu"), f"score {s[0]}-{s[1]}"
        c = _cote(j["equipe"], r)
        if c is None:
            return None, f"équipe {j['equipe']} non identifiée"
        if t == "vainqueur" and s[0] == s[1]:
            return None, "égalité"
        return ("gagné" if s[c - 1] > s[2 - c] else "perdu"), f"score {s[0]}-{s[1]}"
    c = _cote(j.get("equipe"), r)
    if t == "total_exact":
        v = sum(r["score"]) if r.get("score") else None
        return (None, "score absent") if v is None else (("gagné" if v == j["ligne"] else "perdu"), f"{v} sets")
    if t in ("handicap", "total_equipe", "score_sets", "score_exact", "score_exact_liste", "double_chance") and c is None:
        return None, f"équipe {j.get('equipe')} non identifiée"
    if t == "double_chance":
        return ("gagné" if s[c - 1] >= s[2 - c] else "perdu"), f"score {s[0]}-{s[1]}"
    if t in ("score_exact", "score_exact_liste"):
        # score écrit dans l'ordre du titre du match (équipe citée en premier d'abord) ; l'équipe nommée doit gagner
        c1 = _cote(j.get("ref"), r)
        if c1 is None:
            return None, "ordre du score non identifié"
        for sc in j["score"].split("|"):
            a, b = map(int, sc.split("-"))
            if not ((a > b) if c == c1 else (b > a)):
                return None, "ordre du score ambigu"
        ref = f"{s[c1 - 1]}-{s[2 - c1]}"
        return ("gagné" if ref in j["score"].split("|") else "perdu"), f"score {ref}"
    if t == "handicap":
        v = s[c - 1] - s[2 - c] + j["ligne"]
        return (None, "ligne entière") if v == 0 else (("gagné" if v > 0 else "perdu"), f"écart {s[c-1]-s[2-c]}")
    if t == "total_equipe":
        return _compare(s[c - 1], j["sens"], j["ligne"]), f"{j['equipe']} : {s[c-1]}"
    if t == "score_sets":
        ref = f"{s[c - 1]}-{s[2 - c]}"
        return ("gagné" if ref == j["score"] else "perdu"), f"score {ref}"
    return None, f"type {t} non géré"


def verdict_boost(b: dict, r: dict, legs: list[dict], maintenant: datetime) -> dict | None:
    # Unibet rembourse un joueur non titulaire (même entré en jeu) : on ne sait pas qui est titulaire ici
    unibet = b.get("bookmaker") == "Unibet"
    """Verdict {statut, score, explication, sources} ou None si le boost ne peut pas être réglé."""
    if r["statut"] == "annule":
        d = _dt(b.get("debut"))
        if d and maintenant - d > timedelta(hours=ANNULE_H) and len(legs) == 1:
            return {"statut": "remboursé", "score": "", "explication": "match annulé ou reporté de plus de 48 h",
                    "sources": []}
        return None
    if r["statut"] != "termine" or r.get("conflit"):
        return None
    if not (r.get("confirme_par") or r["source"] == "nhl"):
        return None
    res = [evaluer_jambe(j, r) for j in legs]
    if unibet:
        res = [(None, "titularisation non vérifiable (Unibet)") if j["type"] == "joueur" and x[0] in ("perdu", "remboursé")
               else x for j, x in zip(legs, res)]
    statuts = [x[0] for x in res]
    texte = " ; ".join(x[1] for x in res)
    if "perdu" in statuts:
        statut = "perdu"
    elif None in statuts:
        return None
    elif all(s == "gagné" for s in statuts):
        statut = "gagné"
    elif len(legs) == 1:
        statut = "remboursé"
    else:
        return None
    s = r.get("score")
    score = f"{r['equipe_1']} {s[0]}-{s[1]} {r['equipe_2']}" if s else ""
    srcs = [r["source"]] + list(r.get("confirme_par") or [])
    return {"statut": statut, "score": score[:300], "explication": texte[:600],
            "sources": [URLS[r["source"]].format(id=r["id"])] if r["source"] in URLS else [],
            "sources_noms": srcs}


def jambes_du_boost(b: dict) -> list[dict] | None:
    # Uniquement nos règles : les jambes IA oublient parfois une partie du pari (« ou match nul », « ou »)
    return analyser(b.get("pari"), b.get("match"), b.get("sport")) or None


def a_regler(base: dict[str, dict], maintenant: datetime) -> list[dict]:
    out = []
    for b in base.values():
        r = b.get("reglement") or {}
        if r.get("statut") in REGLES or r.get("a_la_main") or b.get("long_terme"):
            continue
        d = _dt(b.get("debut"))
        if d and d < maintenant - timedelta(hours=DELAI_H) and SPORTS.get(b.get("sport")):
            out.append(b)
    out.sort(key=lambda b: b["debut"])
    return out


def regler(base: dict[str, dict], rech: Recherche, maintenant: datetime | None = None, max_boosts: int = 600) -> dict:
    """Passage de règlement par les scores. Renvoie un résumé ; modifie `base` et l'archive de `rech`."""
    t = maintenant or datetime.now(timezone.utc)
    resume = {"examines": 0, "regles": 0, "non_analysables": 0, "sans_resultat": 0, "non_tranches": 0}
    for b in a_regler(base, t)[:max_boosts]:
        resume["examines"] += 1
        legs = jambes_du_boost(b)
        if not legs:
            resume["non_analysables"] += 1
            continue
        besoin = any(j["type"] == "joueur" for j in legs)
        r = rech.chercher(b, details=besoin)
        if r is None:
            resume["sans_resultat"] += 1
            continue
        v = verdict_boost(b, r, legs, t)
        if v is None:
            resume["non_tranches"] += 1
            continue
        rg = b.setdefault("reglement", {})
        rg.update({"statut": v["statut"], "regle_le": t.isoformat(timespec="seconds"), "score": v["score"],
                   "explication": v["explication"], "sources": v["sources"], "modele": "scores",
                   "methode": "scores", "sources_noms": v.get("sources_noms", []),
                   "jambes_reglement": legs})
        resume["regles"] += 1
    return resume


def regler_depuis_dossier(base: dict[str, dict], dossier) -> dict:
    """Passage complet pour la collecte : archive `resultats.json` lue puis réécrite, proxy français si dispo."""
    import tempfile
    from pathlib import Path

    from . import stockage
    from .acces import Navigateur, SecretsManquants
    from .scores.recherche import Lecteur, archive_vide

    dossier = Path(dossier)
    archive = stockage.charger(dossier / "resultats.json") or archive_vide()
    with tempfile.TemporaryDirectory() as tmp:
        try:
            nav = Navigateur(Path(tmp))
        except SecretsManquants:
            nav = None
        lecteur = Lecteur(nav)
        resume = regler(base, Recherche(archive, lecteur))
        resume["requetes"] = lecteur.requetes
        resume["octets_proxy"] = nav.octets if nav else 0
        if lecteur.derniere_erreur:
            resume["erreurs_http"] = lecteur.derniere_erreur
    stockage.ecrire(dossier / "resultats.json", archive)
    return resume
