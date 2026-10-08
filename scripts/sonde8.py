"""Sonde n° 8 : Unibet France par la zone ISP (sans restriction de domaine) + empreinte Chrome.

Sonde n° 7 : le Web Unlocker refuse unibet.fr (« classé jeux d'argent, bloqué par la politique
d'usage de Bright Data » sans vérification d'identité) ; une requête est passée quand même et a montré
que la page /sport/super-cotes-boostees contient les boosts en JSON, avec « (1,80 -> 2,10 / Mise max 25€) »,
et l'API interne /services-api/sportsbookdata/... On ne s'appuie pas sur ce passage accidentel.

Ici, par la zone ISP (autorisée pour tous les domaines) : la page et l'API interne répondent-elles,
ou DataDome bloque-t-il (403 + captcha-delivery) ?
"""
from __future__ import annotations

import json
from datetime import datetime, timezone

from sonde import OUT, ecrire_brut, masquer, proxy_francais
from sonde2 import sonde_chrome

URLS = {
    "page_boosts": "https://www.unibet.fr/sport/super-cotes-boostees",
    "api_topmarket": "https://www.unibet.fr/services-api/sportsbookdata/current/events/live/topmarket",
}


def main() -> None:
    OUT.mkdir(exist_ok=True)
    proxies, verif = proxy_francais()
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    for nom, url in URLS.items():
        res[nom] = sonde_chrome(f"unibet_{nom}", url, proxies, verif)
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume8.json").write_text(texte, encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    main()
