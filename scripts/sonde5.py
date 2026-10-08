"""Sonde n° 5 : PMU (et peut-être Unibet) via l'API Kambi.

Découverte (config de pmu.fr, 8/10/2026) : la partie sport de PMU tourne sur la plateforme Kambi,
marque « pmusportsfr », avec l'API d'offre publique
https://eu1.offering-api.kambicdn.com/offering/v2018/pmusportsfr (aucune connexion requise : c'est
elle que le site appelle pour afficher les cotes à tout visiteur).

Ici :
  1. arbre des groupes (sports / compétitions) de PMU : y a-t-il un groupe « boost / super cote » ?
  2. pages d'accueil de l'offre (landing, mises en avant) : traces de boost dans les paris ;
  3. marques Kambi candidates pour Unibet France (Unibet est historiquement sur Kambi).
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone

from curl_cffi import requests as creq

from sonde import OUT, ecrire_brut, masquer, proxy_francais

KAMBI = "https://eu1.offering-api.kambicdn.com/offering/v2018"
PARAMS = "lang=fr_FR&market=FR&client_id=2&channel_id=1"
MOTS = re.compile(r"boost|super ?cote|supercote|cote ?\+|price ?boost|odds ?boost|enhanced", re.I)
MARQUES_UNIBET = ["ubfr", "unibetfr", "ub", "unibet", "ubfrance"]


def get(url, proxies, verif):
    r = creq.get(url, impersonate="chrome", proxies=proxies, verify=verif, timeout=60,
                 headers={"Accept-Language": "fr-FR,fr;q=0.9", "Origin": "https://www.pmu.fr",
                          "Referer": "https://www.pmu.fr/"})
    return r


def groupes_boost(noeud, chemin=""):
    out = []
    nom = noeud.get("name") or noeud.get("englishName") or ""
    c = f"{chemin}/{noeud.get('termKey') or nom}"
    if MOTS.search(nom) or MOTS.search(noeud.get("englishName") or ""):
        out.append({"chemin": c, "nom": nom, "id": noeud.get("id"), "nb": noeud.get("eventCount")})
    for g in noeud.get("groups") or []:
        out += groupes_boost(g, c)
    return out


def traces(texte: str, n=15) -> list[str]:
    return [texte[max(0, m.start() - 300): m.end() + 400] for m in MOTS.finditer(texte)][:n]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    proxies, verif = proxy_francais()
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}
    # 1. arbre des groupes PMU
    try:
        r = get(f"{KAMBI}/pmusportsfr/group.json?{PARAMS}", proxies, verif)
        res["pmu_groupes"] = {"statut": r.status_code, "octets": len(r.content)}
        if r.status_code == 200:
            arbre = r.json().get("group") or {}
            res["pmu_groupes"]["sports"] = [g.get("name") for g in arbre.get("groups") or []][:60]
            res["pmu_groupes"]["boost"] = groupes_boost(arbre)
        else:
            res["pmu_groupes"]["debut"] = r.text[:500]
    except Exception as e:
        res["pmu_groupes"] = {"erreur": masquer(repr(e))[:300]}
    # 2. offre mise en avant
    for nom, chemin in {"landing": "betoffer/landing.json", "highlight": "group/highlight.json",
                        "liste_jour": "listView/all/all/all/all/starting-within.json"}.items():
        try:
            r = get(f"{KAMBI}/pmusportsfr/{chemin}?{PARAMS}&useCombined=true", proxies, verif)
            t = r.text
            res[f"pmu_{nom}"] = {"statut": r.status_code, "octets": len(t), "traces_boost": len(MOTS.findall(t))}
            ecrire_brut(f"kambi_pmu_{nom}", {"debut": t[:3000], "boost": traces(t)})
        except Exception as e:
            res[f"pmu_{nom}"] = {"erreur": masquer(repr(e))[:300]}
    # 3. Unibet sur Kambi ?
    res["unibet"] = {}
    for m in MARQUES_UNIBET:
        try:
            r = get(f"{KAMBI}/{m}/group.json?{PARAMS}", proxies, verif)
            info = {"statut": r.status_code, "octets": len(r.content)}
            if r.status_code == 200:
                arbre = r.json().get("group") or {}
                info["sports"] = [g.get("name") for g in arbre.get("groups") or []][:15]
                info["boost"] = groupes_boost(arbre)
            res["unibet"][m] = info
        except Exception as e:
            res["unibet"][m] = {"erreur": masquer(repr(e))[:200]}
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume5.json").write_text(texte, encoding="utf-8")
    print(texte[:60000])


if __name__ == "__main__":
    main()
