"""« Super Cotes » de Genybet et NetBet (plateforme Sportnco, sites français).

Les deux sites ont la même structure : le « sport » Super Cotes (id 71) à l'adresse /super-cotes, page rendue
côté serveur avec son état dans window.__NUXT__ (lu par boosts/nuxt.py, sans exécuter de JavaScript).
- composants « sport_page_featured » / « competition_page_* » : events[] = un boost par « événement »
  (label « Lille (vs Arsenal) marque au moins 1 but », start, categoryLabel « Super Cote Football »), avec un
  pari « Super Cotes (temps réglementaire, remboursé si un ou plusieurs matchs annulés) » Oui / Non ;
  l'issue « Non » est un artifice à 1 (non jouable) ;
- sport_page_all.topCompetitions.links : les compétitions Super Cotes avec leur nombre d'événements ; si la
  page du sport n'en montre qu'une partie, on lit la page de chaque compétition.
Cote d'origine non publiée. Mise max : 10 € (constatée dans l'appli par l'utilisateur, 13/10/2026).
Lu par l'IP française (proxy) avec l'empreinte de Chrome, environ 140 Ko par page.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone

from . import nuxt
from .unibet import RE_LONG_TERME
from .winamax import PageInattendue, _cote, _texte

SITES = {"genybet": ("Genybet", "https://sport.genybet.fr"), "netbet": ("NetBet", "https://www.netbet.fr")}
CHEMIN = "/super-cotes"
MISE_MAX = 10.0
RE_VS = re.compile(r"^(?P<a>.+?)\s*\(\s*(?:vs\.?|contre|v)\s+(?P<b>[^)]+)\)\s*(?P<reste>.*)$", re.I)
RE_SUPER = re.compile(r"^\s*super\s*cotes?\s*", re.I)


def _composants(etat: dict) -> dict:
    return (((etat.get("state") or {}).get("UFWSClient") or {}).get("components")) or {}


def evenements(etat: dict) -> list[dict]:
    """Tous les événements (avec paris) de la page, sans doublon."""
    vus, out = set(), []

    def parcourir(o):
        if isinstance(o, dict):
            if "label" in o and "start" in o and ("bets" in o or "choices" in o):
                if o.get("id") not in vus:
                    vus.add(o.get("id"))
                    out.append(o)
                return
            for v in o.values():
                parcourir(v)
        elif isinstance(o, list):
            for v in o:
                parcourir(v)

    parcourir(_composants(etat))
    return out


def competitions(etat: dict) -> list[dict]:
    """Compétitions Super Cotes annoncées par la page du sport (adresse, nombre d'événements)."""
    lien = ((((_composants(etat).get("sport_page_all") or {}).get("data") or {}).get("topCompetitions") or {})
            .get("links")) or []
    return [x for x in lien if isinstance(x, dict) and str(x.get("url") or "").startswith(CHEMIN)]


def _utc(iso: str | None) -> str | None:
    try:
        return datetime.fromisoformat(str(iso)).astimezone(timezone.utc).isoformat(timespec="minutes")
    except (TypeError, ValueError):
        return None


def separer(label: str) -> tuple[str | None, str]:
    """« Lille (vs Arsenal) marque au moins 1 but » → (« Lille - Arsenal », label inchangé)."""
    m = RE_VS.match(label or "")
    if not m:
        return None, label
    return f"{m.group('a').strip()} - {m.group('b').strip()}", label


def boosts(etat: dict, cle: str, maintenant: datetime | None = None) -> list[dict]:
    nom, _ = SITES[cle]
    out = []
    for e in evenements(etat):
        debut = _utc(e.get("start"))
        if maintenant is not None and (e.get("live") or e.get("becomeLive")
                                       or (debut and datetime.fromisoformat(debut) <= maintenant)):
            continue                                    # match commencé : boost non jouable avant le début
        label = _texte(e.get("label")) or ""
        match, pari = separer(label)
        sport = _texte(RE_SUPER.sub("", e.get("categoryLabel") or "")) or None
        for b in e.get("bets") or ([e["choices"]] if e.get("choices") else []):
            question = _texte(((b or {}).get("question") or {}).get("label"))
            jouables = [c for c in (b or {}).get("choices") or []
                        if (_cote(c.get("odd")) or 0) > 1.01 and not c.get("isEmptyChoice")
                        and (c.get("actor") or {}).get("label", "").strip().lower() != "non"]
            for c in jouables:
                issue = (c.get("actor") or {}).get("label") or ""
                texte_pari = pari if issue.strip().lower() in ("oui", "yes", "") else f"{pari} — {issue}"
                out.append({
                    "id": f"{cle}|{e.get('id')}|{c.get('id')}",
                    "bookmaker": nom,
                    "match": match or label,
                    "sport": sport,
                    "ligue": None,
                    "pari": texte_pari,
                    "intitule_brut": f"{label} [{question}]" if question else label,
                    "cote_origine": None,
                    "cote_boostee": _cote(c.get("odd")),
                    "hausse_pct": None,
                    "mise_max": MISE_MAX,
                    "mise_max_supposee": False,
                    "type": "cote boostée",
                    "long_terme": bool(RE_LONG_TERME.search(label)),
                    "debut": debut,
                    "disponible": not c.get("status"),
                    "ref": {"event_id": e.get("id"), "choice_id": c.get("id"), "url": e.get("url"),
                            "competition_id": e.get("competitionId")},
                })
    return out


def lire_page(nav, url: str) -> dict:
    r = nav.get(url)
    if r.status_code != 200:
        raise PageInattendue(f"HTTP {r.status_code} sur {url} (blocage probable)")
    return nuxt.etat(r.text)


def collecter_site(cle: str, nav) -> list[dict]:
    _, base = SITES[cle]
    maintenant = datetime.now(timezone.utc)
    etat = lire_page(nav, base + CHEMIN)
    out = boosts(etat, cle, maintenant)
    annonces = competitions(etat)
    if sum(int(c.get("events") or 0) for c in annonces) > len(evenements(etat)):
        for c in annonces:
            out += boosts(lire_page(nav, base + c["url"]), cle, maintenant)
    return list({b["id"]: b for b in out}.values())


def collecter_genybet(nav) -> list[dict]:
    return collecter_site("genybet", nav)


def collecter_netbet(nav) -> list[dict]:
    return collecter_site("netbet", nav)
