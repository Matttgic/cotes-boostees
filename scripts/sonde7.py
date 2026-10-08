"""Sonde n° 7 : Unibet France via le Web Unlocker de Bright Data.

unibet.fr est protégé par DataDome (défi JavaScript) : 403 même depuis une IP française avec
l'empreinte de Chrome. Le Web Unlocker résout ce défi côté Bright Data et renvoie la page.
Sur la page « Cotes boostées » de l'appli, chaque intitulé contient cote d'origine, cote boostée
et mise max : « Montauban gagne et Johnny Matthews marque au moins 1 essai (2,50 -> 2,75 / Mise max 25 €) ».

Ici : quelques adresses candidates, et pour chacune : statut, taille, traces « Mise max » / « -> »,
adresses d'API internes repérées dans la page.
Secrets : BRIGHTDATA_API_KEY (clé du compte) et BRIGHTDATA_UNLOCKER_ZONE (nom de la zone Web Unlocker).
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone

import requests

from sonde import OUT, ecrire_brut

API = "https://api.brightdata.com/request"
CANDIDATES = {
    "accueil_sport": "https://www.unibet.fr/sport",
    "cotes_boostees": "https://www.unibet.fr/sport/cotes-boostees",
    "super_cotes": "https://www.unibet.fr/sport/super-cotes-boostees",
}
MISE = re.compile(r"mise\s*max", re.I)
FLECHE = re.compile(r"\d+[.,]\d+\s*(?:->|→|&gt;)\s*\d+[.,]\d+")


def masquer(t: str) -> str:
    k = os.environ.get("BRIGHTDATA_API_KEY", "").strip()
    return t.replace(k, "***") if len(k) >= 6 else t


def debloquer(url: str) -> requests.Response:
    return requests.post(API, timeout=120,
                         headers={"Authorization": f"Bearer {os.environ['BRIGHTDATA_API_KEY'].strip()}"},
                         json={"zone": os.environ["BRIGHTDATA_UNLOCKER_ZONE"].strip(), "url": url,
                               "format": "raw", "country": "fr"})


def main() -> None:
    OUT.mkdir(exist_ok=True)
    if not os.environ.get("BRIGHTDATA_API_KEY") or not os.environ.get("BRIGHTDATA_UNLOCKER_ZONE"):
        raise SystemExit("Secrets BRIGHTDATA_API_KEY et BRIGHTDATA_UNLOCKER_ZONE requis.")
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    for nom, url in CANDIDATES.items():
        try:
            r = debloquer(url)
        except requests.RequestException as e:
            res[nom] = {"erreur": masquer(repr(e))[:300]}
            continue
        t = r.text
        res[nom] = {
            "statut": r.status_code, "octets": len(t),
            "erreur_brightdata": r.headers.get("x-brd-error") or r.headers.get("x-brd-err-code"),
            "datadome": "captcha-delivery" in t or "datadome" in t.lower()[:5000],
            "mise_max": len(MISE.findall(t)), "fleches_de_cote": len(FLECHE.findall(t)),
            "exemples": [t[max(0, m.start() - 200): m.end() + 120] for m in MISE.finditer(t)][:5],
            "api_internes": sorted(set(re.findall(r"[\"'](/(?:zones|api|service|sport)[a-z0-9_/.-]{3,100}"
                                                   r"(?:\?[^\"'\s]{0,80})?)[\"']", t)))[:60],
            "titre": (re.search(r"<title>([^<]{0,120})", t) or [None, None])[1],
        }
        ecrire_brut(f"unibet_{nom}", {"debut": t[:5000], "fin": t[-3000:]})
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume7.json").write_text(texte, encoding="utf-8")
    print(texte[:60000])


if __name__ == "__main__":
    main()
