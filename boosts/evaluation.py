"""Passage d'évaluation : décompose les nouveaux boosts (IA) et calcule leur valeur face à Pinnacle.

Tant que le match n'a pas commencé, chaque passage recalcule la valeur (`valeur_derniere`).
La première valeur calculable (`valeur_initiale`) est celle sur laquelle la stratégie B décide de jouer
ou non : c'est ce que le parieur aurait su en voyant le boost.
"""
from __future__ import annotations

from datetime import datetime, timezone

from . import jambes as jb
from . import pinnacle, valeur
from .reglement import client_ia, fournisseur

ESSAIS_DECOMPOSITION = 3
ID_PINNACLE = {nom: sid for sid, nom in pinnacle.SPORTS.items()}


def _a_venir(b: dict, t: datetime) -> bool:
    d = valeur._t(b.get("debut"))
    return d is not None and d > t


def evaluer_boosts(base: dict[str, dict], maintenant: str, collecter_pinnacle=pinnacle.collecter) -> dict:
    t = datetime.fromisoformat(maintenant) if maintenant else datetime.now(timezone.utc)
    resume = {"decomposes": 0, "echecs_decomposition": 0, "evalues": 0, "exactes": 0, "approx": 0,
              "non_evaluables": 0}
    a_venir = [b for b in base.values() if _a_venir(b, t)]
    if not a_venir:
        return resume

    # 1. décomposition des nouveaux boosts (une fois par boost)
    fourn = fournisseur()
    client = client_ia(fourn) if fourn else None
    for b in a_venir:
        if b.get("jambes") is not None or b.get("jambes_essais", 0) >= ESSAIS_DECOMPOSITION or client is None:
            continue
        b["jambes_essais"] = int(b.get("jambes_essais", 0)) + 1
        try:
            jambes, modele = jb.decomposer(b, client, fourn)
        except Exception as e:
            resume["echecs_decomposition"] += 1
            resume["derniere_erreur"] = f"{type(e).__name__} : {e}"[:300]
            continue
        if jambes is None:
            resume["echecs_decomposition"] += 1
            continue
        b["jambes"], b["jambes_modele"] = jambes, modele
        resume["decomposes"] += 1

    # 2. cotes Pinnacle des sports concernés, puis valeur de chaque boost
    a_evaluer = [b for b in a_venir if b.get("jambes")]
    sports = {valeur.sport_commun(b.get("sport")) for b in a_evaluer}
    ids = {ID_PINNACLE[s]: s for s in sports if s in ID_PINNACLE}
    if not ids:
        return resume
    try:
        index = valeur.Index(collecter_pinnacle(ids))
    except Exception as e:
        resume["erreur_pinnacle"] = f"{type(e).__name__} : {e}"[:300]
        return resume
    for b in a_evaluer:
        v = {**valeur.evaluer(b, b["jambes"], index), "date": maintenant, "cote_boostee": b["cote_boostee"]}
        b["valeur_derniere"] = v
        if v["statut"] != "non_evaluable" and not b.get("valeur_initiale"):
            b["valeur_initiale"] = v
        resume["evalues"] += 1
        resume[{"exacte": "exactes", "approx": "approx"}.get(v["statut"], "non_evaluables")] += 1
    return resume
