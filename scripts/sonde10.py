"""Sonde n° 10 : OlyBoosts d'OlyBet (plateforme BetConstruct, API « swarm » en WebSocket).

OlyBet.fr affiche son offre sport dans sports.olybet.fr (Spring Builder de BetConstruct) :
partnerId 18769041, swarm wss://eu-swarm-reverse.betconstruct.com, compétition « OlyBoosts » 18265893.
On lit toute la compétition (matchs, marchés, sélections) pour voir si la cote d'origine et le plafond
sont exposés. Essai direct puis par le proxy français.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timezone

from curl_cffi.requests import Session

from sonde import OUT, ecrire_brut, masquer, proxy_francais

SWARM = os.environ.get("SONDE_URL") or "wss://eu-swarm-reverse.betconstruct.com/"
SITE_ID = 18769041
COMPETITION = 18265893


def echange(ws, rid: str, commande: str, params: dict) -> dict:
    ws.send_str(json.dumps({"command": commande, "params": params, "rid": rid}))
    while True:
        m = json.loads(ws.recv_str())
        if m.get("rid") == rid:
            return m


def lire(proxies=None, verif=True) -> dict:
    s = Session(impersonate="chrome", proxies=proxies, verify=verif)
    ws = s.ws_connect(SWARM, headers={"Origin": "https://sports.olybet.fr"}, timeout=60)
    out = {"session": echange(ws, "1", "request_session",
                              {"site_id": SITE_ID, "language": "fra", "source": 42})}
    out["olyboosts"] = echange(ws, "2", "get", {
        "source": "betting",
        "what": {"sport": [], "region": [], "competition": [], "game": [], "market": [], "event": []},
        "where": {"competition": {"id": COMPETITION}}, "subscribe": False})
    # compétitions dont le nom évoque un boost (au cas où l'identifiant change)
    out["competitions"] = echange(ws, "3", "get", {
        "source": "betting", "what": {"sport": ["id", "name"], "competition": ["id", "name"]},
        "where": {}, "subscribe": False})
    ws.close()
    return out


def main() -> None:
    OUT.mkdir(exist_ok=True)
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    for mode in ("direct", "proxy"):
        try:
            data = lire() if mode == "direct" else lire(*proxy_francais())
        except Exception as e:  # noqa: BLE001
            res[mode] = f"{type(e).__name__} : {e}"[:400]
            continue
        ecrire_brut(f"olybet_swarm_{mode}", data)
        o = json.dumps(data.get("olyboosts"), ensure_ascii=False)
        noms = [c.get("name") for sp in ((data.get("competitions") or {}).get("data") or {}).get("data", {})
                .get("sport", {}).values() for c in (sp.get("competition") or {}).values()]
        res[mode] = {"session": (data["session"].get("code"), bool((data["session"].get("data") or {}).get("sid"))),
                     "octets_olyboosts": len(o), "jeux": o.count('"game"'),
                     "competitions_boost": [n for n in noms if n and "boost" in n.lower()][:20]}
        break
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume10.json").write_text(texte, encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    main()
