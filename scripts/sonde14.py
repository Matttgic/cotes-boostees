"""Sonde n° 14 : logos (icônes officielles) des bookmakers suivis, pour le site.

Pour chaque bookmaker, première adresse candidate qui renvoie une image ; enregistrée telle quelle dans
sonde/logos/<cle>.<ext>. IP française du proxy (nouvelle IP si refus, pour Betsson)."""
from __future__ import annotations

import json
from datetime import datetime, timezone

from curl_cffi import requests as creq

from sonde import OUT, masquer, proxy_francais

CANDIDATS = {
    "winamax": ["https://operator-front-static-cdn.winamax.fr/img/style/v2/202410-apple-touch-icon.png",
                "https://operator-front-static-cdn.winamax.fr/img/content/poker/2022/20220412_logo_winamax/Favicon_v2.png"],
    "unibet": ["https://www.unibet.fr/apple-touch-icon.png", "https://www.unibet.fr/favicon.png",
               "https://www.unibet.fr/favicon.ico"],
    "olybet": ["https://www.olybet.fr/icon/apple-touch-icon-180x180.png", "https://www.olybet.fr/icon/favicon-32x32.png"],
    "genybet": ["https://sport.genybet.fr/img/3_genybet/apple-touch-icon.png",
                "https://sport.genybet.fr/img/3_genybet/favicon.ico"],
    "netbet": ["https://www.netbet.fr/img/3_netbet/apple-touch-icon.png", "https://www.netbet.fr/img/3_netbet/favicon.ico"],
    "betsson": ["https://www.betsson.fr/icons/favicon-128x128.png", "https://www.betsson.fr/icons/favicon-96x96.png"],
}
EXT = {"image/png": "png", "image/x-icon": "ico", "image/vnd.microsoft.icon": "ico", "image/svg+xml": "svg",
       "image/jpeg": "jpg", "image/webp": "webp"}


def main() -> None:
    dossier = OUT / "logos"
    dossier.mkdir(parents=True, exist_ok=True)
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "logos": {}}
    for cle, urls in CANDIDATS.items():
        essais = []
        for url in urls:
            for _ in range(4):                       # nouvelle IP si le site refuse celle-ci
                proxies, verif = proxy_francais()
                try:
                    r = creq.get(url, impersonate="chrome", proxies=proxies, verify=verif, timeout=40)
                except Exception as e:  # noqa: BLE001
                    essais.append(f"{url} : {type(e).__name__}")
                    continue
                type_ = (r.headers.get("content-type") or "").split(";")[0].strip().lower()
                essais.append(f"{url} : {r.status_code} {type_} {len(r.content)}")
                if r.status_code == 200 and type_ in EXT:
                    (dossier / f"{cle}.{EXT[type_]}").write_bytes(r.content)
                    res["logos"][cle] = {"url": url, "type": type_, "octets": len(r.content)}
                    break
                if r.status_code != 403:
                    break
            if cle in res["logos"]:
                break
        if cle not in res["logos"]:
            res["logos"][cle] = {"echec": essais}
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume14.json").write_text(texte, encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    main()
