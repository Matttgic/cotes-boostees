"""Règlement des boosts par une IA avec recherche web : ChatGPT (OpenAI) ou Claude (Anthropic).

Les boosts sont surtout des paris composés (« X buteur et les deux équipes marquent »,
« A, B et C gagnent ») qu'aucune API de résultats gratuite ne règle d'un coup. On demande donc à
l'IA de chercher les résultats et de trancher, en JSON, avec ses sources.

Fournisseur : OpenAI si le secret OPENAI_API_KEY est présent, sinon Anthropic (ANTHROPIC_API_KEY).
OpenAI : modèle économique (gpt-6-luna) aux deux premiers essais, puis un modèle plus solide
(gpt-6.1-sol) si le premier n'a pas su trancher. REGLEMENT_MODELE impose un modèle unique.

Garde-fous :
- seulement les boosts dont le match a commencé depuis au moins `DELAI_H` heures ;
- au plus `MAX_PAR_PASSAGE` boosts par passage (coût maîtrisé), une nouvelle tentative au plus
  toutes les `ATTENTE_H` heures, `MAX_TENTATIVES` tentatives, puis « à régler à la main » ;
- « inconnu » ne règle rien : le boost reste en attente ;
- `reglements_manuels.json` (branche donnees) a toujours le dernier mot :
  {"winamax|714229410|2213811052": "gagné"}.
"""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timedelta, timezone

from .simulation import PARIS, REGLES

MODELE_IMPOSE = os.environ.get("REGLEMENT_MODELE", "").strip()
MODELES = {"openai": ("gpt-6-luna", "gpt-6.1-sol"), "anthropic": ("claude-haiku-5-5", "claude-sonnet-5-5")}
ESSAIS_MODELE_ECO = 2
DELAI_H = 4
ATTENTE_H = 6
MAX_TENTATIVES = 4
MAX_PAR_PASSAGE = int(os.environ.get("REGLEMENT_MAX", "15"))
MAX_RECHERCHES = 4
# paris à long terme (saison NBA, qualification en playoffs…) : premier essai 120 jours après le début,
# puis un essai par semaine, sans limite (jamais « à la main » faute de résultat)
DELAI_LONG_TERME_J = 120
ATTENTE_LONG_TERME_J = 7

# Règles Winamax utiles au règlement (règlement officiel, vérifiées pour cotes-value)
REGLES_BOOKMAKER = {
    "Winamax": (
        "Règles Winamax : au hockey, sauf mention « prol. et TAB inclus » dans l'intitulé, seul le temps "
        "réglementaire compte ; au basket et au football américain, prolongations incluses ; au baseball, "
        "manches supplémentaires incluses ; au football, temps réglementaire (90 min + arrêts de jeu) sauf "
        "mention contraire. Un pari sur un joueur qui ne participe pas au match est remboursé. "
        "Un match annulé ou reporté de plus de 48 h est remboursé."),
    "Unibet": (
        "Règles Unibet : sauf mention contraire, temps réglementaire (« Temps réglementaire » ou « 80 Mins » au "
        "rugby) ; un pari sur un joueur qui ne débute pas le match est remboursé ; pour les paris de saison "
        "(moyennes, meilleurs marqueurs…), le pari est perdu si le seuil de matchs joués indiqué n'est pas atteint."),
}

CONSIGNE = """Tu règles un pari sportif déjà joué. Cherche le résultat réel sur le web (sources fiables :
sites officiels des ligues, ESPN, L'Équipe, Flashscore, BBC, sites de statistiques).

Bookmaker : {bookmaker}
Sport : {sport}
Match : {match}
Date et heure du match (heure de Paris) : {heure}
Pari : « {pari} »
{regles}

Réponds UNIQUEMENT par un objet JSON, sans texte autour :
{{"statut": "gagné" | "perdu" | "remboursé" | "inconnu",
  "score": "score final et statistiques utiles au pari",
  "explication": "une ou deux phrases : pourquoi le pari est gagné, perdu ou remboursé",
  "sources": ["url", "..."]}}

Règles : « inconnu » si le match n'est pas terminé, si tu ne trouves pas une source fiable pour CHAQUE
condition du pari, ou au moindre doute. Ne devine jamais une statistique."""


def _maintenant() -> datetime:
    return datetime.now(timezone.utc)


def a_regler(base: dict[str, dict], maintenant: datetime | None = None) -> list[dict]:
    """Boosts à soumettre à ce passage, les plus anciens d'abord."""
    t = maintenant or _maintenant()
    out = []
    for b in base.values():
        r = b.get("reglement") or {}
        if r.get("statut") in REGLES or r.get("a_la_main"):
            continue
        lt = bool(b.get("long_terme"))
        delai = timedelta(days=DELAI_LONG_TERME_J) if lt else timedelta(hours=DELAI_H)
        attente = timedelta(days=ATTENTE_LONG_TERME_J) if lt else timedelta(hours=ATTENTE_H)
        if not b.get("debut") or datetime.fromisoformat(b["debut"]) > t - delai:
            continue
        if not lt and r.get("tentatives", 0) >= MAX_TENTATIVES:
            continue
        derniere = r.get("derniere_tentative")
        if derniere and datetime.fromisoformat(derniere) > t - attente:
            continue
        out.append(b)
    out.sort(key=lambda b: b["debut"])
    return out[:MAX_PAR_PASSAGE]


def consigne(b: dict) -> str:
    heure = datetime.fromisoformat(b["debut"]).astimezone(PARIS).strftime("%d/%m/%Y %Hh%M")
    return CONSIGNE.format(bookmaker=b.get("bookmaker"), sport=b.get("sport"), match=b.get("match"),
                           heure=heure, pari=b.get("pari"), regles=REGLES_BOOKMAKER.get(b.get("bookmaker"), ""))


