"""Cerveau v0.1 : pilote de décision prospectif et 100 % fictif.

Ce module ne s'entraîne PAS sur les anciens résultats. Il inscrit une trace
datée avant match, ne retouche pas les décisions passées et observe ensuite
les verdicts du collecteur. La première sélection positive fixe définitivement
la cote et la mise fictives utilisées dans le bilan, même si l'offre change.
"""
from __future__ import annotations

import math
from datetime import datetime, timezone

VERSION = "observation-v1"
SEUIL_EV = 5.0
COTE_MIN, COTE_MAX = 1.60, 5.00
HORIZON_HEURES = 72
MISE_PLAFOND = 10.0
REGLES = ("gagné", "perdu", "remboursé")


def nombre(valeur):
    try:
        x = float(valeur)
        return x if math.isfinite(x) else None
    except (ValueError, TypeError):
        return None


def instant(valeur):
    if not valeur:
        return None
    try:
        t = datetime.fromisoformat(str(valeur).replace("Z", "+00:00"))
        return t.replace(tzinfo=timezone.utc) if t.tzinfo is None else t.astimezone(timezone.utc)
    except (ValueError, TypeError):
        return None


def _calcul(b, maintenant: str) -> dict:
    """Décide UNIQUEMENT à partir des cotes et évaluations présentes à cet instant."""
    cote = nombre(b.get("cote_boostee"))
    limite = nombre(b.get("mise_max"))
    v = b.get("valeur_derniere") or {}
    ev = nombre(v.get("ev_pct"))
    juste = nombre(v.get("cote_juste"))
    t, depart = instant(maintenant), instant(b.get("debut"))
    raisons = []
    statut = "abstention"

    if b.get("long_terme") or depart is None or t is None:
        raisons.append("Paris long terme ou horaire non vérifiable")
    elif not 0 < (depart - t).total_seconds() <= HORIZON_HEURES * 3600:
        raisons.append("Départ hors fenêtre de 72 heures")
    elif cote is None or cote <= 1 or limite is None or limite <= 0 or b.get("mise_max_supposee"):
        raisons.append("Cote ou mise maximale non vérifiée")
    elif v.get("statut") != "exacte" or not v.get("detail") or len(v["detail"]) != 1:
        raisons.append("Marché absent, combiné ou probabilité non exacte")
    elif instant(v.get("date")) != t:
        raisons.append("Référence non recalculée pendant cette collecte")
    elif (ev is None or juste is None or juste <= 1
          or abs((cote / juste - 1) * 100 - ev) > 0.5):
        raisons.append("EV incohérente ou insuffisamment documentée")
    elif not COTE_MIN <= cote <= COTE_MAX:
        statut = "ecarter"
        raisons.append("Cote hors intervalle prudent 1,60–5,00")
    elif ev < SEUIL_EV:
        statut = "ecarter"
        raisons.append("EV exacte sous le seuil de +5 %")
    else:
        statut = "selectionner"
        raisons.append("EV exacte ≥ +5 %, pari simple et cote de référence fraîche")
        raisons.append("Mise fictive plafonnée à 10 €")

    return {
        "decision": statut,
        "raisons": raisons,
        "cote": cote,
        "ev_pct": ev if v.get("statut") == "exacte" else None,
        "cote_juste": juste if v.get("statut") == "exacte" else None,
        "source": list(v.get("sources") or []) if v.get("statut") == "exacte" else [],
        "mise_fictive": round(min(limite, MISE_PLAFOND), 2) if statut == "selectionner" else None,
    }


def _signature(x):
    """Signale les véritables changements, sans recopier chaque passage horaire."""
    return (x["decision"], x["cote"], x["ev_pct"], x["cote_juste"],
            x["mise_fictive"], tuple(x["raisons"]))


