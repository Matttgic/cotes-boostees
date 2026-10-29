"""Validation du règlement par les scores : on rejoue les boosts DÉJÀ réglés (par l'IA ou à la main) et on
compare les verdicts. Aucune écriture dans la branche `donnees`.

Sortie dans $SORTIE (défaut sonde-scores/) : RAPPORT_SCORES.md, rapport_scores.json, resultats_validation.json.
Les boosts encore en attente sont examinés à blanc (combien seraient réglés, avec quel verdict).

Usage : DONNEES=donnees BRIGHTDATA_*=... python scripts/valider_scores.py
"""
from __future__ import annotations

import copy
import json
import os
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from boosts import reglement_scores, stockage  # noqa: E402
from boosts.acces import Navigateur, SecretsManquants  # noqa: E402
from boosts.scores.recherche import Lecteur, Recherche, archive_vide  # noqa: E402
from boosts.simulation import REGLES  # noqa: E402

SEUIL = 98.0


def main() -> int:
    dossier = Path(os.environ.get("DONNEES", "donnees"))
    sortie = Path(os.environ.get("SORTIE", "sonde-scores"))
    sortie.mkdir(parents=True, exist_ok=True)
    base = stockage.charger(dossier / "boosts.json")
    t = datetime.now(timezone.utc)

    deja = {k: copy.deepcopy(b) for k, b in base.items()
            if (b.get("reglement") or {}).get("statut") in REGLES and (b["reglement"].get("methode") != "scores")}
    verites = {k: b["reglement"]["statut"] for k, b in deja.items()}
    for b in deja.values():
        b.pop("reglement", None)
    attente = {k: copy.deepcopy(b) for k, b in base.items() if k not in deja and not (b.get("reglement") or {}).get("statut")}

    with tempfile.TemporaryDirectory() as tmp:
        try:
            nav = Navigateur(Path(tmp))
        except SecretsManquants:
            nav = None
        lecteur = Lecteur(nav)
        rech = Recherche(archive_vide(), lecteur, t)
        res_val = reglement_scores.regler(deja, rech, t, max_boosts=10_000)
        res_att = reglement_scores.regler(attente, rech, t, max_boosts=10_000)
        octets = nav.octets if nav else 0

    compares = [(k, verites[k], b["reglement"]["statut"]) for k, b in deja.items() if (b.get("reglement") or {}).get("methode") == "scores"]
    accord = [x for x in compares if x[1] == x[2]]
    desaccords = []
    for k, ia, sc in compares:
        if ia != sc:
            b = deja[k]
            desaccords.append({"id": k, "bookmaker": b["bookmaker"], "match": b["match"], "pari": b["pari"],
                               "verdict_ia_ou_manuel": ia, "verdict_scores": sc,
                               "explication_scores": b["reglement"]["explication"], "score": b["reglement"]["score"],
                               "explication_ia": ((base[k].get("reglement") or {}).get("explication") or "")[:300]})
    taux = 100 * len(accord) / len(compares) if compares else 0.0
    nouveaux = Counter((b.get("reglement") or {}).get("statut") for b in attente.values() if (b.get("reglement") or {}).get("methode") == "scores")
    par_bookmaker = Counter(b["bookmaker"] for b in attente.values() if (b.get("reglement") or {}).get("methode") == "scores")
    rapport = {
        "date": t.isoformat(timespec="seconds"), "boosts_rejoues": len(deja), "regles_par_scores": len(compares),
        "accord": len(accord), "desaccords": len(desaccords), "taux_accord_pct": round(taux, 2), "seuil_pct": SEUIL,
        "resume_validation": res_val, "resume_attente": res_att, "attente_reglables": dict(nouveaux),
        "attente_reglables_par_bookmaker": dict(par_bookmaker), "sources": rech.archive["sources"],
        "ligues": rech.archive["ligues"], "requetes": lecteur.requetes, "octets_proxy": octets,
        "erreurs_http": lecteur.derniere_erreur, "sans_correspondance": len(rech.archive["sans_correspondance"]),
        "decision": "ACTIVABLE" if compares and taux >= SEUIL and len(compares) >= 40 else "NON ACTIVABLE",
    }
    stockage.ecrire(sortie / "rapport_scores.json", {**rapport, "desaccords_detail": desaccords})
    stockage.ecrire(sortie / "resultats_validation.json", rech.archive)
    md = [f"# Validation du règlement par les scores ({rapport['date']})", "",
          f"**{rapport['decision']}** : accord {rapport['accord']}/{rapport['regles_par_scores']} = {rapport['taux_accord_pct']} % "
          f"(seuil {SEUIL} %, au moins 40 comparaisons).", "",
          f"- Boosts déjà réglés rejoués : {len(deja)} ; réglés par les scores : {len(compares)} ; désaccords : {len(desaccords)}",
          f"- Détail du rejeu : {res_val}", f"- En attente (à blanc) : {res_att} ; réglables : {dict(nouveaux)}",
          f"- Par bookmaker : {dict(par_bookmaker)}", f"- Sources : {json.dumps(rech.archive['sources'], ensure_ascii=False)}",
          f"- Erreurs HTTP : {lecteur.derniere_erreur}", f"- Requêtes : {lecteur.requetes}, proxy : {octets / 1e6:.1f} Mo", "",
          "## Désaccords"]
    for d in desaccords[:60]:
        md.append(f"- {d['bookmaker']} | {d['match']} | {d['pari']} : IA/manuel **{d['verdict_ia_ou_manuel']}** vs scores "
                  f"**{d['verdict_scores']}** ({d['explication_scores']} ; {d['score']})")
    (sortie / "RAPPORT_SCORES.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("\n".join(md[:12]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
