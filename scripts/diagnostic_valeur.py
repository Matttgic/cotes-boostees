"""Diagnostic : pourquoi des boosts à venir restent « non évaluables » ?

Lit boosts.json (branche donnees, dépôt public), recharge Pinnacle pour les sports concernés et, pour chaque
boost à venir non évaluable, enregistre :
- les matchs Pinnacle candidats (même sport, fenêtre horaire) avec leur ressemblance de noms ;
- pour le meilleur candidat, la liste des marchés disponibles (marché, période, lignes).
Résultat : sonde/diagnostic_valeur.json (branche `sonde`). Aucun secret nécessaire.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from boosts import pinnacle, valeur  # noqa: E402
from boosts.correspondance import ressemblance  # noqa: E402

DONNEES = "https://raw.githubusercontent.com/Matttgic/cotes-boostees/donnees/boosts.json"
OUT = Path("sonde")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    base = requests.get(DONNEES, timeout=60).json()
    t = datetime.now(timezone.utc)
    cibles = [b for b in base.values() if not b.get("long_terme") and b.get("jambes")
              and (valeur._t(b.get("debut")) or t) > t
              and (b.get("valeur_derniere") or {}).get("statut") in (None, "non_evaluable")]
    sports = {valeur.sport_commun(b.get("sport")) for b in cibles} - {None}
    ids = {sid: s for sid, s in pinnacle.SPORTS.items() if s in sports}
    lignes = pinnacle.collecter(ids) if ids else []
    index = valeur.Index(lignes)
    # forme des marchés de résultat par sport (2 ou 3 issues)
    formes = defaultdict(lambda: defaultdict(int))
    for l in lignes:
        if l["marche"] in ("RESULTAT_1N2", "VAINQUEUR") and l["periode"] in ("MATCH", "TEMPS_REG"):
            formes[l["sport"]][f"{l['marche']}/{l['periode']}"] += 1
    res = {"date_utc": t.isoformat(timespec="seconds"), "boosts_cibles": len(cibles),
           "lignes_pinnacle": len(lignes), "formes_resultat": {k: dict(v) for k, v in formes.items()},
           "ligues_pinnacle": {}, "boosts": []}
    ligues = defaultdict(set)
    for l in lignes:
        ligues[l["sport"]].add(l.get("ligue"))
    res["ligues_pinnacle"] = {k: sorted(x for x in v if x)[:200] for k, v in ligues.items()}
    for b in cibles:
        sport = valeur.sport_commun(b.get("sport"))
        debut = valeur._t(b.get("debut"))
        diag = {"id": b["id"], "sport": b.get("sport"), "match": b.get("match"), "pari": b.get("pari"),
                "debut": b.get("debut"), "raison": (b.get("valeur_derniere") or {}).get("raison"),
                "jambes": b["jambes"], "candidats": []}
        for j in b["jambes"]:
            cands = []
            for m in index.matchs.values():
                if m["sport"] != sport or not m["debut"] or not debut:
                    continue
                if not (debut - timedelta(hours=3) <= m["debut"] <= debut + timedelta(hours=30)):
                    continue
                s = max(min(ressemblance(j["equipe_1"], m["domicile"]), ressemblance(j["equipe_2"], m["exterieur"])),
                        min(ressemblance(j["equipe_1"], m["exterieur"]), ressemblance(j["equipe_2"], m["domicile"])))
                cands.append((round(s, 2), m))
            cands.sort(key=lambda x: -x[0])
            top = []
            for s, m in cands[:3]:
                marches = defaultdict(set)
                for l in index.lignes.get(m["match_id"], []):
                    marches[f"{l['marche']}|{l['periode']}"].add(l.get("ligne") if l.get("joueur") is None
                                                                 else f"{l.get('joueur')}:{l.get('ligne')}")
                top.append({"ressemblance": s, "match": f"{m['domicile']} - {m['exterieur']}",
                            "debut": m["debut"].isoformat(),
                            "marches": {k: sorted(map(str, v))[:40] for k, v in sorted(marches.items())}})
            diag["candidats"].append({"jambe": f"{j['equipe_1']} - {j['equipe_2']} / {j['type']}", "top": top})
        res["boosts"].append(diag)
    (OUT / "diagnostic_valeur.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("date_utc", "boosts_cibles", "lignes_pinnacle", "formes_resultat")},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
