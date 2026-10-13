"""Cotes boostées Betsson France (« Flash Boost »).

betsson.fr est une application JavaScript ; ses données viennent d'une API de contenu (POST JSON) :
  https://velsv-bson-ssb-pr.betsson.fr/services/content/get
  {"clientContext": {"language": "FR", "ipAddress": "0.0.0.0"}, "contentId": {"type": …, "id": …}}
- headline « 1355/20/boostedOddCard » : les cartes « Cotes Boostées » de l'accueil ; chaque carte donne
  le marché boosté (idfomarket) et, dans `bodytext`, le marché d'origine du même match ;
- market <id> : nom (« 🐦‍🔥 Barcola Buteur (Max 20€) - Flash Boost »), match, début, état, sélections en
  cote fractionnaire (currentpriceup / currentpricedown → 1 + up/down). Une carte périmée renvoie
  CONTENT_NOT_FOUND. La cote d'origine = même sélection (même nom) dans le marché d'origine.
Betsson refuse les IP que sa base géographique situe hors de France (« Geoloc redirection », 403) : une
partie des IP du proxy « françaises » sont dans ce cas. On garde la session qui passe (cache entre deux
passages) et on en essaie d'autres sinon. Constaté le 13/10/2026 (sondes n° 12 et 13).
"""
from __future__ import annotations

import os
import re
from datetime import datetime, timezone

from .acces import proxy_francais
from .unibet import RE_LONG_TERME
from .winamax import PageInattendue, _cote, _texte

API = "https://velsv-bson-ssb-pr.betsson.fr/services/content/get"
CARTES = ("headline", "1355/20/boostedOddCard")
ENTETES = {"Origin": "https://www.betsson.fr", "Referer": "https://www.betsson.fr/", "Accept": "application/json"}
ESSAIS_IP = 8
MISE_DEFAUT = 20.0
RE_MISE = re.compile(r"max\.?\s*(\d+(?:[.,]\d+)?)\s*€", re.I)
RE_DECOR = re.compile(r"\s*\((?:[^()]*max[^()]*)\)|\s*-\s*flash\s*boost\s*$|\s*-\s*boost(?:ée?)?\s*$", re.I)
RE_EMOJI = re.compile(r"^[^\wÀ-ÿ(«\"']+")
RE_RATING = re.compile(r"\s+rating\s+\d+\s*$", re.I)


def corps(type_: str, id_: str) -> dict:
    return {"clientContext": {"language": "FR", "ipAddress": "0.0.0.0"}, "contentId": {"type": type_, "id": id_}}


def cote(sel: dict) -> float | None:
    try:
        return _cote(1 + int(sel["currentpriceup"]) / int(sel["currentpricedown"]))
    except (KeyError, TypeError, ValueError, ZeroDivisionError):
        return None


def nettoyer(nom: str) -> str:
    t = RE_DECOR.sub("", _texte(nom) or "")
    t = RE_DECOR.sub("", t)
    return RE_EMOJI.sub("", t).strip(" -")


def _utc(iso: str | None) -> str | None:
    try:
        return datetime.fromisoformat(str(iso)).astimezone(timezone.utc).isoformat(timespec="minutes")
    except (TypeError, ValueError):
        return None


def _donnees(rep: dict | None) -> dict:
    d = (rep or {}).get("data")
    return d if isinstance(d, dict) else {}


def cartes(rep: dict) -> list[dict]:
    return [c for c in (_donnees(rep).get("headlineItems") or []) if c.get("idfomarket")]


