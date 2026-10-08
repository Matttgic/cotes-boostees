"""Sonde n° 6 : structure des cotes boostées sur Kambi.

Sonde n° 5 : la marque Kambi « ub » (Unibet), marché FR, a un groupe « Cotes boostées »
(termKey unibet_featured, 16 événements) ; l'API d'offre Kambi est publique et n'est pas derrière
DataDome. PMU (« pmusportsfr ») n'a pas de groupe « boost » visible.

Ici :
  1. Unibet : contenu complet du groupe unibet_featured (événements, paris, cotes, étiquettes) ;
  2. PMU : paris étiquetés boost / promo dans l'offre football et l'accueil (champ tags des paris).
"""
from __future__ import annotations

import collections
import json
import re
import time
from datetime import datetime, timezone

from curl_cffi import requests as creq

from sonde import OUT, ecrire_brut, masquer, proxy_francais

KAMBI = "https://eu1.offering-api.kambicdn.com/offering/v2018"
PARAMS = "lang=fr_FR&market=FR&client_id=2&channel_id=1&useCombined=true"
MOTS = re.compile(r"boost|super ?cote|supercote|price ?boost|odds ?boost|enhanced|promo", re.I)


def get(url, proxies, verif, referer):
    time.sleep(1.5)                              # la sonde n° 5 a pris des 429 en enchaînant
    return creq.get(url, impersonate="chrome", proxies=proxies, verify=verif, timeout=60,
                    headers={"Accept-Language": "fr-FR,fr;q=0.9", "Origin": referer, "Referer": referer + "/"})


def resume_offre(d: dict) -> dict:
    """Ce qui distingue un boost : étiquettes, types de paris, champs inhabituels des issues."""
    events = d.get("events") or []
    offres = d.get("betOffers") or [o for e in events for o in (e.get("betOffers") or [])]
    tags = collections.Counter(t for o in offres for t in (o.get("tags") or []))
    types = collections.Counter((o.get("betOfferType") or {}).get("name") for o in offres)
    champs_issue = collections.Counter(k for o in offres for oc in (o.get("outcomes") or []) for k in oc)
    champs_offre = collections.Counter(k for o in offres for k in o)
    return {"evenements": len(events), "offres": len(offres), "tags": dict(tags.most_common(30)),
            "types": dict(types.most_common(20)), "champs_offre": dict(champs_offre.most_common(40)),
            "champs_issue": dict(champs_issue.most_common(40))}


def main() -> None:
    OUT.mkdir(exist_ok=True)
    proxies, verif = proxy_francais()
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds")}

    # 1. Unibet, groupe des cotes boostées
    try:
        r = get(f"{KAMBI}/ub/listView/unibet_featured.json?{PARAMS}", proxies, verif, "https://www.unibet.fr")
        res["unibet_boosts"] = {"statut": r.status_code, "octets": len(r.content)}
        if r.status_code == 200:
            d = r.json()
            res["unibet_boosts"].update(resume_offre(d))
            ex = []
            for e in (d.get("events") or [])[:16]:
                ev = e.get("event") or {}
                for o in e.get("betOffers") or []:
                    ex.append({"evenement": ev.get("name"), "debut": ev.get("start"), "sport": ev.get("sport"),
                               "chemin": [p.get("name") for p in ev.get("path") or []],
                               "critere": (o.get("criterion") or {}).get("label"), "tags": o.get("tags"),
                               "issues": [{k: oc.get(k) for k in oc if k not in ("id", "betOfferId")}
                                          for oc in o.get("outcomes") or []],
                               "autres": {k: v for k, v in o.items() if k not in ("outcomes", "criterion", "tags",
                                                                                   "id", "eventId")}})
            res["unibet_boosts"]["exemples"] = ex[:6]
            ecrire_brut("kambi_unibet_boosts", d)
        else:
            res["unibet_boosts"]["debut"] = r.text[:300]
    except Exception as e:
        res["unibet_boosts"] = {"erreur": masquer(repr(e))[:300]}

    # 2. PMU : étiquettes des paris (football du jour + accueil)
    for nom, chemin in {"football": "listView/football.json", "accueil": "betoffer/landing.json"}.items():
        try:
            r = get(f"{KAMBI}/pmusportsfr/{chemin}?{PARAMS}", proxies, verif, "https://www.pmu.fr")
            info = {"statut": r.status_code, "octets": len(r.content)}
            if r.status_code == 200:
                d = r.json()
                info.update(resume_offre(d))
                t = r.text
                info["traces_boost"] = [t[max(0, m.start() - 250): m.end() + 300] for m in MOTS.finditer(t)][:8]
                if nom == "accueil":
                    ecrire_brut("kambi_pmu_accueil", d)
            else:
                info["debut"] = r.text[:300]
            res[f"pmu_{nom}"] = info
        except Exception as e:
            res[f"pmu_{nom}"] = {"erreur": masquer(repr(e))[:300]}

    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume6.json").write_text(texte, encoding="utf-8")
    print(texte[:60000])


if __name__ == "__main__":
    main()