def lire_reponse(texte: str) -> dict:
    """Dernier objet JSON de la réponse ; statut normalisé, « inconnu » si illisible."""
    blocs = re.findall(r"\{.*\}", texte, re.S)
    for brut in reversed(blocs):
        try:
            d = json.loads(brut)
        except json.JSONDecodeError:
            continue
        s = str(d.get("statut", "")).strip().lower()
        s = {"gagne": "gagné", "rembourse": "remboursé", "annulé": "remboursé"}.get(s, s)
        if s not in REGLES:
            s = "inconnu"
        sources = [u for u in d.get("sources") or [] if isinstance(u, str) and u.startswith("http")][:6]
        return {"statut": s, "score": str(d.get("score") or "")[:300],
                "explication": str(d.get("explication") or "")[:600], "sources": sources}
    return {"statut": "inconnu", "score": "", "explication": "réponse illisible", "sources": []}


def fournisseur() -> str | None:
    if os.environ.get("OPENAI_API_KEY", "").strip():
        return "openai"
    if os.environ.get("ANTHROPIC_API_KEY", "").strip():
        return "anthropic"
    return None


def modele(fourn: str, tentatives_passees: int) -> str:
    if MODELE_IMPOSE:
        return MODELE_IMPOSE
    eco, solide = MODELES[fourn]
    return eco if tentatives_passees < ESSAIS_MODELE_ECO else solide


def _demander_openai(client, m: str, texte_consigne: str) -> tuple[str, dict]:
    r = client.responses.create(
        model=m, input=texte_consigne,
        tools=[{"type": "web_search",
                "user_location": {"type": "approximate", "country": "FR", "timezone": "Europe/Paris"}}])
    recherches = sum(1 for o in (r.output or []) if getattr(o, "type", "") == "web_search_call")
    u = r.usage
    return r.output_text or "", {"entree": getattr(u, "input_tokens", 0), "sortie": getattr(u, "output_tokens", 0),
                                 "recherches": recherches}


def _demander_anthropic(client, m: str, texte_consigne: str) -> tuple[str, dict]:
    r = client.messages.create(
        model=m, max_tokens=1500,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": MAX_RECHERCHES,
                "user_location": {"type": "approximate", "country": "FR", "timezone": "Europe/Paris"}}],
        messages=[{"role": "user", "content": texte_consigne}])
    texte = "".join(getattr(c, "text", "") for c in r.content if getattr(c, "type", "") == "text")
    stu = getattr(r.usage, "server_tool_use", None)
    return texte, {"entree": r.usage.input_tokens, "sortie": r.usage.output_tokens,
                   "recherches": getattr(stu, "web_search_requests", 0) if stu else 0}


def client_ia(fourn: str):
    if fourn == "openai":
        from openai import OpenAI
        return OpenAI()
    import anthropic
    return anthropic.Anthropic()


def demander(fourn: str, client, b: dict) -> tuple[dict, dict]:
    """Un appel à l'IA. Renvoie (verdict, usage)."""
    m = modele(fourn, int((b.get("reglement") or {}).get("tentatives", 0)))
    f = _demander_openai if fourn == "openai" else _demander_anthropic
    texte, usage = f(client, m, consigne(b))
    usage["modele"] = m
    return lire_reponse(texte), usage


def appliquer(b: dict, verdict: dict, quand: datetime, modele_utilise: str = "") -> None:
    r = b.setdefault("reglement", {})
    r["tentatives"] = int(r.get("tentatives", 0)) + 1
    r["derniere_tentative"] = quand.isoformat(timespec="seconds")
    r.update({k: verdict[k] for k in ("score", "explication", "sources")})
    r["modele"] = modele_utilise
    if verdict["statut"] in REGLES:
        r["statut"] = verdict["statut"]
        r["regle_le"] = r["derniere_tentative"]
    elif r["tentatives"] >= MAX_TENTATIVES and not b.get("long_terme"):
        r["a_la_main"] = True


def appliquer_manuels(base: dict[str, dict], manuels: dict[str, str], quand: str) -> int:
    n = 0
    for bid, s in manuels.items():
        s = str(s).strip().lower()
        if bid in base and s in REGLES:
            r = base[bid].setdefault("reglement", {})
            if r.get("statut") != s or r.get("source") != "manuel":
                r.update({"statut": s, "source": "manuel", "regle_le": quand, "a_la_main": False})
                n += 1
    return n


def regler(base: dict[str, dict]) -> dict:
    """Passage de règlement (nécessite OPENAI_API_KEY ou ANTHROPIC_API_KEY). Renvoie un résumé."""
    fourn = fournisseur()
    if fourn is None:
        return {"erreur": "aucune clé d'IA (OPENAI_API_KEY ou ANTHROPIC_API_KEY)"}
    client = client_ia(fourn)
    t = _maintenant()
    resume = {"fournisseur": fourn, "soumis": 0, "regles": 0, "inconnus": 0, "erreurs": 0, "recherches": 0,
              "jetons": {}}
    for b in a_regler(base, t):
        resume["soumis"] += 1
        try:
            verdict, usage = demander(fourn, client, b)
        except Exception as e:  # une panne de l'API ne casse pas la collecte
            resume["erreurs"] += 1
            resume["derniere_erreur"] = f"{type(e).__name__} : {e}"[:300]
            continue
        appliquer(b, verdict, t, usage["modele"])
        resume["regles" if verdict["statut"] in REGLES else "inconnus"] += 1
        resume["recherches"] += usage["recherches"]
        j = resume["jetons"].setdefault(usage["modele"], {"entree": 0, "sortie": 0})
        j["entree"] += usage["entree"]
        j["sortie"] += usage["sortie"]
    return resume
