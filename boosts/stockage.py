"""Historique des boosts : un enregistrement par boost (clé `id`), jamais effacé.

À chaque passage :
- boost nouveau : on garde tout, plus `premiere_vue` et `cote_boostee_initiale` ;
- boost déjà connu : on met à jour `derniere_vue`, `nb_vues`, l'état et la cote du moment ;
  si la cote boostée change, l'ancienne valeur part dans `historique_cotes`.
Les champs ajoutés plus tard par d'autres étapes (règlement, cote juste…) ne sont jamais écrasés.
"""
from __future__ import annotations

import json
from pathlib import Path

CHAMPS_VIVANTS = ("cote_boostee", "cote_origine", "hausse_pct", "mise_max", "disponible", "debut", "match",
                  "pari", "sport", "type")


def charger(chemin: Path) -> dict[str, dict]:
    if not chemin.exists():
        return {}
    return json.loads(chemin.read_text(encoding="utf-8"))


def ecrire(chemin: Path, donnees) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    tmp = chemin.with_suffix(chemin.suffix + ".tmp")
    tmp.write_text(json.dumps(donnees, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    tmp.replace(chemin)


def fusionner(base: dict[str, dict], lus: list[dict], maintenant: str) -> tuple[int, int]:
    """Intègre les boosts lus. Renvoie (nouveaux, cotes modifiées)."""
    nouveaux = modifies = 0
    for b in lus:
        connu = base.get(b["id"])
        if connu is None:
            base[b["id"]] = {**b, "premiere_vue": maintenant, "derniere_vue": maintenant, "nb_vues": 1,
                             "cote_boostee_initiale": b["cote_boostee"], "historique_cotes": []}
            nouveaux += 1
            continue
        if b["cote_boostee"] != connu.get("cote_boostee"):
            connu.setdefault("historique_cotes", []).append(
                {"jusqu_a": maintenant, "cote_boostee": connu.get("cote_boostee")})
            modifies += 1
        for k in CHAMPS_VIVANTS:
            if b.get(k) is not None:
                connu[k] = b[k]
        connu["derniere_vue"] = maintenant
        connu["nb_vues"] = int(connu.get("nb_vues", 0)) + 1
    return nouveaux, modifies
