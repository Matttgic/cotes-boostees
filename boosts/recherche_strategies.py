"""Replay chronologique : observations immuables, résultats connus avant décision.

Les performances restent une recherche rétrospective sur des règlements enregistrés
par le collecteur. Aucun classement obtenu ici n'est une validation prospective.
"""
from __future__ import annotations

import math
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
import json
import random

VERSION = "replay-v1"
DATE_GEL_RECHERCHE = "2026-10-14T00:00:00+00:00"
MIN_APPRENTISSAGE = 30
BANKROLL = 1000.0
REGLES = ("gagné", "perdu", "remboursé")
CHAMPS = ("id", "bookmaker", "sport", "match", "pari", "debut", "premiere_vue",
          "cote_boostee_initiale", "cote_origine", "mise_max", "mise_max_supposee", "long_terme", "disponible")


def instant(x):
    try:
        d = datetime.fromisoformat(str(x).replace("Z", "+00:00"))
        return d.replace(tzinfo=timezone.utc) if d.tzinfo is None else d.astimezone(timezone.utc)
    except (ValueError, TypeError):
        return None


def nombre(x):
    try:
        v = float(x)
        return v if math.isfinite(v) else None
    except (ValueError, TypeError):
        return None


def sport(b):
    s = str(b.get("sport") or "?").casefold()
    return "rugby" if s.startswith("rugby") else s


def rencontre(b):
    d = instant(b.get("debut"))
    return sport(b), str(b.get("match") or "").strip().casefold(), d.isoformat()[:16] if d else "?"


def charger_historique(path):
    p = Path(path)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    seed = Path(__file__).resolve().parent.parent / "analyses" / "historique-strategies.json"
    return json.loads(seed.read_text(encoding="utf-8")) if seed.exists() else {
        "schema": 1, "observations": {}, "valeurs": {}, "resultats": []}


def observer(base, historique, maintenant, heure_execution=None):
    """Capture au scan courant ; ne reconstitue jamais une observation passée."""
    scan = instant(maintenant)
    receipt = heure_execution or maintenant
    t = instant(receipt)
    observations = historique.setdefault("observations", {})
    valeurs = historique.setdefault("valeurs", {})
    resultats = historique.setdefault("resultats", [])
    derniers = {r["id"]: r["statut"] for r in resultats}
    for identifiant, b in base.items():
        debut = instant(b.get("debut"))
        if identifiant not in observations and t and debut and t < debut \
                and b.get("disponible") is True and instant(b.get("derniere_vue")) == scan:
            observations[identifiant] = {**{k: b.get(k) for k in CHAMPS}, "available_at": receipt}
            observations[identifiant]["cote_boostee_initiale"] = b.get("cote_boostee")
        v = b.get("valeur_derniere") or {}
        if identifiant in observations and identifiant not in valeurs and t and debut and t < debut \
                and instant(v.get("date")) == scan and v.get("statut") in ("exacte", "interpolee", "approx"):
            valeurs[identifiant] = {**{k: v.get(k) for k in ("statut", "cote_boostee", "cote_juste", "ev_pct", "date")},
                                    "available_at": receipt}
        r = b.get("reglement") or {}
        if identifiant in observations and r.get("statut") in REGLES and derniers.get(identifiant) != r["statut"]:
            resultats.append({"id": identifiant, "statut": r["statut"], "regle_le": r.get("regle_le"),
                              "available_at": receipt, "modele": r.get("modele"), "source": r.get("source")})
    historique["derniere_observation"] = receipt


def _eligible(b, date, cote=None):
    c = nombre(cote if cote is not None else b.get("cote_boostee_initiale"))
    mise = nombre(b.get("mise_max"))
    debut = instant(b.get("debut"))
    return bool(c and c > 1 and mise and mise > 0 and date and debut and date < debut
                and not b.get("long_terme") and not b.get("mise_max_supposee")
                and b.get("disponible", True))


def regles_candidates():
    """Grille limitée et publique ; J n'en choisit une qu'avec les résultats antérieurs."""
    bands = ((1.5, 2.5), (1.5, 3.5), (1.5, 5), (2, 3.5), (2, 5), (3, 5), (1.5, 8))
    scopes = (("tous", None), ("sport", "tennis"), ("sport", "football"),
              ("sport", "hockey sur glace"), ("sport", "basketball"), ("sport", "rugby"),
              ("bookmaker", "Winamax"), ("bookmaker", "Unibet"))
    return [{"id": f"{kind}:{value or 'tous'}:{lo:g}-{hi:g}", "scope": kind, "value": value,
             "min": lo, "max": hi} for kind, value in scopes for lo, hi in bands]


