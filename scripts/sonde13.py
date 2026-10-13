"""Sonde n° 13 : cotes boostées Betsson France par son API de contenu (sans navigateur).

POST https://velsv-bson-ssb-pr.betsson.fr/services/content/get
  {"clientContext": {"language": "FR", "ipAddress": "0.0.0.0"}, "contentId": {"type": ..., "id": ...}}
- headline « 1355/20/boostedOddCard » : les cartes « Cotes Boostées » (idfomarket = marché boosté,
  bodytext = marché d'origine ?) ;
- market <id> : le marché et ses sélections (cotes fractionnaires currentpriceup / currentpricedown).
Betsson filtre les IP qu'il situe hors de France : on change d'IP du proxy jusqu'à passer (8 essais).
"""
from __future__ import annotations

import gzip
import json
from datetime import datetime, timezone

from curl_cffi import requests as creq

from sonde import BRUT, OUT, masquer, proxy_francais

API = "https://velsv-bson-ssb-pr.betsson.fr/services/content/get"


def get(s, proxies, verif, type_, id_):
    r = s.post(API, json={"clientContext": {"language": "FR", "ipAddress": "0.0.0.0"},
                          "contentId": {"type": type_, "id": id_}},
               proxies=proxies, verify=verif, timeout=40,
               headers={"Origin": "https://www.betsson.fr", "Referer": "https://www.betsson.fr/",
                        "Accept": "application/json", "Accept-Language": "fr-FR,fr;q=0.9"})
    return r


def main() -> None:
    OUT.mkdir(exist_ok=True)
    BRUT.mkdir(parents=True, exist_ok=True)
    res: dict = {"date_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "essais": []}
    s = creq.Session(impersonate="chrome")
    for essai in range(8):
        proxies, verif = proxy_francais()
        try:
            r = get(s, proxies, verif, "headline", "1355/20/boostedOddCard")
        except Exception as e:  # noqa: BLE001
            res["essais"].append(f"{type(e).__name__} : {e}"[:200])
            continue
        res["essais"].append(r.status_code)
        if r.status_code == 200:
            break
    else:
        texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
        (OUT / "resume13.json").write_text(texte, encoding="utf-8")
        print(texte)
        return
    res["debut_reponse"] = r.text[:300]
    cartes = r.json()
    brut = {"cartes": cartes, "marches": {}}
    items = ((cartes.get("data") or {}).get("headlineItems")) or []
    for it in items:
        for mid in (it.get("idfomarket"), it.get("bodytext")):
            if mid and mid not in brut["marches"]:
                rm = get(s, proxies, verif, "market", mid)
                brut["marches"][mid] = rm.json() if rm.status_code == 200 else {"statut": rm.status_code}
    with gzip.open(BRUT / "betsson_api.json.gz", "wt", encoding="utf-8") as f:
        f.write(json.dumps(brut, ensure_ascii=False))
    res["cartes"] = []
    for it in items:
        m = ((brut["marches"].get(it.get("idfomarket")) or {}).get("data")) or {}
        o = ((brut["marches"].get(it.get("bodytext")) or {}).get("data")) or {}
        res["cartes"].append({
            "carte": it.get("name"), "marche": m.get("name"), "evenement": m.get("eventname"),
            "debut": m.get("tsstart"), "etat": m.get("idfobolifestate"), "fin_paris": m.get("tsbetend"),
            "selections": [(x.get("name"), x.get("currentpriceup"), x.get("currentpricedown"))
                           for x in m.get("selections") or []],
            "origine_marche": o.get("name"),
            "origine_selections": [(x.get("name"), x.get("currentpriceup"), x.get("currentpricedown"))
                                   for x in (o.get("selections") or [])][:6]})
    texte = masquer(json.dumps(res, ensure_ascii=False, indent=2))
    (OUT / "resume13.json").write_text(texte, encoding="utf-8")
    print(texte)


if __name__ == "__main__":
    import traceback
    try:
        main()
    except Exception:  # noqa: BLE001 - la trace va dans le résumé (journaux Actions illisibles d'ici)
        OUT.mkdir(exist_ok=True)
        (OUT / "resume13.json").write_text(masquer(json.dumps({"erreur": traceback.format_exc()[-3000:]},
                                                              ensure_ascii=False, indent=2)), encoding="utf-8")
