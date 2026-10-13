"""Analyse reproductible sans réseau et sans dépendance statistique supplémentaire."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from boosts.recherche_strategies import analyser, markdown, resume


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--historique", default="analyses/historique-strategies.json")
    parser.add_argument("--sortie", default="analyses")
    args = parser.parse_args()
    h = json.loads(Path(args.historique).read_text(encoding="utf-8"))
    r = analyser(h)
    dest = Path(args.sortie)
    dest.mkdir(parents=True, exist_ok=True)
    (dest / "RECHERCHE.md").write_text(markdown(r), encoding="utf-8")
    strategies = {}
    for key, b in r["strategies"].items():
        strategies[key] = {**b, "replay": {k: v for k, v in b["replay"].items() if k != "decisions"}}
    (dest / "recherche-initiale.json").write_text(json.dumps(
        {"strategies": strategies, "recherche": resume(r)}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Rapport et snapshot générés dans {dest}")
    for key, b in r["strategies"].items():
        print(key, b["global"])


if __name__ == "__main__":
    main()