def filtre(b, r):
    c = nombre(b.get("cote_boostee_initiale"))
    return bool(c and r["min"] <= c <= r["max"]
                and (r["scope"] == "tous" or (r["scope"] == "sport" and sport(b) == r["value"])
                     or (r["scope"] == "bookmaker" and b.get("bookmaker") == r["value"])))


def _retour(b, statut):
    return float(b["cote_boostee_initiale"]) - 1 if statut == "gagné" else -1 if statut == "perdu" else 0


def choisir_regle(entrainement):
    scored = []
    for rule in regles_candidates():
        seen, returns = set(), []
        for b, label, available in sorted(entrainement.values(), key=lambda x: (x[0]["available_at"], x[0]["id"])):
            key = rencontre(b)
            if key in seen or not filtre(b, rule):
                continue
            seen.add(key)
            returns.append(_retour(b, label))
        n = len(returns)
        if n < 12:
            continue
        # Retours ramenés vers zéro avec 20 observations virtuelles, puis pénalité de dispersion.
        # Ce score n'est PAS un intervalle de confiance.
        mean = sum(returns) / (n + 20)
        variance = sum((x - sum(returns) / n) ** 2 for x in returns) / max(1, n - 1)
        score = mean - 0.5 * math.sqrt(variance / (n + 20))
        scored.append((score, rule["id"], rule, n))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return (scored[0][2], scored[0][0], scored[0][3]) if scored and scored[0][0] > 0 else (None, 0, 0)


def _sigmoid(x):
    x = max(-30, min(30, x))
    return 1 / (1 + math.exp(-x))


def _prior(b):
    normal = nombre(b.get("cote_origine"))
    cote = nombre(b.get("cote_boostee_initiale"))
    # Le prix normal garde la marge du bookmaker ; c'est un prior à calibrer, pas une cote juste.
    return min(0.95, max(0.02, 1 / (normal if normal and normal > 1 else cote)))


def _features(b, categories):
    p = _prior(b)
    x = [1.0, math.log(float(b["cote_boostee_initiale"])) - 1.1]
    x += [float(sport(b) == c) for c in categories[0]]
    x += [float((b.get("bookmaker") or "?") == c) for c in categories[1]]
    return math.log(p / (1 - p)), x


def ajuster_modele(entrainement):
    rows = [v for v in entrainement.values() if v[1] in ("gagné", "perdu")]
    categories = (sorted({sport(b) for b, _, _ in rows}), sorted({b.get("bookmaker") or "?" for b, _, _ in rows}))
    counts = Counter(rencontre(b) for b, _, _ in rows)
    train = [(*_features(b, categories), float(label == "gagné"), 1 / counts[rencontre(b)]) for b, label, _ in rows]
    coefficients = [0.0] * (2 + len(categories[0]) + len(categories[1]))
    penalties = [3.0, 8.0] + [6.0] * len(categories[0]) + [12.0] * len(categories[1])
    lipschitz = max(penalties) + 0.25 * sum(w * sum(v * v for v in x) for _, x, _, w in train)
    step = 1 / max(1, lipschitz)
    for _ in range(120):
        gradient = [penalties[i] * v for i, v in enumerate(coefficients)]
        for offset, features, label, weight in train:
            residual = weight * (_sigmoid(offset + sum(c * x for c, x in zip(coefficients, features))) - label)
            for i, x in enumerate(features):
                gradient[i] += residual * x
        coefficients = [c - step * g for c, g in zip(coefficients, gradient)]
    return categories, coefficients


def predire(b, modele):
    categories, coefficients = modele
    offset, features = _features(b, categories)
    return _sigmoid(offset + sum(c * x for c, x in zip(coefficients, features)))


