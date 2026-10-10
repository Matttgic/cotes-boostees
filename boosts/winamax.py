"""Cotes boostées Winamax.

Source : https://www.winamax.fr/paris-sportifs/sports/100000 (le « sport » 100000 = Cotes boostées).
La page embarque tout son état dans `PRELOADED_STATE` (JSON) :
- matches[id]  : un boost = un « match » sportId 100000, titre « Cote Boostée : A - B »,
                 categoryId = vrai sport (categories[id].categoryName, boostedOddSportId),
                 matchStart = heure du match (timestamp Unix) ;
- bets[id]     : betTitle « Cote boostée (mise max 20 €) », previousOdd = cote d'origine ;
- outcomes[id] : label = intitulé du pari ;
- odds[id]     : cote boostée de l'issue.
Constaté le 8/10/2026 (sonde n° 3).
"""
from __future__ import annotations

import json
import re
from datetime import datetime, timezone

URL = "https://www.winamax.fr/paris-sportifs/sports/100000"
SPORT_BOOSTS = 100000
RE_MISE = re.compile(r"mise\s+max(?:imale)?\s*(?:de\s*)?(\d+(?:[.,]\d+)?)\s*€", re.I)



# Issue décidée à la fin de la saison, non au démarrage de l'événement Winamax.
RE_LONG_TERME = re.compile(
    r"\b(?:gagne\s+le\s+titre|remporte\s+le\s+titre|"
    r"remporte\s+(?:la|sa)\s+division|"
    r"meilleur\s+(?:marqueur|buteur|passeur|rebondeur)\s+(?:de\s+la|en)\s+saison|"
    r"champion(?:ne)?\s+(?:de|du|d')|"
    r"saison\s+r[ée]guli[èe]re)\b",
    re.I,
)
RE_TITRE_SAISON = re.compile(r"\b20\d{2}\s*[-/]\s*(?:20\d{2}|\d{2})\b")


def est_long_terme(titre: str | None, pari: str | None) -> bool:
    """Détection restrictive : un simple nom de ligue ne suffit pas."""
    p, t = pari or "", titre or ""
    return bool(RE_LONG_TERME.search(p) or
                (RE_TITRE_SAISON.search(t) and
                 re.search(r"\b(?:titre|division|champion|saison|playoffs?)\b", p, re.I)))


def corriger_long_terme(base: dict[str, dict]) -> int:
    """Marque aussi les paris anciens qui ne figurent plus dans le scan."""
    total = 0
    for b in base.values():
        if (b.get("bookmaker") == "Winamax" and not b.get("long_terme")
                and est_long_terme(b.get("match"), b.get("pari"))):
            b["long_terme"] = True
            total += 1
    return total


class PageInattendue(RuntimeError):
    pass


def etat(html: str) -> dict:
    """État JSON de la page (PRELOADED_STATE)."""
    i = html.find("PRELOADED_STATE")
    if i < 0:
        raise PageInattendue("PRELOADED_STATE absent (page de blocage ou site modifié)")
    debut = html.find("{", i)
    if debut < 0:
        raise PageInattendue("PRELOADED_STATE sans objet JSON")
    valeur, _ = json.JSONDecoder().raw_decode(html[debut:])
    if not isinstance(valeur, dict):
        raise PageInattendue("PRELOADED_STATE n'est pas un objet")
    return valeur


def _mise_max(*textes) -> float | None:
    for t in textes:
        if isinstance(t, str):
            m = RE_MISE.search(t)
            if m:
                return float(m.group(1).replace(",", "."))
    return None


def _cote(v) -> float | None:
    try:
        c = round(float(v), 3)      # previousOdd arrive parfois en 3.0901640000000006
    except (TypeError, ValueError):
        return None
    return c if c > 1 else None


def _texte(v) -> str | None:
    """Intitulés Winamax : tabulations et espaces en trop."""
    if not isinstance(v, str):
        return None
    return re.sub(r"\s+", " ", v).strip() or None


def _iso(ts) -> str | None:
    try:
        return datetime.fromtimestamp(int(ts), tz=timezone.utc).isoformat(timespec="minutes")
    except (TypeError, ValueError, OSError):
        return None


def boosts(e: dict) -> list[dict]:
    """Une ligne par issue boostée, au format commun du projet."""
    matchs = e.get("matches") or {}
    paris = e.get("bets") or {}
    issues = e.get("outcomes") or {}
    cotes = e.get("odds") or {}
    categories = e.get("categories") or {}
    tournois = e.get("tournaments") or {}
    out = []
    for mid, m in matchs.items():
        if str(m.get("sportId")) != str(SPORT_BOOSTS):
            continue
        cat = categories.get(str(m.get("categoryId"))) or {}
        tournoi = tournois.get(str(m.get("tournamentId"))) or {}
        titre = re.sub(r"^\s*(?:grosse\s+)?cote\s+boost[ée]e\s*:\s*", "", m.get("title") or "", flags=re.I)
        ids_paris = m.get("bets") or ([m["mainBetId"]] if m.get("mainBetId") else [])
        for bid in ids_paris:
            b = paris.get(str(bid)) or {}
            nom_type = b.get("betTypeName") or b.get("betTitle") or ""
            for oid in b.get("outcomes") or []:
                o = issues.get(str(oid)) or {}
                cote = _cote(cotes.get(str(oid)))
                if cote is None:
                    continue
                origine = _cote(b.get("previousOdd"))
                out.append({
                    "id": f"winamax|{bid}|{oid}",
                    "bookmaker": "Winamax",
                    "match": _texte(titre),
                    "sport": cat.get("categoryName"),
                    "sport_id_winamax": cat.get("boostedOddSportId"),
                    "pari": _texte(o.get("label")),
                    "long_terme": est_long_terme(titre, o.get("label")),
                    "cote_origine": origine,
                    "cote_boostee": cote,
                    "hausse_pct": round((cote / origine - 1) * 100, 1) if origine else None,
                    "mise_max": _mise_max(b.get("betTitle"), b.get("betTypeName"), b.get("betTypeHelp"),
                                          tournoi.get("warning")),
                    "type": "grosse cote boostée" if "grosse" in nom_type.lower() else "cote boostée",
                    "debut": _iso(m.get("matchStart")),
                    "disponible": bool(m.get("available")) and bool(b.get("available", True)),
                    "ref": {"match_id": m.get("matchId") or mid, "bet_id": bid, "outcome_id": oid,
                            "categorie_id": m.get("categoryId"), "tournoi_id": m.get("tournamentId")},
                })
    return out


def collecter(nav) -> list[dict]:
    r = nav.get(URL)
    if r.status_code != 200:
        raise PageInattendue(f"HTTP {r.status_code} (blocage probable)")
    return boosts(etat(r.text))