def boosts(rep_cartes: dict, marches: dict[str, dict], maintenant: datetime | None = None) -> list[dict]:
    """Cartes + réponses « market » (par identifiant) → boosts au format commun du projet."""
    out = []
    for carte in cartes(rep_cartes):
        m = _donnees(marches.get(carte["idfomarket"]))
        if not m:
            continue                                     # carte périmée (CONTENT_NOT_FOUND)
        debut = _utc(m.get("tsstart"))
        fin = _utc(m.get("tsbetend")) or debut
        if maintenant is not None and (m.get("is4inrunning") or (fin and datetime.fromisoformat(fin) <= maintenant)):
            continue                                     # match commencé ou paris fermés
        origine = _donnees(marches.get(carte.get("bodytext") or ""))
        if origine.get("idfoevent") != m.get("idfoevent"):
            origine = {}
        nom = _texte(m.get("name")) or ""
        mise = RE_MISE.search(nom)
        pari = nettoyer(nom)
        a, b = _texte(m.get("participantname_home")), _texte(m.get("participantname_away"))
        for s in m.get("selections") or []:
            c = cote(s)
            if c is None:
                continue
            avant = next((cote(x) for x in origine.get("selections") or [] if x.get("name") == s.get("name")), None)
            texte_pari = pari if len(m.get("selections") or []) == 1 else f"{pari} — {s.get('name')}"
            out.append({
                "id": f"betsson|{m.get('idfomarket')}|{s.get('idfoselection')}",
                "bookmaker": "Betsson",
                "match": f"{a} - {b}" if a and b else _texte(m.get("eventname")),
                "sport": _texte(RE_RATING.sub("", m.get("sportname") or "")) or None,
                "ligue": _texte(m.get("tournamentname")),
                "pari": texte_pari,
                "intitule_brut": f"{nom} [{s.get('name')}]",
                "cote_origine": avant,
                "cote_boostee": c,
                "hausse_pct": round((c / avant - 1) * 100, 1) if avant else None,
                "mise_max": float(mise.group(1).replace(",", ".")) if mise else MISE_DEFAUT,
                "mise_max_supposee": not bool(mise),
                "type": "cote boostée",
                "long_terme": bool(RE_LONG_TERME.search(pari)),
                "debut": debut,
                "disponible": bool(m.get("istradable")) and m.get("idfobolifestate") in (None, "O")
                              and not s.get("idfoselectionsuspensiontype"),
                "ref": {"market_id": m.get("idfomarket"), "selection_id": s.get("idfoselection"),
                        "event_id": m.get("idfoevent"), "marche_origine": carte.get("bodytext")},
            })
    return out


def _session_qui_passe(nav, cache: dict) -> tuple[dict, dict]:
    """(proxies, réponse des cartes) avec une IP acceptée par Betsson ; la session gagnante est gardée."""
    sessions = ([cache["session"]] if cache.get("session") else []) + \
               [os.urandom(4).hex() for _ in range(ESSAIS_IP)]
    statuts = []
    for s in sessions:
        proxies = proxy_francais(s)
        try:
            r = nav.post(API, json=corps(*CARTES), headers=ENTETES, proxies=proxies)
        except Exception as e:  # noqa: BLE001 - IP suivante
            statuts.append(type(e).__name__)
            continue
        statuts.append(r.status_code)
        if r.status_code == 200:
            try:
                rep = r.json()
            except ValueError:
                continue
            cache["session"] = s
            cache["essais"] = len(statuts)
            return proxies, rep
    cache.pop("session", None)
    raise PageInattendue(f"aucune IP acceptée par Betsson ({statuts})")


def collecter(nav, cache: dict | None = None) -> list[dict]:
    cache = cache if cache is not None else {}
    proxies, rep = _session_qui_passe(nav, cache)
    marches: dict[str, dict] = {}
    for carte in cartes(rep):
        for mid in (carte.get("idfomarket"), carte.get("bodytext")):
            if mid and mid not in marches:
                r = nav.post(API, json=corps("market", mid), headers=ENTETES, proxies=proxies)
                marches[mid] = r.json() if r.status_code == 200 else {}
                if not _donnees(marches[mid]) and mid == carte.get("idfomarket"):
                    break                                # carte périmée : inutile de lire son marché d'origine
    return boosts(rep, marches, datetime.now(timezone.utc))