def enregistrer(base: dict, registre: dict, maintenant: str, heure_execution: str | None = None) -> dict:
    """Ajoute des décisions datées avant le coup d'envoi ; aucun backfill des matchs passés."""
    t = instant(maintenant)
    if t is None:
        raise ValueError("Date de collecte invalide")
    effectif = instant(heure_execution) if heure_execution else datetime.now(timezone.utc)
    if effectif is None:
        raise ValueError("Heure réelle invalide")
    registre.setdefault("schema", 1)
    registre.setdefault("modele", VERSION)
    entrees = registre.setdefault("entrees", {})
    ajoutees = changements = 0
    for b in sorted(base.values(), key=lambda x: str(x.get("id", ""))):
        identifiant = b.get("id")
        debut = instant(b.get("debut"))
        if not identifiant or debut is None or debut <= t or debut <= effectif:
            continue
        # Important : un ancien boost disponible=True n'est PAS forcément encore en vente.
        # Il doit avoir été effectivement vu au cours de CE passage.
        if instant(b.get("derniere_vue")) != t or b.get("disponible") is not True:
            continue
        proposition = _calcul(b, maintenant)
        proposition.update({
            "horodatage": maintenant,
            "version": VERSION,
        })
        entree = entrees.get(identifiant)
        if entree is None:
            entree = {
                "id": identifiant,
                "sport": b.get("sport") or "?",
                "bookmaker": b.get("bookmaker") or "?",
                "match": b.get("match") or "?",
                "pari": b.get("pari") or "?",
                "debut": b.get("debut"),
                "historique": [],
                "premiere_selection": None,
            }
            entrees[identifiant] = entree
            ajoutees += 1
        precedent = entree["historique"][-1] if entree["historique"] else None
        if precedent is None or _signature(precedent) != _signature(proposition):
            entree["historique"].append(proposition)
            changements += 1
        # Le premier pari fictif est VERROUILLÉ : aucun changement de cote/résultat a posteriori.
        if entree["premiere_selection"] is None and proposition["decision"] == "selectionner":
            entree["premiere_selection"] = dict(proposition)
    registre["derniere_observation"] = maintenant
    return {"nouveaux_boosts": ajoutees, "decisions_enregistrees": changements,
            "boosts_observes": len(entrees)}


def bilan(registre: dict, boosts: dict) -> dict:
    entrees = registre.get("entrees") or {}
    sorties = []
    for identifiant, entree in entrees.items():
        choisi = entree.get("premiere_selection")
        b = boosts.get(identifiant) or {}
        if not choisi:
            continue
        s = (b.get("reglement") or {}).get("statut", "en attente")
        if s not in REGLES:
            s = "en attente"
        cote, mise = nombre(choisi.get("cote")), nombre(choisi.get("mise_fictive"))
        if cote is None or mise is None or mise <= 0:
            continue
        gain = None
        if s == "gagné":
            gain = round(mise * (cote - 1), 2)
        elif s == "perdu":
            gain = -mise
        elif s == "remboursé":
            gain = 0.0
        sorties.append({
            "id": identifiant, "decision_date": choisi["horodatage"],
            "debut": entree.get("debut"), "sport": entree.get("sport"),
            "bookmaker": entree.get("bookmaker"), "match": entree.get("match"),
            "pari": entree.get("pari"), "cote": cote, "mise": mise,
            "ev_pct": choisi.get("ev_pct"), "statut": s, "gain": gain,
            "resultat_source": (b.get("reglement") or {}).get("source", "automatique") if gain is not None else None,
        })
    sorties.sort(key=lambda x: (x.get("debut") or "", x["id"]))
    regles = [x for x in sorties if x["gain"] is not None]
    capital, sommet, baisse = 0.0, 0.0, 0.0
    for x in regles:
        capital = round(capital + x["gain"], 2)
        sommet = max(sommet, capital)
        baisse = min(baisse, capital - sommet)
    mise_totale = round(sum(x["mise"] for x in regles), 2)
    gagnants = sum(x["statut"] == "gagné" for x in regles)
    perdants = sum(x["statut"] == "perdu" for x in regles)
    compteurs = {"selectionner": 0, "ecarter": 0, "abstention": 0}
    for e in entrees.values():
        if e.get("historique"):
            statut = e["historique"][-1].get("decision")
            if statut in compteurs:
                compteurs[statut] += 1
    return {
        "observes": len(entrees),
        "derniere_observation": registre.get("derniere_observation"),
        "decisions_courantes": compteurs,
        "paris_selectionnes": len(sorties),
        "paris_regles": len(regles),
        "paris_en_attente": len(sorties) - len(regles),
        "gagnes": gagnants, "perdus": perdants,
        "gain_net": round(sum(x["gain"] for x in regles), 2),
        "mises_reglees": mise_totale,
        "roi_pct": round(sum(x["gain"] for x in regles) / mise_totale * 100, 1) if mise_totale else None,
        "pire_baisse": round(baisse, 2),
        "historique_paris": sorties,
    }


def rafraichir(base: dict, registre: dict, maintenant: str, heure_execution: str | None = None) -> dict:
    resume = enregistrer(base, registre, maintenant, heure_execution=heure_execution)
    registre["bilan"] = bilan(registre, base)
    return resume
