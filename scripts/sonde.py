"""Sonde : où trouver les cotes boostées de Winamax, Unibet et PMU ?

Deux questions, une seule exécution (dans GitHub Actions) :
  A. PulseScore expose-t-il les boosts ? On lit les grands championnats chez chaque bookmaker
     et on cherche des marchés ou sélections dont l'intitulé évoque un boost.
  B. Les sites des bookmakers répondent-ils depuis les serveurs GitHub (blocage hors France) ?
     On lit la page d'accueil paris sportifs et on cherche les traces des boosts dans le code reçu.

Budget PulseScore : une vingtaine de requêtes au plus.
Sorties dans sonde/ : resume.json (synthèse) et brut/ (extraits utiles, jamais la clé).

Usage : PULSESCORE_KEY=... python scripts/sonde.py
"""
from __future__ import annotations

import gzip
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import quote

import requests

PS = "https://api.pulsescore.net/api"
BOOKMAKERS = ["winamax", "unibet-fr", "pmu"]
# championnats où les boosts du jour ont le plus de chances d'être (comparaison sans accents ni casse)
LIGUES_CIBLES = ["ligue 1", "premier league", "liga", "serie a", "bundesliga", "champions",
                 "coupe du monde", "world cup", "nations", "amical", "friendl", "qualif"]
MAX_LIGUES = 4
MOTS_BOOST = re.compile(r"boost|super ?cote|cote ?\+|promo|sp[ée]cial|enhanced|odds ?boost", re.I)

SITES = {
    "winamax": "https://www.winamax.fr/paris-sportifs",
    "unibet": "https://www.unibet.fr/sport",
    "pmu": "https://parisportif.pmu.fr/",
}
NAVIGATEUR = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/128.0 Mobile Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9",
}

OUT = Path("sonde")
BRUT = OUT / "brut"


def masquer(texte: str) -> str:
    """Retire les secrets d'un texte (un message d'erreur peut contenir l'URL du proxy)."""
    for nom in ("BRIGHTDATA_PASSWORD", "PULSESCORE_KEY"):
        v = os.environ.get(nom, "").strip()
        if v:
            texte = texte.replace(v, "***").replace(quote(v, safe=""), "***")
    return texte


def ecrire_brut(nom: str, contenu) -> None:
    BRUT.mkdir(parents=True, exist_ok=True)
    with gzip.open(BRUT / f"{nom}.json.gz", "wt", encoding="utf-8") as f:
        f.write(masquer(json.dumps(contenu, ensure_ascii=False)))


def sans_accents(t: str) -> str:
    return (t.lower().replace("é", "e").replace("è", "e").replace("ê", "e")
            .replace("à", "a").replace("ç", "c"))


# --------------------------------------------------------------------------- A. PulseScore

def sonde_pulsescore(cle: str) -> dict:
    s = requests.Session()
    s.headers.update({"X-Secret": cle, "Accept": "application/json", "Accept-Encoding": "gzip"})
    requetes = 0

    def get(chemin: str, params: dict | None = None):
        nonlocal requetes
        requetes += 1
        try:
            r = s.get(f"{PS}/{chemin}", params=params, timeout=90)
        except requests.RequestException as e:
            return None, f"erreur réseau : {e!r}"[:200]
        finally:
            time.sleep(1.2)
        if r.status_code != 200:
            return None, f"HTTP {r.status_code}"
        try:
            return r.json(), None
        except ValueError:
            return None, "JSON invalide"

    res = {}
    for bm in BOOKMAKERS:
        info = {"ligues_lues": [], "marches_vus": 0, "selections_vues": 0, "traces_boost": [], "erreurs": []}
        ligues, err = get(f"{bm}/soccer/leagues", {"page": 1, "limit": 100})
        if err:
            info["erreurs"].append(f"ligues : {err}")
            res[bm] = info
            continue
        liste = ligues.get("leagues") if isinstance(ligues, dict) else ligues
        noms = []
        for l in liste or []:
            nom = l.get("name") or l.get("league") if isinstance(l, dict) else l
            if isinstance(nom, str):
                noms.append(nom)
        info["nb_ligues"] = len(noms)
        info["ligues_boost_dans_le_nom"] = [n for n in noms if MOTS_BOOST.search(n)]
        choisies = [n for n in noms if any(c in sans_accents(n) for c in LIGUES_CIBLES)][:MAX_LIGUES]
        for ligue in choisies:
            d, err = get(f"{bm}/soccer/leagues/{quote(ligue, safe='')}/events")
            if err:
                info["erreurs"].append(f"{ligue} : {err}")
                continue
            evs = d.get("events") if isinstance(d, dict) else d
            info["ligues_lues"].append({"ligue": ligue, "matchs": len(evs or [])})
            for e in evs or []:
                for m in e.get("markets") or []:
                    info["marches_vus"] += 1
                    nom_m = m.get("rawName") or ""
                    if MOTS_BOOST.search(nom_m):
                        info["traces_boost"].append({"match": f"{e.get('home')} - {e.get('away')}",
                                                     "marche": nom_m, "selections": m.get("selections")})
                    for sel in m.get("selections") or []:
                        info["selections_vues"] += 1
                        if MOTS_BOOST.search(sel.get("rawName") or ""):
                            info["traces_boost"].append({"match": f"{e.get('home')} - {e.get('away')}",
                                                         "marche": nom_m, "selection": sel})
        ecrire_brut(f"pulsescore_{bm}_ligues", liste if isinstance(liste, list) else ligues)
        info["traces_boost"] = info["traces_boost"][:30]
        res[bm] = info
    res["_requetes"] = requetes
    return res