def _evenements(historique, valeur=False):
    observations = historique.get("observations", {})
    events = []
    for identifiant, b in observations.items():
        if valeur:
            v = historique.get("valeurs", {}).get(identifiant)
            if not v:
                continue
            date = instant(v.get("available_at"))
            cote = nombre(v.get("cote_boostee"))
            if _eligible(b, date, cote):
                events.append((date, 0, identifiant, {**b, "cote_boostee_initiale": cote, "reference": v}))
        else:
            date = instant(b.get("available_at"))
            if _eligible(b, date):
                events.append((date, 0, identifiant, b))
    for index, r in enumerate(historique.get("resultats", [])):
        date = instant(r.get("available_at"))
        regle_le = instant(r.get("regle_le"))
        if date and regle_le:
            date = max(date, regle_le)
        b = observations.get(r["id"])
        if date and b and instant(b.get("debut")) and date > instant(b["debut"]) and _eligible(b, instant(b.get("available_at"))):
            events.append((date, 1, r["id"], r))
    # Décisions AVANT règlements au même instant : aucune connaissance du résultat du scan en cours.
    return sorted(events, key=lambda x: (x[0], x[1], x[2]))


def simuler(historique, policy="modele", taille="fixe", rule=None, minimum_ev=5.0, mise_fixe=10.0, debut_paris=None):
    """Une bankroll réelle en simulation : mises immobilisées jusqu'au règlement observé."""
    valeur = policy == "valeur"
    training, paris, exposure = {}, {}, {}
    cash, net, peak, drawdown = BANKROLL, 0.0, 0.0, 0.0
    curves, decisions, rule_log = [], [], []
    selected_matches = set()
    current_rule, current_day, modele, trained_signature = None, None, None, None
    start = None
    for date, kind, identifiant, payload in _evenements(historique, valeur):
        if kind == 1:
            b = historique["observations"][identifiant]
            training[identifiant] = (b, payload["statut"], date.isoformat())
            trade = paris.get(identifiant)
            if trade:
                old = trade.get("gain")
                gain = round(trade["mise"] * (trade["cote"] - 1), 2) if payload["statut"] == "gagné" else -trade["mise"] if payload["statut"] == "perdu" else 0.0
                if old is None:
                    cash += trade["mise"] + gain
                    exposure.pop(identifiant, None)
                    net += gain
                else:
                    cash += gain - old
                    net += gain - old
                trade.update(statut=payload["statut"], gain=gain, resultat_disponible=date.isoformat())
                point = {"debut": date.isoformat(), "cumul": round(net, 2)}
                if curves and curves[-1]["debut"] == point["debut"]:
                    curves[-1] = point
                else:
                    curves.append(point)
            continue
        b = payload
        if debut_paris and date < instant(debut_paris):
            continue
        cote = float(b["cote_boostee_initiale"])
        n = sum(label in ("gagné", "perdu") for _, label, _ in training.values())
        if n < MIN_APPRENTISSAGE:
            continue
        if start is None:
            start = date.isoformat()
        if identifiant in training:
            continue
        probability, ev, motif, applied = None, None, "filtre", None
        selected = False
        if policy == "regle":
            selected, applied = filtre(b, rule), rule
        elif policy == "temoin":
            selected = True
        elif policy == "adaptative":
            day = date.strftime("%Y-%m-%d")
            if day != current_day:
                current_rule, score, evidence = choisir_regle(training)
                rule_log.append({"date": date.isoformat(), "regle": current_rule, "score": round(score, 4), "regles_entrainement": n, "taille_selection": evidence})
                current_day = day
            selected, applied = current_rule is not None and filtre(b, current_rule), current_rule
        elif policy == "valeur":
            v = b["reference"]
            juste = nombre(v.get("cote_juste"))
            declared = nombre(v.get("ev_pct"))
            probability = 1 / juste if juste and juste > 1 else None
            ev = 100 * (cote * probability - 1) if probability is not None else None
            selected = (v.get("statut") in ("exacte", "interpolee") and ev is not None
                        and declared is not None and abs(ev - declared) <= 0.5 and ev >= minimum_ev)
        else:
            signature = tuple(sorted((k, v[1], v[2]) for k, v in training.items()))
            if signature != trained_signature:
                modele = ajuster_modele(training)
                trained_signature = signature
            probability = predire(b, modele)
            ev = 100 * (cote * probability - 1)
            selected = 1.5 <= cote <= 8 and ev >= minimum_ev
        key = rencontre(b)
        if selected and policy != "temoin" and key in selected_matches:
            selected, motif = False, "match_deja_joue"
        equity = cash + sum(x["mise"] for x in exposure.values())
        maximum = min(float(b["mise_max"]), 20.0)
        if taille == "kelly":
            # Demi-edge puis Kelly 1/8 : aucune mise proportionnelle à une proba non amortie.
            edge = max(0, (cote * probability - 1) * 0.5) if probability is not None else 0
            stake = min(maximum, equity * edge / (cote - 1) / 8, equity * 0.02)
        elif taille == "proportionnelle":
            stake = min(maximum, equity * 0.01)
        else:
            stake = min(maximum, mise_fixe)
        open_match = sum(t["mise"] for t in exposure.values() if rencontre(t) == key)
        stake = min(stake, max(0, equity * 0.10 - sum(x["mise"] for x in exposure.values())),
                    max(0, equity * 0.02 - open_match), max(0, cash))
        stake = math.floor((stake + 1e-9) * 100) / 100
        if selected and stake < 1:
            selected, motif = False, "exposition_ou_mise_insuffisante"
        decision = {"id": identifiant, "date": date.isoformat(), "joue": selected,
                    "p_modele": round(probability, 6) if probability is not None else None,
                    "p_prior": round(_prior(b), 6),
                    "ev_modele_pct": round(ev, 3) if ev is not None else None,
                    "regles_entrainement": n, "dernier_resultat_utilise": max(v[2] for v in training.values()),
                    "regle": applied["id"] if applied else None, "motif": "selection" if selected else motif}
        decisions.append(decision)
        if not selected:
            continue
        trade = {"id": identifiant, "sport": b.get("sport"), "bookmaker": b.get("bookmaker"),
                 "match": b.get("match"), "pari": b.get("pari"), "debut": b.get("debut"),
                 "cote": cote, "mise": stake, "statut": "en attente", "gain": None,
                 "decision_date": date.isoformat(), "bankroll_avant": round(equity, 2),
                 "p_modele": decision["p_modele"], "ev_modele_pct": decision["ev_modele_pct"],
                 "regle": decision["regle"]}
        paris[identifiant] = trade
        exposure[identifiant] = trade
        selected_matches.add(key)
        cash -= stake
    from . import simulation
    copies = {k: {**p, "cote_boostee_initiale": p["cote"], "mise_max": p["mise"],
                  "reglement": {"statut": p["statut"]}} for k, p in paris.items()}
    result = simulation.bilan(copies, nom=policy)
    result["paris"] = sorted(paris.values(), key=lambda p: (p["decision_date"], p["id"]))
    result["courbe"] = curves
    for point in curves:
        peak = max(peak, point["cumul"])
        drawdown = min(drawdown, point["cumul"] - peak)
    result["global"]["pire_baisse"] = round(drawdown, 2)
    result["replay"] = {"version": VERSION, "debut_evaluation": start, "banque_initiale": BANKROLL,
                        "cash_final": round(cash, 2), "mises_ouvertes": round(sum(t["mise"] for t in exposure.values()), 2),
                        "banque_finale": round(cash + sum(t["mise"] for t in exposure.values()), 2),
                        "decisions": decisions, "regles_par_jour": rule_log, "taille_mise": taille,
                        "seuil_ev_estimee": minimum_ev, "mise_fixe": mise_fixe,
                        "reglements": "verdicts du collecteur, non audités indépendamment"}
    labels = {r["id"]: r["statut"] for r in historique.get("resultats", [])}
    scored = [(d, float(labels[d["id"]] == "gagné")) for d in decisions
              if d["p_modele"] is not None and labels.get(d["id"]) in ("gagné", "perdu")]
    result["replay"]["calibration"] = {
        "predictions_reglees": len(scored),
        "brier_modele": round(sum((d["p_modele"] - y) ** 2 for d, y in scored) / len(scored), 4) if scored else None,
        "brier_prior_bookmaker": round(sum((d["p_prior"] - y) ** 2 for d, y in scored) / len(scored), 4) if scored else None,
    }
    daily = defaultdict(lambda: {"regles": 0, "mise": 0.0, "gain": 0.0})
    groups = defaultdict(lambda: [0.0, 0.0])
    for p in paris.values():
        if p["gain"] is None:
            continue
        d = daily[p["decision_date"][:10]]
        d["regles"] += 1
        d["mise"] = round(d["mise"] + p["mise"], 2)
        d["gain"] = round(d["gain"] + p["gain"], 2)
        g = groups[rencontre(p)]
        g[0] += p["gain"]
        g[1] += p["mise"]
    result["replay"]["par_jour_decision"] = dict(sorted(daily.items()))
    # Dispersion conditionnelle aux paris pris ; ne corrige pas le choix a posteriori de l'algorithme.
    rng = random.Random(611)
    returns = []
    blocks = list(groups.values())
    if blocks:
        for _ in range(1000):
            draw = rng.choices(blocks, k=len(blocks))
            stake = sum(x[1] for x in draw)
            returns.append(100 * sum(x[0] for x in draw) / stake if stake else 0)
        returns.sort()
    result["replay"]["dispersion_roi_90_pct"] = [round(returns[49], 1), round(returns[949], 1)] if returns else None
    return result


