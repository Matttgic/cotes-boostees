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
TOUT = os.environ.get("SONDE_FICHIER", "") == "tout"      # garder toutes les réponses JSON
DIRECT = os.environ.get("SONDE_FICHIER", "") == "direct"      # champ « fichier » du workflow réutilisé
Q = "lid=4&zid=0&cid=70&cgid=1&ctid=70"
API = [f"/matchmarketscontentapi/betboost?{Q}&pd=%23AC%23B1%23C1%23D1002%23G98%23",
       f"/matchmarketscontentapi/betboost?{Q}&pd=%23AC%23B1%23D1002%23G98%23",
       f"/matchmarketscontentapi/popularboostcompetitions?{Q}&pd=%23AC%23B1%23D1002%23K%5E5%23",
       f"/othersportsmatchbettingcontentapi/betboost?{Q}&pd=%23AC%23B13%23D1002%23",
       f"/splashcontentapi/betboostpoll?{Q}&pd=%23AS%23B1%23",
       f"/splashcontentapi/betboostpoll?{Q}&pd=%23AS%23B13%23"]


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
        if texte and (re.search(r"boost", texte, re.I) or (TOUT and ("json" in (r.headers.get("content-type") or "")
                                                                         or "/services/" in r.url or "/api/" in r.url)))\
                and len(reponses) < 1500:
            with gzip.open(BRUT / f"web_rep_{len(reponses)}.txt.gz", "wt", encoding="utf-8") as f:
                f.write(r.url + "\n\n" + texte)

    with sync_playwright() as p:
        nav = p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        # certains sites (Betsson) refusent les IP du proxy que leur base situe hors de France :
        # on change d'IP jusqu'à passer le filtre (6 essais)
        for essai in range(6):
            ctx = nav.new_context(proxy=None if DIRECT else proxy_playwright(), ignore_https_errors=True,
                                  locale="fr-FR", timezone_id="Europe/Paris", viewport={"width": 1366, "height": 900},
                                  user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                             "like Gecko) Chrome/141.0.0.0 Safari/537.36")
            ctx.route("**/*", lambda route: route.abort() if route.request.resource_type in ("image", "media", "font")
                      else route.continue_())
            page = ctx.new_page()
            r0 = page.goto(URLS[0], wait_until="domcontentloaded", timeout=90000)
            if r0 is not None and r0.status != 403 and "geoloc" not in page.title().lower():
                break
            ctx.close()
        res["essais_ip"] = essai + 1
        page.on("response", noter)
        trames: list[str] = []
        res["websockets"] = []

        def ws_ouvert(ws):
            res["websockets"].append(ws.url[:300])
            ws.on("framereceived", lambda f: trames.append(ws.url[:120] + " <<< " + (f if isinstance(f, str) else
                                                                                      f.decode("utf-8", "replace"))))
            ws.on("framesent", lambda f: trames.append(ws.url[:120] + " >>> " + (f if isinstance(f, str) else
                                                                                    f.decode("utf-8", "replace"))))
        page.on("websocket", ws_ouvert)
        # requêtes envoyées (méthode, corps) vers les API, pour pouvoir les rejouer
        envoyees: list[dict] = []
        page.on("request", lambda rq: envoyees.append({"url": rq.url[:400], "methode": rq.method,
                                                         "corps": (rq.post_data or "")[:3000],
                                                         "entetes": {k: v for k, v in rq.headers.items()
                                                                     if k.lower() not in ("cookie", "authorization")}})
                if "api" in rq.url or "services" in rq.url else None)
        for i, url in enumerate(URLS):
            info = {"url": url}
            try:
                page.goto(url, wait_until="domcontentloaded", timeout=90000)
                page.wait_for_timeout(15000)
                texte = page.inner_text("body")
                info.update({"titre": page.title(), "texte_octets": len(texte),
                             "lignes_boost": [l for l in texte.splitlines() if re.search(r"boost", l, re.I)][:40]})
                with gzip.open(BRUT / f"web_page_{i}.txt.gz", "wt", encoding="utf-8") as f:
                    f.write(texte)
                with gzip.open(BRUT / f"web_page_{i}.html.gz", "wt", encoding="utf-8") as f:
                    f.write(page.content())
                page.screenshot(path=str(BRUT / f"web_page_{i}.png"))
            except Exception as e:  # noqa: BLE001
                info["erreur"] = f"{type(e).__name__} : {e}"[:400]
            res["pages"].append(info)
        res["routage_boost"] = [r for r in reponses if "routingdata" in r["url"]][:1]
        res["api"] = []
        for chemin in ([] if "bet365" not in URLS[0] else API):
            try:
                r = page.evaluate("""async (u) => { const r = await fetch(u, {credentials: 'include'});
                                     return {s: r.status, t: await r.text()}; }""", chemin)
                with gzip.open(BRUT / f"web_api_{len(res['api'])}.txt.gz", "wt", encoding="utf-8") as f:
                    f.write(chemin + "\n\n" + r["t"])
                res["api"].append({"chemin": chemin, "statut": r["s"], "octets": len(r["t"]), "debut": r["t"][:500]})
            except Exception as e:  # noqa: BLE001
                res["api"].append({"chemin": chemin, "erreur": f"{type(e).__name__} : {e}"[:300]})
        nav.close()
        with gzip.open(BRUT / "web_trames.txt.gz", "wt", encoding="utf-8") as f:
            f.write("\n\n".join(trames))
        with gzip.open(BRUT / "web_requetes.json.gz", "wt", encoding="utf-8") as f:
            f.write(json.dumps(envoyees, ensure_ascii=False, indent=1))
        res["trames"] = len(trames)
        res["trames_boost"] = [t[:600] for t in trames if re.search(r"boost|max 20", t, re.I)][:10]
    res["octets_recus"] = octets
    res["direct"] = DIRECT
    res["reponses"] = sorted(reponses, key=lambda r: -r["boost"])[:60]
    res["hotes"] = sorted({re.sub(r"^https?://([^/]+).*", r"\1", r["url"]) for r in reponses})
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume12.json").write_text(texte, encoding="utf-8")
    print(texte[:5000])


if __name__ == "__main__":
    main()
