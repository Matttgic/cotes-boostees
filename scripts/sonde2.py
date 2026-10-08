"""Sonde n° 2 : comment lire les boosts une fois passé par une IP française ?

Résultat de la sonde n° 1 (8/10/2026, proxy ISP Bright Data, IP Paris) :
- PMU répond (200) : page Next.js vide, les données viennent d'API appelées par le navigateur ;
- Winamax : 403 de CloudFront (pare-feu) ;
- Unibet : 403 de DataDome (anti-robot avec défi JavaScript).

Ici :
  1. PMU : on lit la config (conf.js) et les scripts de la page pour trouver les adresses d'API
     et tout ce qui parle de boost / SuperCote ;
  2. Winamax et Unibet : nouvel essai avec l'empreinte réseau d'un vrai Chrome (curl_cffi),
     souvent suffisant contre un pare-feu qui filtre les robots Python.

Sorties dans sonde/ (resume2.json + brut/), secrets masqués.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from urllib.parse import urljoin

import requests
from curl_cffi import requests as creq

from sonde import NAVIGATEUR, OUT, ecrire_brut, erreur_proxy, masquer, proxy_francais

MOTS = re.compile(r"boost|super ?cote|supercote|cotes?[-_ ]boost", re.I)
URL_API = re.compile(r"https?://[a-z0-9.-]+\.(?:pmu\.fr|pmu\.com|pmu-[a-z0-9-]+\.[a-z]+)[^\"'\s\\)]*", re.I)
MAX_SCRIPTS = 25


def contextes(texte: str, n: int = 12, largeur: int = 160) -> list[str]:
    return [texte[max(0, m.start() - largeur): m.end() + largeur] for m in MOTS.finditer(texte)][:n]


def sonde_pmu(proxies, verif) -> dict:
    s = requests.Session()
    s.headers.update(NAVIGATEUR)
    info: dict = {}
    page = s.get("https://www.pmu.fr/sport/", proxies=proxies, verify=verif, timeout=60)
    info["page"] = {"statut": page.status_code, "octets": len(page.text)}
    scripts = re.findall(r'src="([^"]+\.js[^"]*)"', page.text)
    info["scripts_trouves"] = len(scripts)
    hotes, traces, lus = set(), {}, 0
    # conf.js d'abord (adresses des API), puis les scripts de l'app
    scripts.sort(key=lambda u: (0 if "conf.js" in u else 1 if ("_app" in u or "sport" in u) else 2))
    for src in scripts[:MAX_SCRIPTS]:
        url = urljoin("https://www.pmu.fr/", src)
        try:
            r = s.get(url, proxies=proxies, verify=verif, timeout=60)
        except requests.RequestException as e:
            traces[src] = [f"erreur : {e!r}"[:200]]
            continue
        lus += len(r.content)
        hotes.update(u.split("?")[0][:150] for u in URL_API.findall(r.text))
        c = contextes(r.text)
        if c:
            traces[src.split("/")[-1][:80]] = c
        if "conf.js" in src:
            ecrire_brut("pmu_conf", r.text[:200000])
    info["octets_scripts"] = lus
    info["adresses_api"] = sorted(hotes)[:80]
    info["traces_boost"] = traces
    ecrire_brut("pmu_scripts", info)
    return info


def sonde_chrome(nom: str, url: str, proxies, verif) -> dict:
    """Même page, mais avec l'empreinte TLS/HTTP2 de Chrome."""
    try:
        r = creq.get(url, impersonate="chrome", proxies=proxies, verify=verif, timeout=60,
                     headers={"Accept-Language": "fr-FR,fr;q=0.9"})
    except Exception as e:
        return {"erreur": masquer(repr(e))[:300]}
    html = r.text
    info = {
        "statut": r.status_code,
        "serveur": r.headers.get("server"),
        "datadome": r.headers.get("x-datadome"),
        "erreur_proxy": erreur_proxy(r) if hasattr(r, "headers") else None,
        "octets": len(html),
        "preloaded_state": "PRELOADED_STATE" in html,
        "occurrences_boost": len(MOTS.findall(html)),
    }
    ecrire_brut(f"chrome_{nom}", {"statut": r.status_code, "entetes": dict(r.headers),
                                  "debut": html[:3000], "boost": contextes(html)})
    return info


def main() -> None:
    OUT.mkdir(exist_ok=True)
    proxies, verif = proxy_francais()
    if not proxies:
        raise SystemExit("Secrets Bright Data absents : cette sonde n'a de sens que via l'IP française.")
    resume: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    try:
        resume["pmu"] = sonde_pmu(proxies, verif)
    except Exception as e:
        resume["pmu"] = {"erreur": masquer(repr(e))[:300]}
    resume["winamax_chrome"] = sonde_chrome("winamax", "https://www.winamax.fr/paris-sportifs", proxies, verif)
    resume["unibet_chrome"] = sonde_chrome("unibet", "https://www.unibet.fr/sport", proxies, verif)
    texte = masquer(json.dumps(resume, ensure_ascii=False, indent=2))
    (OUT / "resume2.json").write_text(texte, encoding="utf-8")
    print(texte[:60000])


if __name__ == "__main__":
    main()
