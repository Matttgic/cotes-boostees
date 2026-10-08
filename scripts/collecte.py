"""Un passage de collecte : lit les boosts des bookmakers et met à jour l'historique.

Fichiers (dossier $DONNEES, par défaut ./donnees, branche git `donnees`) :
- boosts.json : tous les boosts jamais vus (voir boosts/stockage.py) ;
- etat.json   : dernier passage, compteurs, consommation du proxy, 200 derniers passages.

Code de sortie 1 si aucun bookmaker n'a pu être lu : le workflow passe au rouge et GitHub
t'envoie un e-mail.

Usage : BRIGHTDATA_*=... python scripts/collecte.py
"""
from __future__ import annotations

import os
import sys
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from boosts import stockage, winamax          # noqa: E402
from boosts.acces import Navigateur, masquer  # noqa: E402

COLLECTEURS = {"winamax": winamax.collecter}
JOURNAL_MAX = 200


def main() -> int:
    dossier = Path(os.environ.get("DONNEES", "donnees"))
    maintenant = datetime.now(timezone.utc).isoformat(timespec="seconds")
    base = stockage.charger(dossier / "boosts.json")
    etat = stockage.charger(dossier / "etat.json") or {}

    passage = {"date": maintenant, "bookmakers": {}}
    with tempfile.TemporaryDirectory() as tmp:
        nav = Navigateur(Path(tmp))
        for nom, collecter in COLLECTEURS.items():
            try:
                lus = collecter(nav)
            except Exception as e:  # un bookmaker en panne n'arrête pas les autres
                passage["bookmakers"][nom] = {"erreur": masquer(f"{type(e).__name__} : {e}")[:300]}
                print(f"[{nom}] ERREUR", masquer(traceback.format_exc())[-1500:], file=sys.stderr)
                continue
            nouveaux, modifies = stockage.fusionner(base, lus, maintenant)
            passage["bookmakers"][nom] = {"boosts_en_ligne": len(lus), "nouveaux": nouveaux,
                                          "cotes_modifiees": modifies}
            print(f"[{nom}] {len(lus)} boosts en ligne, {nouveaux} nouveaux, {modifies} cotes modifiées")
        passage["octets_proxy"] = nav.octets
        passage["requetes"] = nav.requetes

    etat["dernier_passage"] = passage
    etat["octets_proxy_total"] = int(etat.get("octets_proxy_total", 0)) + passage["octets_proxy"]
    etat["boosts_total"] = len(base)
    etat["journal"] = ([passage] + list(etat.get("journal") or []))[:JOURNAL_MAX]
    stockage.ecrire(dossier / "boosts.json", base)
    stockage.ecrire(dossier / "etat.json", etat)

    reussis = [n for n, v in passage["bookmakers"].items() if "erreur" not in v]
    print(f"Proxy : {passage['octets_proxy'] / 1e6:.2f} Mo ce passage, "
          f"{etat['octets_proxy_total'] / 1e9:.3f} Go au total. Historique : {len(base)} boosts.")
    return 0 if reussis else 1


if __name__ == "__main__":
    sys.exit(main())
