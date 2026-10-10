"""Cerveau v0.1 : pilote de décision prospectif et 100 % fictif.

Ce module ne s'entraîne PAS sur les anciens résultats. Il inscrit une trace
datée avant match, ne retouche pas les décisions passées et observe ensuite
les verdicts du collecteur. La première sélection positive fixe définitivement
la cote et la mise fictives utilisées dans le bilan, même si l'offre change.
"""
from __future__ import annotations

import math
from datetime import datetime, timezone

from .correspondance import normaliser

VERSION = "observation-v1.1"
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


def _reference_raison(v: dict) -> tuple[str, str]:
    """Diagnostic, pas estimation : l'absence d'une cote reste une abstention."""
    raison = str(v.get("raison") or "")
    r = raison.casefold()
    if "sport non suivi" in r:
        return "sport_non_suivi", "Sport non suivi par les références"
    if "match introuvable" in r:
        return "match_introuvable", "Rencontre introuvable dans les références"
    if "ligne absente" in r:
        return "ligne_absente", "Marché ou ligne identique indisponible"
    if "condition non cotée" in r or "type de pari non coté" in r:
        return "marche_non_cote", "Type de pari non coté par les références"
    if v.get("statut") == "approx":
        return "combiné_lie", "Conditions liées : probabilité seulement approximative"
    return "reference_absente", "Probabilité de référence non exploitable"


def _rencontres_distinctes(detail: list) -> bool:
    """Un combiné n'est exact que si ses matchs de référence sont identifiables ET distincts.

    Le calcul de valeur certifie déjà 'exacte'. Ce contrôle additionnel protège des
    identifiants de matchs présents chez plusieurs fournisseurs et des libellés proches.
    """
    cles = set()
    for d in detail:
        if not isinstance(d, dict) or not isinstance(d.get("match"), str):
            return False
        equipes = d["match"].split(" - ")
        if len(equipes) != 2 or not all(equipes):
            return False
        gauche, droite = (tuple(normaliser(nom)[0]) for nom in equipes)
        if not gauche or not droite or gauche == droite:
            return False
        cle = tuple(sorted((gauche, droite)))
        if cle in cles:
            return False
        cles.add(cle)
    return True


def _calcul(b, maintenant: str) -> dict:
    """Décide seulement avec l'information visible pendant ce scan, sans résultat futur."""
    cote = nombre(b.get("cote_boostee"))
    limite = nombre(b.get("mise_max"))
    v = b.get("valeur_derniere") or {}
    ev = nombre(v.get("ev_pct"))
    juste = nombre(v.get("cote_juste"))
    t, depart = instant(maintenant), instant(b.get("debut"))
    raisons = []
    code = None
    statut = "abstention"
    details = v.get("detail")
    details = details if isinstance(details, list) else []

    if b.get("long_terme"):
        statut, code = "hors_perimetre", "long_terme"
        raisons.append("Pari de saison ou long terme : suivi séparé, sans référence fiable")
    elif depart is None or t is None:
        statut, code = "hors_perimetre", "horaire_inconnu"
        raisons.append("Horaire de début non vérifiable")
    elif not 0 < (depart - t).total_seconds() <= HORIZON_HEURES * 3600:
        statut, code = "hors_perimetre", "hors_fenetre"
        raisons.append("Événement hors fenêtre d'évaluation de 72 heures")
    elif cote is None or cote <= 1 or limite is None or limite <= 0 or b.get("mise_max_supposee"):
        code = "mise_non_verifiee"
        raisons.append("Cote ou mise maximale non vérifiée")
    elif v.get("statut") != "exacte" or not details:
        code, raison = _reference_raison(v)
        raisons.append(raison)
    elif len(details) > 1 and not _rencontres_distinctes(details):
        code = "independance_non_verifiee"
        raisons.append("Combiné : indépendance des rencontres non vérifiable")
    elif instant(v.get("date")) != t:
        code = "reference_perimee"
        raisons.append("Référence non recalculée pendant ce scan")
    elif (ev is None or juste is None or juste <= 1
          or abs((cote / juste - 1) * 100 - ev) > 0.5):
        code = "ev_incoherente"
        raisons.append("EV incohérente ou insuffisamment documentée")
    elif not COTE_MIN <= cote <= COTE_MAX:
        statut, code = "ecarter", "cote_hors_bornes"
        raisons.append("Cote hors intervalle 1,60–5,00 du protocole")
    elif ev < SEUIL_EV:
        statut, code = "ecarter", "ev_insuffisante"
        raisons.append("EV exacte sous le seuil de +5 %")
    else:
        statut, code = "selectionner", "ev_positive"
        raisons.append("EV exacte ≥ +5 % et référence actualisée")
        if len(details) > 1:
            raisons.append(f"{len(details)} rencontres indépendantes identifiées")
        raisons.append("Mise fictive plafonnée à 10 €")

    return {
        "decision": statut,
        "motif_code": code,
        "raisons": raisons,
        "reference_raison": str(v.get("raison") or "")[:220] if statut == "abstention" else None,
        "cote": cote,
        "ev_pct": ev if v.get("statut") == "exacte" else None,
        "cote_juste": juste if v.get("statut") == "exacte" else None,
        "source": list(v.get("sources") or []) if v.get("statut") == "exacte" else [],
        "mise_fictive": round(min(limite, MISE_PLAFOND), 2) if statut == "selectionner" else None,
        "features": {
            "cote_origine": nombre(b.get("cote_origine")),
            "hausse_pct": nombre(b.get("hausse_pct")),
            "mise_max": limite,
            "mise_max_supposee": bool(b.get("mise_max_supposee")),
            "type_boost": b.get("type"),
            "horizon_heures": round((depart - t).total_seconds() / 3600, 1) if t and depart else None,
            "long_terme": bool(b.get("long_terme")),
            "qualite_reference": v.get("statut", "absente"),
            "nb_conditions": len(details),
        },
    }

def _signature(x):
    """Signale les véritables changements, sans recopier chaque passage horaire."""
    return (x["decision"], x["cote"], x["ev_pct"], x["cote_juste"],
            x["mise_fictive"], x.get("motif_code"), tuple(x["raisons"]))


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
    observations_reglees = 0
    for identifiant, entree in entrees.items():
        choisi = entree.get("premiere_selection")
        b = boosts.get(identifiant) or {}
        if (b.get("reglement") or {}).get("statut") in REGLES:
            observations_reglees += 1
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
    compteurs = {"selectionner": 0, "ecarter": 0, "abstention": 0, "hors_perimetre": 0}
    motifs = {}
    for e in entrees.values():
        if e.get("historique"):
            statut = e["historique"][-1].get("decision")
            if statut in compteurs:
                compteurs[statut] += 1
            code = e["historique"][-1].get("motif_code") or "ancien_format"
            motifs[code] = motifs.get(code, 0) + 1
    return {
        "observes": len(entrees),
        "observations_reglees": observations_reglees,
        "derniere_observation": registre.get("derniere_observation"),
        "decisions_courantes": compteurs,
        "motifs_courants": dict(sorted(motifs.items())),
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