def analyser(historique, grille=True):
    strategies = {
        "J_adaptative": simuler(historique, "adaptative", "proportionnelle"),
        "K_modele": simuler(historique, "modele", "fixe"),
        "L_kelly_dynamique": simuler(historique, "modele", "kelly"),
        "M_modele_20": simuler(historique, "modele", "fixe", mise_fixe=20),
    }
    names = {"J_adaptative": "J — filtre choisi quotidiennement avec les seuls résultats passés",
             "K_modele": "K — probabilité calibrée progressivement, EV estimée ≥ 5 %, 10 € maximum",
             "L_kelly_dynamique": "L — même modèle, demi-edge et Kelly 1/8 sur bankroll réelle",
             "M_modele_20": "M — même modèle, 20 € maximum et plafond de 2 % par rencontre"}
    for key, v in strategies.items():
        v["strategie"] = names[key]
    controls = {"temoin_10": simuler(historique, "temoin"), "temoin_20": simuler(historique, "temoin", mise_fixe=20),
                "value_0": simuler(historique, "valeur", minimum_ev=0),
                "value_5": simuler(historique, "valeur", minimum_ev=5)}
    ranking = []
    sensitivity = []
    if grille:
        for rule in regles_candidates():
            b = simuler(historique, "regle", rule=rule)
            ranking.append({"regle": rule, "global": b["global"], "debut_evaluation": b["replay"]["debut_evaluation"]})
        ranking.sort(key=lambda x: (-x["global"]["gain_net"], x["regle"]["id"]))
        for ev in (0, 5, 10):
            for stake in (5, 10, 20):
                b = simuler(historique, "modele", minimum_ev=ev, mise_fixe=stake)
                sensitivity.append({"seuil_ev": ev, "mise_max": stake, "global": b["global"]})
    future = {
        "J_adaptative": simuler(historique, "adaptative", "proportionnelle", debut_paris=DATE_GEL_RECHERCHE),
        "K_modele": simuler(historique, "modele", debut_paris=DATE_GEL_RECHERCHE),
        "L_kelly_dynamique": simuler(historique, "modele", "kelly", debut_paris=DATE_GEL_RECHERCHE),
        "M_modele_20": simuler(historique, "modele", mise_fixe=20, debut_paris=DATE_GEL_RECHERCHE),
    }
    future_controls = {"temoin_10": simuler(historique, "temoin", debut_paris=DATE_GEL_RECHERCHE),
                       "temoin_20": simuler(historique, "temoin", mise_fixe=20, debut_paris=DATE_GEL_RECHERCHE)}
    return {"version": VERSION, "source_sha": historique.get("source_sha"),
            "derniere_observation": historique.get("derniere_observation"),
            "observations": len(historique.get("observations", {})), "valeurs": len(historique.get("valeurs", {})),
            "reglements": len(historique.get("resultats", [])), "minimum_apprentissage": MIN_APPRENTISSAGE,
            "qualite": {"producteurs_verdicts": dict(Counter(r.get("modele") or r.get("source") or "inconnu" for r in historique.get("resultats", []))),
                        "observations_apres_debut": sum(instant(b.get("available_at")) >= instant(b.get("debut")) for b in historique.get("observations", {}).values() if instant(b.get("available_at")) and instant(b.get("debut"))),
                        "mises_supposees": sum(bool(b.get("mise_max_supposee")) for b in historique.get("observations", {}).values()),
                        "methodes_value": dict(Counter(v.get("statut") for v in historique.get("valeurs", {}).values()))},
            "limites": ["Rejeu rétrospectif choisi après consultation de ce même historique.",
                         "Règlements automatiques non vérifiés indépendamment.",
                         "Prix normal bookmaker utilisé comme prior, avec marge ; EV du modèle estimée.",
                         "56 filtres explorés : leur meilleur score final est choisi après coup.",
                         "9 variantes de seuil et mise explorées : M est une candidate choisie après cette comparaison.",
                         "Bankroll 1 000 €, exposition ouverte ≤ 10 %, par libellé de rencontre ≤ 2 %.",
                         "Les combinés peuvent partager des rencontres non identifiables par leurs seuls libellés."],
            "strategies": strategies, "temoins": controls, "classement_exploratoire": ranking,
            "sensibilite_modele": sensitivity,
            "prospectif": {"date_debut": DATE_GEL_RECHERCHE, "banque_initiale": BANKROLL,
                           "strategies": future, "temoins": future_controls}}


