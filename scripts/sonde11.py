"""Sonde n° 11 : plusieurs adresses d'un coup (IP française + empreinte Chrome), pour repérer la plateforme
des sites français de Genybet, NetBet et bet365. SONDE_URL = adresses séparées par des espaces ou virgules
(défaut : accueils sport des trois). Chaque page brute va dans brut/<hôte>_<n>.html.gz."""
from __future__ import annotations

import gzip
import json
import os
import re
from datetime import datetime, timezone
from urllib.parse import urlparse

from curl_cffi import requests as creq

from sonde import BRUT, OUT, masquer, proxy_francais

DEFAUT = ("https://www.genybet.fr/ https://sport.genybet.fr/ https://www.netbet.fr/ "
          "https://www.netbet.fr/paris-sportifs https://www.bet365.fr/ https://www.bet365.fr/#/HO/")
INDICES = ("betconstruct", "swarm", "altenar", "sportnco", "kambi", "sbtech", "openbet", "betradar", "sportradar",
           "digitain", "playtech", "gan", "boost", "partner_id", "partnerid", "site_id", "integration", "api")


def main() -> None:
    OUT.mkdir(exist_ok=True)
    BRUT.mkdir(parents=True, exist_ok=True)
    # SONDE_FICHIER = « sessions=N » : refaire la liste avec N adresses IP différentes du proxy
    n = int((os.environ.get("SONDE_FICHIER") or "").removeprefix("sessions=") or 1) \
        if (os.environ.get("SONDE_FICHIER") or "").startswith("sessions=") else 1
    urls = [u for u in re.split(r"[\s,]+", os.environ.get("SONDE_URL") or DEFAUT) if u] * n
    sessions = [proxy_francais() for _ in range(n)]
    proxies, verif = sessions[0]
    res = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "pages": []}
    par_session = len(urls) // n
    for i, url in enumerate(urls):
        proxies, verif = sessions[i // par_session]
        try:
            r = creq.get(url, impersonate="chrome", proxies=proxies, verify=verif, timeout=60,
                         headers={"Accept-Language": "fr-FR,fr;q=0.9"})
        except Exception as e:  # noqa: BLE001
            res["pages"].append({"url": url, "erreur": f"{type(e).__name__} : {e}"[:300]})
            continue
        nom = f"{urlparse(url).hostname}_{i}.html.gz"
        with gzip.open(BRUT / nom, "wt", encoding="utf-8") as f:
            f.write(r.text)
        bas = r.text.lower()
        hotes = sorted(set(re.findall(r"https?://([a-z0-9.-]+\.[a-z]{2,})", bas)))
        res["pages"].append({"url": url, "final": str(r.url), "statut": r.status_code, "octets": len(r.content),
                             "fichier": nom, "titre": (re.search(r"<title[^>]*>(.*?)</title>", r.text, re.S | re.I)
                                                       or [None, ""])[1].strip()[:120],
                             "indices": {k: bas.count(k) for k in INDICES if k in bas},
                             "hotes": hotes[:80]})
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume11.json").write_text(texte, encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    main()
