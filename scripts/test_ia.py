"""Vérifie la clé d'IA et le modèle sur un pari dont on connaît le résultat (finale de la Coupe du monde 2022,
Argentine 3-3 France, 4-2 aux TAB ; Messi a marqué 2 buts) : la réponse attendue est « gagné »."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from boosts import reglement  # noqa: E402

PARI = {"id": "test", "bookmaker": "Winamax", "sport": "Football", "match": "Argentine - France",
        "pari": "Lionel Messi buteur et plus de 4,5 buts dans le match", "debut": "2022-12-18T15:00:00+00:00"}

fourn = reglement.fournisseur()
if not fourn:
    sys.exit("Aucune clé d'IA")
verdict, usage = reglement.demander(fourn, reglement.client_ia(fourn), PARI)
print(json.dumps({"fournisseur": fourn, "usage": usage, "verdict": verdict}, ensure_ascii=False, indent=1))
sys.exit(0 if verdict["statut"] == "gagné" else 1)