# --------------------------------------------------------------------------- B. sites directs

CA_BRIGHTDATA = Path(__file__).resolve().parent.parent / "certs" / "brightdata_proxy_ca.crt"


def proxy_francais() -> tuple[dict | None, str | bool]:
    """Proxy Bright Data sortant en France si les secrets sont là, sinon accès direct.
    Renvoie (proxies pour requests, vérification TLS)."""
    client = os.environ.get("BRIGHTDATA_CUSTOMER_ID", "").strip()
    zone = os.environ.get("BRIGHTDATA_ZONE", "").strip()
    mdp = os.environ.get("BRIGHTDATA_PASSWORD", "").strip()
    if not (client and zone and mdp):
        return None, True
    client = client.removeprefix("brd-customer-")
    session = os.urandom(4).hex()          # même IP pour toute la sonde
    url = (f"http://brd-customer-{client}-zone-{zone}-country-fr-session-{session}:"
           f"{quote(mdp, safe='')}@brd.superproxy.io:33335")
    return {"http": url, "https": url}, bundle_certificats()


def bundle_certificats() -> str:
    """Certificats publics + celui de Bright Data : valable que la zone intercepte le TLS
    (résidentiel) ou non (ISP, datacenter)."""
    import certifi
    chemin = Path(os.environ.get("RUNNER_TEMP", "/tmp")) / "ca_bundle_sonde.pem"
    chemin.write_text(Path(certifi.where()).read_text() + "\n" + CA_BRIGHTDATA.read_text())
    return str(chemin)


def erreur_proxy(r: requests.Response) -> str | None:
    """Code d'erreur Bright Data éventuel (ancien et nouvel en-tête)."""
    return r.headers.get("x-brd-err-code") or r.headers.get("x-brd-error") or r.headers.get("Proxy-Status")


def sonde_sites() -> dict:
    proxies, verif = proxy_francais()
    res: dict = {"_acces": "proxy Bright Data (France)" if proxies else "direct (serveur GitHub)"}
    try:
        if proxies:
            g = requests.get("https://geo.brdtest.com/mygeo.json", proxies=proxies, verify=verif, timeout=40)
            j = g.json()
            res["_ip"] = {"statut": g.status_code, "pays": j.get("country"),
                          "ville": (j.get("geo") or {}).get("city"), "asn": j.get("asn")}
        else:
            j = requests.get("https://ipinfo.io/json", timeout=20).json()
            res["_ip"] = {k: j.get(k) for k in ("country", "region", "org")}
    except Exception as e:  # information seulement
        res["_ip"] = f"inconnu : {e!r}"[:300]
    for nom, url in SITES.items():
        info: dict = {"url": url}
        try:
            r = requests.get(url, headers=NAVIGATEUR, timeout=60, allow_redirects=True,
                             proxies=proxies, verify=verif)
        except requests.RequestException as e:
            info["erreur"] = repr(e)[:300]
            res[nom] = info
            continue
        info["erreur_proxy"] = erreur_proxy(r)
        html = r.text
        info.update({
            "statut": r.status_code,
            "url_finale": r.url,
            "octets": len(html),
            "preloaded_state": "PRELOADED_STATE" in html,
            "next_data": "__NEXT_DATA__" in html,
            "occurrences_boost": len(re.findall(r"boost", html, re.I)),
            # chemins d'API ou de pages mentionnant un boost (ce qu'on lira ensuite)
            "chemins_boost": sorted(set(re.findall(r"[\"'(](/[^\"'()\s]{0,120}boost[^\"'()\s]{0,80})", html, re.I)))[:40],
            "blocage_probable": r.status_code in (401, 403, 451) or bool(
                re.search(r"pas disponible dans votre pays|not available in your country|geo.?block|captcha|"
                          r"access denied|cloudflare", html[:20000], re.I)),
        })
        # extraits autour de « boost » pour comprendre la structure
        extraits = [html[max(0, m.start() - 200): m.end() + 300] for m in re.finditer(r"boost", html, re.I)][:15]
        ecrire_brut(f"site_{nom}", {"statut": r.status_code, "entetes": dict(r.headers), "extraits": extraits,
                                    "debut": html[:3000]})
        res[nom] = info
    return res


def main() -> None:
    OUT.mkdir(exist_ok=True)
    resume = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    cle = os.environ.get("PULSESCORE_KEY", "").strip()
    if os.environ.get("SONDE_PULSESCORE", "oui") != "oui":
        resume["pulsescore"] = "non lancé (déjà sondé)"
    else:
        resume["pulsescore"] = sonde_pulsescore(cle) if cle else "secret PULSESCORE_KEY absent"
    resume["sites"] = sonde_sites()
    texte = masquer(json.dumps(resume, ensure_ascii=False, indent=2))
    (OUT / "resume.json").write_text(texte, encoding="utf-8")
    print(texte[:60000])


if __name__ == "__main__":
    main()
