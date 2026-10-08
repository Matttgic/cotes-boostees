"""Sonde n° 9 : page complète des cotes boostées Unibet (zone ISP + empreinte Chrome), pour écrire le
parseur. La page est rendue côté serveur (Angular) avec son état JSON embarqué."""
from __future__ import annotations

import gzip
import json
from datetime import datetime, timezone

from curl_cffi import requests as creq

from sonde import BRUT, OUT, masquer, proxy_francais

URL = __import__("os").environ.get("SONDE_URL") or "https://www.unibet.fr/cotes-boostees"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    BRUT.mkdir(parents=True, exist_ok=True)
    proxies, verif = proxy_francais()
    r = creq.get(URL, impersonate="chrome", proxies=proxies, verify=verif, timeout=60,
                 headers={"Accept-Language": "fr-FR,fr;q=0.9"})
    with gzip.open(BRUT / (__import__("os").environ.get("SONDE_FICHIER") or "unibet_page_complete.html.gz"), "wt", encoding="utf-8") as f:
        f.write(r.text)
    res = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "statut": r.status_code,
           "octets": len(r.content), "mise_max": r.text.count("Mise max")}
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume9.json").write_text(texte, encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    main()
