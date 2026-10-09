"""Stratégies expérimentales PRÉDÉFINIES : comparaison prospective, jamais optimisation sur gains passés.

Les seules informations autorisées à la sélection sont celles observées avant le match.
Pour les stratégies EV, la cote d'entrée est celle enregistrée lors du PREMIER calcul
de valeur (et non la cote initiale, parfois antérieure au calcul).
Les paris sont exclusivement fictifs ; aucun de ces filtres ne garantit un EV positif.
"""
from __future__ import annotations

import math
from datetime import datetime, timezone

from . import simulation

BANQUE_DE_REFERENCE = 1000.0  # simulation théorique fixe, PAS un solde réel


def _nombre(v) -> float | None:
    try:
        n = float(v)
        return n if math.isfinite(n) else None
    except (TypeError, ValueError):
        return None


def _instant(v) -> datetime | None:
    try:
        if not v:
            return None
        d = datetime.fromisoformat(str(v).replace("Z", "+00:00"))
        return d.replace(tzinfo=timezone.utc) if d.tzinfo is None else d.astimezone(timezone.utc)
    except (ValueError, TypeError):
        return None


def _mise(b: dict, plafond: float = 10) -> float | None:
    montant = _nombre(b.get("mise_max"))
    if montant is None or montant <= 0:
        return None
    return round(min(montant, plafond), 2)


def _cote(b: dict) -> float | None:
    x = _nombre(b.get("cote_boostee_initiale") or b.get("cote_boostee"))
    return x if x is not None and x > 1 else None


def _court_terme(b: dict) -> bool:
    """Match sous 48 h à la découverte : n'utilise jamais la date du dernier scan."""
    debut, vu = _instant(b.get("debut")), _instant(b.get("premiere_vue"))
    return bool(not b.get("long_terme") and debut and vu and 0 <= (debut - vu).total_seconds() <= 48 * 3600)


def _valeur_initiale(b: dict, seuil: float, cote_max: float) -> tuple[float, float] | None:
    """(cote réellement notée à la 1re évaluation, proba dévigée).

    Écarte un calcul tardif, incomplet, non exact ou une cote inaccessible au 1er calcul.
    L'EV initiale ne peut pas être reconstruite après coup avec la cote courante.
    """
    v = b.get("valeur_initiale") or {}
    if v.get("statut") != "exacte":
        return None
    debut, date_valeur = _instant(b.get("debut")), _instant(v.get("date"))
    premiere_vue = _instant(b.get("premiere_vue"))
    ev, cote, juste = (_nombre(v.get(k)) for k in ("ev_pct", "cote_boostee", "cote_juste"))
    if (debut is None or date_valeur is None or date_valeur >= debut
            or (premiere_vue is not None and date_valeur < premiere_vue)
            or ev is None or ev < seuil or cote is None or cote <= 1 or cote > cote_max
            or juste is None or juste <= 1):
        return None
    p = 1.0 / juste
    # Contrôle de cohérence : les cotes source et l'EV doivent désigner le même prix.
    if not 0 < p < 1 or abs(100 * (cote * p - 1) - ev) > 0.4:
        return None
    return cote, p


def _simuler(base: dict[str, dict], nom: str, filtre, plafond: float = 10, taille=None, prix=None) -> dict:
    selection = {}
    for identifiant, boost in base.items():
        if not filtre(boost):
            continue
        b = dict(boost)  # aucune mutation de boosts.json
        mise = _mise(boost, plafond)
        if taille is not None:
            mise = taille(boost)
        if mise is not None and mise < 0.01:
            continue
        b["mise_max"] = mise
        if prix is not None:
            entree = prix(boost)
            if entree is None:
                continue
            b["cote_boostee_initiale"] = entree
        selection[identifiant] = b
    return simulation.bilan(selection, nom=nom)


def _premiers_par_match(base: dict[str, dict]) -> set[str]:
    """Diversification : le PREMIER boost vu par sport/match/heure, pas le gagnant a posteriori."""
    premiers = {}
    for identifiant, b in base.items():
        if b.get("long_terme"):
            continue
        debut = _instant(b.get("debut"))
        nom = (b.get("match") or "").strip().casefold()
        if not debut or not nom:
            continue
        cle = ((b.get("sport") or "").strip().casefold(), nom, debut.replace(second=0, microsecond=0))
        vu = _instant(b.get("premiere_vue")) or datetime.max.replace(tzinfo=timezone.utc)
        ordre = (vu, str(identifiant))
        if cle not in premiers or ordre < premiers[cle][0]:
            premiers[cle] = (ordre, identifiant)
    return {identifiant for _, identifiant in premiers.values()}


def construire(base: dict[str, dict]) -> dict[str, dict]:
    """Six challengers ; seuils fixés dans le code avant comparaison, zéro tuning sur le P&L."""
    premiere_selection = _premiers_par_match(base)
    eligibles_8 = {k: _valeur_initiale(b, 8, 4) for k, b in base.items()}
    eligibles_5 = {k: _valeur_initiale(b, 5, 5) for k, b in base.items()}

    def kelly_quart(b: dict) -> float | None:
        reference = eligibles_5.get(b["id"])
        if not reference:
            return None
        cote, proba = reference
        fraction = max(0.0, (cote * proba - 1) / (cote - 1))
        # Kelly 1/4, plafonné à 1 % de la banque fictive ET au maximum bookmaker.
        montant = min(BANQUE_DE_REFERENCE * fraction * 0.25, BANQUE_DE_REFERENCE * 0.01)
        maximum = _mise(b, 10)
        return round(min(montant, maximum), 2) if maximum is not None else None

    return {
        "C_plafond": _simuler(base, "C — tous les boosts, 10 € maximum", lambda b: True),
        "D_moderee": _simuler(base, "D — cote 1,60 à 3,50, 10 € maximum",
                             lambda b: (x := _cote(b)) is not None and 1.6 <= x <= 3.5),
        "E_48h": _simuler(base, "E — match dans les 48 h à la découverte, 10 € maximum",
                         _court_terme),
        "F_ev8": _simuler(base, "F — EV exacte ≥ 8 %, cote ≤ 4, 10 € maximum",
                         lambda b: eligibles_8.get(b["id"]) is not None,
                         prix=lambda b: eligibles_8[b["id"]][0]),
        "G_kelly": _simuler(base, "G — EV exacte ≥ 5 %, quart Kelly plafonné (1 000 € fictifs)",
                           lambda b: eligibles_5.get(b["id"]) is not None,
                           taille=kelly_quart, prix=lambda b: eligibles_5[b["id"]][0]),
        "H_1_match": _simuler(base, "H — premier boost par match, 10 € maximum",
                             lambda b: b["id"] in premiere_selection),
    }
