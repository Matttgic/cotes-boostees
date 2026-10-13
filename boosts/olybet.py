"""Cotes boostées OlyBet France (« OlyBoosts »).

OlyBet.fr affiche son offre sport via la plateforme BetConstruct (Spring Builder, sports.olybet.fr).
Les données viennent de l'API « swarm » de BetConstruct, en WebSocket, avec l'identifiant du site
olybet.fr (partenaire 18769041) : elle ne renvoie QUE ce qui est proposé sur olybet.fr, pas les offres
OlyBet d'autres pays. Elle répond depuis les serveurs GitHub sans proxy (0 octet Bright Data) ;
le proxy français ne sert qu'en secours.

1. `get_boosted_selections` : les sélections boostées du site, groupées par match ({match: [{Id…}]}) ;
2. `get` sur ces matchs : un boost = un « match » spécial (show_type OUTRIGHT) dont le nom porte
   l'affiche et le pari (« Arsenal - Lille : Les 2 équipes marquent et plus de 2,5 buts (13.10.2026) »),
   un marché et une issue « Oui » à la cote boostée.

La cote d'origine n'est pas exposée (option « previousBoostedOdds » désactivée sur le site).
Mise max : le GAIN NET d'un OlyBoost est plafonné à 25 € (confirmé par l'utilisateur dans l'appli) →
mise max = 25 / (cote − 1), arrondie au centime inférieur.
Constaté le 13/10/2026 (sonde n° 10).
"""
from __future__ import annotations

import json
import math
import os
import re
import time

from .unibet import RE_LONG_TERME
from .winamax import PageInattendue, _cote, _iso, _texte

SWARM = "wss://eu-swarm-reverse.betconstruct.com/"
ORIGINE = "https://sports.olybet.fr"
SITE_ID = 18769041
GAIN_NET_MAX = 25.0
RE_DATE_FIN = re.compile(r"\s*\(\d{1,2}[./]\d{1,2}[./]\d{2,4}\)\s*$")
RE_SUFFIXE_LIGUE = re.compile(r"\s*[-.(]*\s*cotes?\s+boost[ée]es?\s*\)?\s*$", re.I)


def mise_max(cote: float) -> float | None:
    """Mise donnant un gain net de 25 € au plus, au centime inférieur."""
    if not cote or cote <= 1:
        return None
    return math.floor(GAIN_NET_MAX / (cote - 1) * 100 + 1e-9) / 100


def separer(nom: str) -> tuple[str | None, str | None]:
    """« A - B : pari (13.10.2026) » → (« A - B », « pari »). Sans « : », tout le nom est le pari."""
    t = RE_DATE_FIN.sub("", _texte(nom) or "")
    m = re.match(r"^(.+?\S)\s*:\s+(.+)$", t)
    if not m:
        return None, t or None
    return m.group(1).strip(), m.group(2).strip()


def selections(reponse: dict) -> dict[int, set[int]]:
    """Réponse de get_boosted_selections → {id du match: {id des issues boostées}}."""
    details = ((reponse or {}).get("data") or {}).get("details") or {}
    out: dict[int, set[int]] = {}
    for match, liste in details.items():
        for s in liste if isinstance(liste, list) else [liste]:
            if isinstance(s, dict) and s.get("Id") is not None:
                out.setdefault(int(s.get("MatchId") or match), set()).add(int(s["Id"]))
    return out


