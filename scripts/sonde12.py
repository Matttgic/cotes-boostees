"""Sonde n° 12 : bet365.fr dans un vrai Chromium (Playwright) par le proxy français.

bet365 est une application JavaScript : la page d'accueil seule ne contient aucune cote. On charge le site,
on note toutes les réponses réseau (adresse, taille, extrait) et le texte visible, puis on cherche les
« boosts » (cotes boostées / Super Boost). Adresses : SONDE_URL (défaut : accueil). Sorties : resume12.json
et brut/bet365_*.
"""
from __future__ import annotations

import gzip
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

from sonde import BRUT, OUT, masquer

URLS = (os.environ.get("SONDE_URL") or "https://www.bet365.fr/#/HO/").split()


def proxy_playwright() -> dict | None:
    client = os.environ.get("BRIGHTDATA_CUSTOMER_ID", "").strip().removeprefix("brd-customer-")
    zone = os.environ.get("BRIGHTDATA_ZONE", "").strip()
    mdp = os.environ.get("BRIGHTDATA_PASSWORD", "").strip()
    if not (client and zone and mdp):
        return None
    port = os.environ.get("BRIGHTDATA_PORT", "").strip() or "44445"
    return {"server": f"http://brd.superproxy.io:{port}",
            "username": f"brd-customer-{client}-zone-{zone}-country-fr-session-{os.urandom(4).hex()}",
            "password": mdp}


def main() -> None:
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "playwright"], check=True)
    subprocess.run([sys.executable, "-m", "playwright", "install", "--with-deps", "chromium"], check=True)
    from playwright.sync_api import sync_playwright

    OUT.mkdir(exist_ok=True)
    BRUT.mkdir(parents=True, exist_ok=True)
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "pages": []}
    reponses: list[dict] = []
    octets = 0

    def noter(r):
        nonlocal octets
        try:
            corps = r.body()
        except Exception:  # noqa: BLE001
            return
        octets += len(corps)
        texte = corps[:400000].decode("utf-8", "replace") if "image" not in (r.headers.get("content-type") or "") else ""
        reponses.append({"url": r.url[:300], "statut": r.status, "type": r.headers.get("content-type"),
                         "octets": len(corps), "boost": len(re.findall(r"boost", texte, re.I)), "debut": texte[:300]})
        if texte and re.search(r"boost", texte, re.I) and len(reponses) < 400:
            with gzip.open(BRUT / f"bet365_rep_{len(reponses)}.txt.gz", "wt", encoding="utf-8") as f:
                f.write(r.url + "\n\n" + texte)

    with sync_playwright() as p:
        nav = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        ctx = nav.new_context(proxy=proxy_playwright(), ignore_https_errors=True, locale="fr-FR",
                              timezone_id="Europe/Paris", viewport={"width": 1366, "height": 900},
                              user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like "
                                         "Gecko) Chrome/141.0.0.0 Safari/537.36")
        page = ctx.new_page()
        page.on("response", noter)
        for i, url in enumerate(URLS):
            info = {"url": url}
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=90000)
                page.wait_for_timeout(15000)
                texte = page.inner_text("body")
                info.update({"titre": page.title(), "texte_octets": len(texte),
                             "lignes_boost": [l for l in texte.splitlines() if re.search(r"boost", l, re.I)][:40]})
                with gzip.open(BRUT / f"bet365_page_{i}.txt.gz", "wt", encoding="utf-8") as f:
                    f.write(texte)
                with gzip.open(BRUT / f"bet365_page_{i}.html.gz", "wt", encoding="utf-8") as f:
                    f.write(page.content())
                page.screenshot(path=str(BRUT / f"bet365_page_{i}.png"))
            except Exception as e:  # noqa: BLE001
                info["erreur"] = f"{type(e).__name__} : {e}"[:400]
            res["pages"].append(info)
        nav.close()
    res["octets_recus"] = octets
    res["reponses"] = sorted(reponses, key=lambda r: -r["boost"])[:60]
    res["hotes"] = sorted({re.sub(r"^https?://([^/]+).*", r"\1", r["url"]) for r in reponses})
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume12.json").write_text(texte, encoding="utf-8")
    print(texte[:5000])


if __name__ == "__main__":
    main()
