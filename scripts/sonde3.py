"""Sonde n° 3 : lire réellement les boosts.

Résultat de la sonde n° 2 : avec l'empreinte de Chrome (curl_cffi), Winamax répond (200) et sa page
contient PRELOADED_STATE ; les boosts y sont le « sport » 100000 « Cotes boostées » (catégories
par vrai sport, plafond de mise écrit dans le champ « warning » du tournoi). Unibet reste bloqué
par DataDome. PMU : la page sport est une coquille ; ses données passent par
parisportif.pmu.fr/home/wrapper/... (paramètre « boost » repéré dans la config).

Ici :
  1. Winamax : page du sport 100000, extraction des matchs, paris, issues et cotes boostés,
     avec TOUS les champs bruts (pour repérer cote d'origine / cote boostée / plafond) ;
  2. PMU : pages « wrapper » et promotions, traces de boost.
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from curl_cffi import requests as creq

from sonde import OUT, ecrire_brut, masquer, proxy_francais

MOTS = re.compile(r"boost|super ?cote|supercote", re.I)


def get(url: str, proxies, verif):
    return creq.get(url, impersonate="chrome", proxies=proxies, verify=verif, timeout=60,
                    headers={"Accept-Language": "fr-FR,fr;q=0.9"})


def etat_winamax(html: str) -> dict | None:
    i = html.find("PRELOADED_STATE")
    if i < 0:
        return None
    debut = html.find("{", i)
    etat, _ = json.JSONDecoder().raw_decode(html[debut:])
    return etat


def sonde_winamax(proxies, verif) -> dict:
    r = get("https://www.winamax.fr/paris-sportifs/sports/100000", proxies, verif)
    info: dict = {"statut": r.status_code, "octets": len(r.content)}
    etat = etat_winamax(r.text) if r.status_code == 200 else None
    if not etat:
        info["erreur"] = "PRELOADED_STATE introuvable"
        return info
    info["cles_etat"] = sorted(etat.keys())[:80]
    matchs = etat.get("matches") or {}
    paris = etat.get("bets") or {}
    issues = etat.get("outcomes") or {}
    cotes = etat.get("odds") or {}
    boostes = {k: m for k, m in matchs.items() if str(m.get("sportId")) == "100000"}
    info["nb_matchs_boost"] = len(boostes)
    exemples = []
    for mid, m in boostes.items():
        ex = {"match": m, "paris": []}
        for bid in m.get("bets") or ([m["mainBetId"]] if m.get("mainBetId") else []):
            b = paris.get(str(bid)) or {}
            ex["paris"].append({"pari": b, "issues": [
                {"issue": issues.get(str(o)), "cote": cotes.get(str(o))} for o in b.get("outcomes") or []]})
        exemples.append(ex)
    info["exemples"] = exemples[:3]          # le détail complet est dans brut/
    # champs dont le nom évoque une cote d'origine / un boost, partout dans l'état
    noms = set()

    def parcourir(x, chemin=""):
        if isinstance(x, dict):
            for k, v in x.items():
                if re.search(r"boost|previous|old|origin|initial|max(bet|stake)|limit", k, re.I):
                    noms.add(f"{chemin}.{k}" if chemin else k)
                if len(noms) < 200:
                    parcourir(v, k)
        elif isinstance(x, list):
            for v in x[:50]:
                parcourir(v, chemin)
    parcourir(etat)
    info["champs_suspects"] = sorted(noms)[:120]
    ecrire_brut("winamax_boosts", {"tournois": {k: v for k, v in (etat.get("tournaments") or {}).items()
                                               if "Boost" in json.dumps(v, ensure_ascii=False)},
                                   "matchs": exemples})
    return info


def sonde_pmu(proxies, verif) -> dict:
    urls = {
        "wrapper_events": "https://parisportif.pmu.fr/home/wrapper/events?lang=fr&rst=betslip",
        "wrapper_dashboard": "https://parisportif.pmu.fr/home/wrapper/dashboard?lang=fr",
        "promotions": "https://parisportif.pmu.fr/promotions",
    }
    res = {}
    for nom, url in urls.items():
        try:
            r = get(url, proxies, verif)
        except Exception as e:
            res[nom] = {"erreur": masquer(repr(e))[:300]}
            continue
        t = r.text
        res[nom] = {"statut": r.status_code, "type": r.headers.get("content-type"), "octets": len(t),
                    "url_finale": r.url, "occurrences_boost": len(MOTS.findall(t)),
                    "urls_internes": sorted(set(re.findall(r"[\"'](/[a-z0-9_/-]{3,80}(?:\?[^\"'\s]{0,80})?)[\"']", t)))[:60]}
        ecrire_brut(f"pmu_{nom}", {"debut": t[:4000], "boost": [t[max(0, m.start() - 250): m.end() + 350]
                                                               for m in MOTS.finditer(t)][:20]})
    return res


def main() -> None:
    OUT.mkdir(exist_ok=True)
    proxies, verif = proxy_francais()
    if not proxies:
        raise SystemExit("Secrets Bright Data absents.")
    resume: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    for nom, f in (("winamax", sonde_winamax), ("pmu", sonde_pmu)):
        try:
            resume[nom] = f(proxies, verif)
        except Exception as e:
            resume[nom] = {"erreur": masquer(repr(e))[:400]}
    texte = masquer(json.dumps(resume, ensure_ascii=False, indent=2))
    (OUT / "resume3.json").write_text(texte, encoding="utf-8")
    print(texte[:60000])


if __name__ == "__main__":
    main()
