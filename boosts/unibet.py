"""Cotes boostées Unibet France.

Source : https://www.unibet.fr/cotes-boostees, lue par la zone ISP (IP française) avec l'empreinte de
Chrome, comme Winamax. (Le Web Unlocker de Bright Data refuse les sites de jeux sans vérification
d'identité ; l'offre Kambi « ub » est celle d'Unibet international, pas unibet.fr.)

La page est rendue côté serveur (Angular) ; son état est dans <script id="serverApp-state"> :
- BoostedBets.events[] : un « événement » par match ou par paquet de boosts (« Paris Trashtalk 26/27 »),
  avec SEULEMENT le premier boost (`groupedMarkets`) et le nombre total de paris (`count`) ;
- page de l'événement (lien /paris-<sport>/…/<id>/<slug>) : EventsDetail.events[0].groupedMarkets = tous
  ses boosts.
Chaque intitulé porte la cote d'origine et la mise max : « … (1,80 -> 2,10 / Mise max 25€) ».
Constaté le 8/10/2026 (sondes n° 7 à 9).
"""
from __future__ import annotations

import json
import re

from .winamax import PageInattendue, _cote, _texte

URL = "https://www.unibet.fr/cotes-boostees"
BASE = "https://www.unibet.fr"
MISE_DEFAUT = 25.0                      # mise max habituelle des cotes boostées Unibet (constatée)
RE_COTES = re.compile(r"(\d+[.,]\d+)\s*(?:->|→|&gt;)\s*(\d+[.,]\d+)")
RE_MISE = re.compile(r"mise\s*max\s*(?:de\s*)?(\d+(?:[.,]\d+)?)\s*€", re.I)
RE_PARENTHESE = re.compile(r"\s*/?\s*\((?:[^()]*?(?:->|→|mise\s*max)[^()]*)\)", re.I)
# paris à long terme (saison, classements, playoffs…) : réglés des mois plus tard
RE_LONG_TERME = re.compile(r"\b\d{2}/\d{2}\b|saison|playoffs?|play-?in|division|conf[ée]rence|meilleur "
                           r"(?:marqueur|passeur|rebondeur|intercepteur|buteur)|vainqueur (?:de la|du) "
                           r"(?:ligue|championnat|coupe)|titre", re.I)


def etat(html: str) -> dict:
    m = re.search(r'<script[^>]*id="serverApp-state"[^>]*>(.*?)</script>', html, re.S)
    if not m:
        raise PageInattendue("état serverApp-state absent (page de blocage ou site modifié)")
    return json.loads(m.group(1))


def lien_evenement(html: str, event_id) -> str | None:
    m = re.search(rf'href="(/[^"]*/{event_id}/[^"]*)"', html)
    return BASE + m.group(1) if m else None


def _nettoyer_pari(desc: str) -> str | None:
    t = RE_PARENTHESE.sub("", desc or "")
    t = re.sub(r"^\s*(?:CB|Boost|Cote boostée)\s*[-:]?\s+", "", t, flags=re.I)
    t = re.sub(r"\s*-\s*\d+\s*Mins?\s*$", "", t, flags=re.I)        # « - 80 Mins » (durée du match)
    return _texte(t.strip(" -/"))


def _nombre(s) -> float | None:
    try:
        return float(str(s).replace(",", "."))
    except (TypeError, ValueError):
        return None


def boosts_evenement(e: dict) -> list[dict]:
    path = e.get("path") or {}
    sport = ((path.get("sport") or {}).get("label"))
    ligue = ((path.get("league") or {}).get("label"))
    a, b = (e.get("opponentA") or {}).get("label"), (e.get("opponentB") or {}).get("label")
    match = f"{a} - {b}" if a and b else _texte(e.get("description"))
    out = []
    for g in e.get("groupedMarkets") or []:
        for m in g.get("markets") or []:
            desc = m.get("description") or ""
            # l'issue jouée : celle qui n'est pas cachée (« Oui ») ; « Non » est un artifice à 1,01
            issues = [o for o in m.get("outcomes") or [] if not o.get("hidden") and not o.get("suspended")]
            if len(issues) != 1:
                continue
            o = issues[0]
            cote = _cote(_nombre(o.get("price")))
            if cote is None:
                continue
            fl = RE_COTES.search(desc)
            mise = RE_MISE.search(desc)
            origine = _cote(_nombre(fl.group(1))) if fl else None
            long_terme = bool(RE_LONG_TERME.search(desc) or RE_LONG_TERME.search(e.get("description") or ""))
            out.append({
                "id": f"unibet|{m.get('id')}|{o.get('id')}",
                "bookmaker": "Unibet",
                "match": match,
                "sport": sport,
                "ligue": ligue,
                "pari": _nettoyer_pari(desc),
                "intitule_brut": _texte(desc),
                "cote_origine": origine,
                "cote_boostee": cote,
                "hausse_pct": round((cote / origine - 1) * 100, 1) if origine else None,
                "mise_max": _nombre(mise.group(1)) if mise else MISE_DEFAUT,
                "mise_max_supposee": not bool(mise),
                "type": "cote boostée",
                "long_terme": long_terme,
                "debut": e.get("parsedStart"),
                "disponible": not m.get("suspended"),
                "ref": {"event_id": e.get("id"), "market_id": m.get("id"), "outcome_id": o.get("id"),
                        "periode": m.get("period")},
            })
    return out


def collecter(nav, cache: dict | None = None) -> list[dict]:
    """Page des boosts, puis la page de chaque événement qui a plus de boosts que ceux affichés.
    `cache` (gardé entre deux passages) évite de relire un événement dont le nombre de paris n'a pas
    changé depuis moins de 6 passages : on réutilise alors les boosts lus la dernière fois."""
    cache = cache if cache is not None else {}
    r = nav.get(URL)
    if r.status_code != 200:
        raise PageInattendue(f"HTTP {r.status_code} (blocage probable)")
    html = r.text
    events = (etat(html).get("BoostedBets") or {}).get("events") or []
    out = []
    for e in events:
        lus = boosts_evenement(e)
        affiches = sum(len(g.get("markets") or []) for g in e.get("groupedMarkets") or [])
        if int(e.get("count") or 0) > affiches:
            cle = str(e.get("id"))
            c = cache.get(cle) or {}
            if c.get("count") == e.get("count") and c.get("age", 99) < 6 and c.get("boosts"):
                c["age"] = c.get("age", 0) + 1
                lus = c["boosts"]
            else:
                lien = lien_evenement(html, e.get("id"))
                if lien:
                    rd = nav.get(lien)
                    if rd.status_code == 200:
                        detail = (etat(rd.text).get("EventsDetail") or {}).get("events") or []
                        if detail:
                            lus = boosts_evenement({**e, **detail[0]})
                            cache[cle] = {"count": e.get("count"), "age": 0, "boosts": lus}
        out += lus
    vus = {str(e.get("id")) for e in events}
    for cle in list(cache):
        if cle not in vus:
            del cache[cle]
    return out