def verrouiller_decisions(historique, recherche):
    """Le journal prospectif persiste les mises et probabilités, par version de protocole."""
    journal = historique.setdefault("journal_recherche", {}).setdefault(VERSION, {})
    for key, bilan in recherche["prospectif"]["strategies"].items():
        log = journal.setdefault(key, {})
        mises = {p["id"]: p["mise"] for p in bilan["paris"]}
        for d in bilan["replay"]["decisions"]:
            signature = {k: d[k] for k in ("id", "date", "joue", "p_modele", "ev_modele_pct", "regle")}
            signature["mise"] = mises.get(d["id"])
            if d["id"] in log and log[d["id"]] != signature:
                raise ValueError("Une décision prospective a changé : créer une nouvelle version de recherche")
            log[d["id"]] = signature


def resume(recherche):
    def compact(b):
        replay = b["replay"]
        return {"strategie": b["strategie"], "global": b["global"],
                "banque_finale": replay["banque_finale"], "debut_evaluation": replay["debut_evaluation"],
                "dispersion_roi_90_pct": replay["dispersion_roi_90_pct"]}
    return {"version": recherche["version"], "source_sha": recherche.get("source_sha"),
            "derniere_observation": recherche["derniere_observation"],
            "minimum_apprentissage": recherche["minimum_apprentissage"], "reglements": recherche["reglements"],
            "temoins": {k: compact(v) for k, v in recherche["temoins"].items()},
            "calibration": recherche["strategies"]["K_modele"]["replay"]["calibration"],
            "prospectif": {"date_debut": recherche["prospectif"]["date_debut"],
                           "strategies": {k: compact(v) for k, v in recherche["prospectif"]["strategies"].items()},
                           "temoins": {k: compact(v) for k, v in recherche["prospectif"]["temoins"].items()}}}


