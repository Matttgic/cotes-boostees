"""Un passage de collecte : lit les boosts des bookmakers et met à jour l'historique.

Fichiers (dossier $DONNEES, par défaut ./donnees, branche git `donnees`) :
- boosts.json : tous les boosts jamais vus (voir boosts/stockage.py) ;
- etat.json   : dernier passage, compteurs, consommation du proxy, 200 derniers passages ;
- reglements_manuels.json : tes corrections à la main, prioritaires ({"id du boost": "gagné"}) ;
- bilan.json + BILAN.md : stratégies A-H ;
- cerveau.json : décisions horodatées et bilans des choix fictifs avant match.

Règlement par l'IA seulement si le secret OPENAI_API_KEY (ou ANTHROPIC_API_KEY) est présent.

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

from boosts import cerveau, evaluation, rapport, reglement, simulation, stockage, unibet, winamax  # noqa: E402
from boosts.acces import Navigateur, masquer  # noqa: E402

COLLECTEURS = {"winamax": winamax.collecter, "unibet": unibet.collecter}
AVEC_CACHE = {"unibet"}          # collecteurs qui gardent un cache entre deux passages (etat.json)
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
                lus = collecter(nav, etat.setdefault(f"cache_{nom}", {})) if nom in AVEC_CACHE else collecter(nav)
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

    # Les paris "titre NBA" de Winamax doivent attendre la fin de saison,
    # même lorsque leur date de début officielle est déjà passée.
    passage["long_terme_winamax_corriges"] = winamax.corriger_long_terme(base)

    # valeur face à Pinnacle (stratégie B) : décomposition IA puis cotes justes
    try:
        passage["evaluation"] = evaluation.evaluer_boosts(base, maintenant)
    except Exception as e:
        passage["evaluation"] = {"erreur": f"{type(e).__name__} : {e}"[:300]}
        print("Évaluation : ERREUR", traceback.format_exc()[-1500:], file=sys.stderr)
    print("Évaluation :", passage["evaluation"])

    # Photographier les décisions pendant que les événements sont encore à venir.
    registre_cerveau = stockage.charger(dossier / "cerveau.json") or {}
    try:
        passage["cerveau"] = cerveau.enregistrer(base, registre_cerveau, maintenant)
    except Exception as e:
        passage["cerveau"] = {"erreur": f"{type(e).__name__} : {e}"[:300]}
        print("Cerveau : ERREUR", traceback.format_exc()[-1500:], file=sys.stderr)

    # règlement : corrections manuelles d'abord, puis Claude pour les boosts terminés
    if not (dossier / "reglements_manuels.json").exists():
        stockage.ecrire(dossier / "reglements_manuels.json", {})
    manuels = stockage.charger(dossier / "reglements_manuels.json")
    passage["reglements_manuels"] = reglement.appliquer_manuels(base, manuels, maintenant)
    if reglement.fournisseur():
        try:
            passage["reglement"] = reglement.regler(base)
        except Exception as e:
            passage["reglement"] = {"erreur": f"{type(e).__name__} : {e}"[:300]}
        print("Règlement :", passage["reglement"])
    else:
        passage["reglement"] = "aucune clé d'IA (OPENAI_API_KEY ou ANTHROPIC_API_KEY) : pas de règlement automatique"

    # Résultats observés APRÈS la sélection ; prix et mises des sélections figés.
    registre_cerveau["bilan"] = cerveau.bilan(registre_cerveau, base)
    stockage.ecrire(dossier / "cerveau.json", registre_cerveau)

    bilans = simulation.strategies(base)
    stockage.ecrire(dossier / "bilan.json", bilans)
    (dossier / "BILAN.md").write_text(rapport.markdown(bilans, maintenant), encoding="utf-8")
    for k, b in bilans.items():
        g = b["global"]
        print(f"Stratégie {k} : {g['paris']} paris, {g['regles']} réglés, gain net {g['gain_net']} €, ROI {g['roi_pct']} %")

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