def boosts(reponse_jeux: dict, choisis: dict[int, set[int]], maintenant: float | None = None) -> list[dict]:
    """Réponse du `get` sur les matchs boostés → boosts au format commun du projet.
    Les matchs commencés sont ignorés : OlyBet laisse parfois un boost en ligne après le coup d'envoi, et
    le simuler serait parier en connaissant le début du match."""
    sports = (((reponse_jeux or {}).get("data") or {}).get("data") or {}).get("sport") or {}
    out = []
    for sp in sports.values():
        sport = _texte(sp.get("name"))
        for comp in (sp.get("competition") or {}).values():
            ligue = RE_SUFFIXE_LIGUE.sub("", _texte(comp.get("name")) or "") or None
            for g in (comp.get("game") or {}).values():
                ids = choisis.get(int(g.get("id") or 0), set())
                if maintenant is not None and (g.get("is_started") or g.get("is_live")
                                               or int(g.get("start_ts") or 0) <= maintenant):
                    continue
                for m in (g.get("market") or {}).values():
                    for e in (m.get("event") or {}).values():
                        if int(e.get("id") or 0) not in ids:
                            continue
                        cote = _cote(e.get("price"))
                        if cote is None:
                            continue
                        nom = m.get("name") or g.get("team1_name") or ""
                        match, pari = separer(nom)
                        if (e.get("name") or "").strip().lower() not in ("oui", "yes", ""):
                            pari = f"{pari} — {e['name']}" if pari else e["name"]
                        out.append({
                            "id": f"olybet|{g.get('id')}|{e.get('id')}",
                            "bookmaker": "OlyBet",
                            "match": match or pari,
                            "sport": sport,
                            "ligue": ligue,
                            "pari": pari,
                            "intitule_brut": _texte(nom),
                            "cote_origine": None,
                            "cote_boostee": cote,
                            "hausse_pct": None,
                            "mise_max": mise_max(cote),
                            "mise_max_supposee": False,
                            "regle_mise": "gain net max 25 €",
                            "type": "cote boostée",
                            "long_terme": bool(RE_LONG_TERME.search(pari or "")),
                            "debut": _iso(g.get("start_ts")),
                            "disponible": not g.get("is_blocked") and not m.get("is_blocked")
                                          and not e.get("is_blocked"),
                            "ref": {"game_id": g.get("id"), "market_id": m.get("id"), "event_id": e.get("id"),
                                    "competition_id": comp.get("id")},
                        })
    return out


class Swarm:
    """Petit client de l'API swarm (WebSocket) : une requête, une réponse portant le même « rid »."""

    def __init__(self, proxies=None, verif=True, timeout: int = 60):
        from curl_cffi.requests import Session
        self._s = Session(impersonate="chrome", proxies=proxies, verify=verif)
        self.ws = self._s.ws_connect(SWARM, headers={"Origin": ORIGINE}, timeout=timeout)
        self._rid = 0
        self.octets = 0

    def appel(self, commande: str, params: dict) -> dict:
        self._rid += 1
        rid = str(self._rid)
        self.ws.send_str(json.dumps({"command": commande, "params": params, "rid": rid}))
        for _ in range(50):                      # messages d'abonnement éventuels ignorés
            brut = self.ws.recv_str()
            self.octets += len(brut)
            m = json.loads(brut)
            if m.get("rid") == rid:
                if m.get("code") not in (0, None):
                    raise PageInattendue(f"swarm {commande} : code {m.get('code')} {m.get('msg') or ''}"[:200])
                return m
        raise PageInattendue(f"swarm {commande} : pas de réponse")

    def fermer(self) -> None:
        try:
            self.ws.close()
        finally:
            self._s.close()


def lire(client: Swarm) -> list[dict]:
    client.appel("request_session", {"site_id": SITE_ID, "language": "fra", "source": 42})
    choisis = selections(client.appel("get_boosted_selections", {}))
    if not choisis:
        return []
    jeux = client.appel("get", {
        "source": "betting",
        "what": {"sport": ["id", "name"], "competition": ["id", "name"], "game": [], "market": [], "event": []},
        "where": {"game": {"id": {"@in": sorted(choisis)}}}, "subscribe": False})
    return boosts(jeux, choisis, time.time())


def collecter(nav=None) -> list[dict]:
    """Accès direct ; en cas d'échec, par le proxy français du navigateur (`nav`)."""
    essais = [(None, True)]
    if nav is not None and os.environ.get("OLYBET_PROXY", "secours") != "jamais":
        essais.append((nav.proxies, nav.verif))
    erreur: Exception | None = None
    for proxies, verif in essais:
        client = None
        try:
            client = Swarm(proxies, verif)
            out = lire(client)
            if proxies and nav is not None:
                nav.octets += client.octets
                nav.requetes += 1
            return out
        except Exception as e:  # noqa: BLE001 - on tente le secours puis on remonte la dernière erreur
            erreur = e
        finally:
            if client is not None:
                client.fermer()
    raise erreur or PageInattendue("OlyBet illisible")