def markdown(recherche):
    def pct(v):
        return "—" if v is None else f"{v:+.1f} %"
    def row(k, b):
        g = b["global"]
        return f"| {k} | {g['regles']} / {g['paris']} | {g['mise_totale']:.2f} € | {g['gain_net']:+.2f} € | {pct(g['roi_pct'])} | {g['pire_baisse']:.2f} € |"
    lines = ["# Recherche de stratégies — replay chronologique", "",
             f"Source initiale : branche donnees, commit `{recherche.get('source_sha')}` ; dernière observation du {recherche['derniere_observation']}.",
             "Les observations initiales, premières valeurs et heures de publication des règlements proviennent de 141 instantanés Git.",
             "Une offre retirée du fichier courant reste dans l'historique, sans être transformée en perte.", "",
             "## Méthode", "",
             "Les 30 premiers résultats disponibles servent d'amorçage. Chaque nouvelle offre est ensuite décidée avec les seuls résultats déjà publiés, strictement avant cet instant.",
             "Le prix, la mise maximale et les catégories sont pris dans le premier instantané disponible avant match. Une value tardive ne remonte jamais à la découverte de l'offre.",
             "Les mises restent immobilisées jusqu'à la publication du règlement, y compris lorsque plusieurs matchs ont lieu simultanément. Banque initiale : 1 000 €. Plafonds : 10 % de mises ouvertes, 2 % par libellé de rencontre.",
             "J choisit quotidiennement parmi 56 filtres, avec au moins 12 anciens résultats et un score pénalisant les faibles échantillons et la dispersion. Il mise 1 % de la bankroll, maximum 20 €.",
             "K calibre une régression logistique régularisée sur le prix normal bookmaker, la cote, le sport et le bookmaker. Les multiples boosts d'un match se partagent un poids total de 1 pendant l'apprentissage. EV estimée ≥ 5 %, maximum 10 €.",
             "L utilise la même probabilité avec l'edge réduit de moitié puis Kelly 1/8, calculé sur la bankroll disponible et plafonné à 20 €. M utilise le même modèle que K, avec 20 € maximum.",
             "Le prix normal contient la marge du bookmaker : ce prior et l'EV du modèle ne sont pas des références de cote juste.", "",
             "## Comparaison sur la période après amorçage", "",
             "| Simulation | Réglés / paris | Mises réglées | Gain net | ROI | Baisse maximale |", "|---|---|---|---|---|---|"]
    for k, b in {**recherche["temoins"], **recherche["strategies"]}.items():
        lines.append(row(k, b))
    lines += ["", "Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.",
              "M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.", "",
              "## Stabilité et calibration", ""]
    cal = recherche["strategies"]["K_modele"]["replay"]["calibration"]
    lines.append(f"Sur {cal['predictions_reglees']} prévisions réglées : score de Brier du modèle {cal['brier_modele']}, prior bookmaker {cal['brier_prior_bookmaker']} (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.")
    lines += ["", "| Simulation | Dispersion ROI à 90 % par bootstrap de rencontres |", "|---|---|"]
    for k, b in recherche["strategies"].items():
        interval = b["replay"]["dispersion_roi_90_pct"]
        lines.append(f"| {k} | {interval} |")
    lines.append("Ces intervalles décrivent la dispersion des paris déjà sélectionnés ; ils ne corrigent pas la sélection a posteriori des méthodes et ne simulent pas un nouvel apprentissage complet.")
    for k, b in recherche["strategies"].items():
        lines += ["", f"### {k} par jour de décision", "", "| Jour | Réglés | Gain net |", "|---|---|---|"]
        for day, g in b["replay"]["par_jour_decision"].items():
            lines.append(f"| {day} | {g['regles']} | {g['gain']:+.2f} € |")
        lines += ["", "| Sport | Réglés | Gain net |", "|---|---|---|"]
        for s, g in b["par_sport"].items():
            lines.append(f"| {s} | {g['regles']} | {g['gain_net']:+.2f} € |")
    lines += ["", "## Sensibilité du modèle : les 9 variantes explorées", "",
              "| EV estimée minimale | Mise maximale | Réglés | Gain net | ROI | Baisse maximale |", "|---|---|---|---|---|---|"]
    for x in recherche["sensibilite_modele"]:
        g = x["global"]
        lines.append(f"| {x['seuil_ev']} % | {x['mise_max']} € | {g['regles']} | {g['gain_net']:+.2f} € | {pct(g['roi_pct'])} | {g['pire_baisse']:.2f} € |")
    lines += ["", "## Classement exploratoire des 56 filtres", "",
              "Ce classement a été trié après lecture de tous les résultats. Il sert à proposer des hypothèses, pas à valider une stratégie. Le meilleur filtre tennis repose sur très peu de paris.",
              "| Filtre | Réglés | Gain net | ROI |", "|---|---|---|---|"]
    for r in recherche["classement_exploratoire"]:
        g = r["global"]
        lines.append(f"| {r['regle']['id']} | {g['regles']} | {g['gain_net']:+.2f} € | {pct(g['roi_pct'])} |")
    lines += ["", "## Suivi futur gelé", "",
              f"Départ : {recherche['prospectif']['date_debut']}. Chaque simulation repart avec 1 000 € et peut apprendre des anciens règlements, mais ne joue que les nouvelles observations à partir de cette date.",
              "Les décisions, probabilités et mises sont conservées dans un journal par version. Une modification d'une décision existante est refusée ; une évolution du modèle exige une nouvelle version.", "",
              "## Limites", ""]
    lines += [f"- {x}" for x in recherche["limites"]]
    lines += ["", f"Producteurs des {recherche['reglements']} événements de règlement : {recherche['qualite']['producteurs_verdicts']}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.",
              "La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.", "",
              "Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.", ""]
    return "\n".join(lines)
