"""Règlement des boosts par Claude (API Anthropic + recherche web).

Les boosts sont surtout des paris composés (« X buteur et les deux équipes marquent »,
« A, B et C gagnent ») qu'aucune API de résultats gratuite ne règle d'un coup. On demande donc à
Claude de chercher les résultats et de trancher, en JSON, avec ses sources.

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

MODELE = os.environ.get("REGLEMENT_MODELE", "").strip() or "claude-haiku-5-5"
DELAI_H = 4
ATTENTE_H = 6
MAX_TENTATIVES = 4
MAX_PAR_PASSAGE = int(os.environ.get("REGLEMENT_MAX", "15"))
MAX_RECHERCHES = 4

# Règles Winamax utiles au règlement (règlement officiel, vérifiées pour cotes-value)
REGLES_BOOKMAKER = {
    "Winamax": (
        "Règles Winamax : au hockey, sauf mention « prol. et TAB inclus » dans l'intitulé, seul le temps "
        "réglementaire compte ; au basket et au football américain, prolongations incluses ; au baseball, "
        "manches supplémentaires incluses ; au football, temps réglementaire (90 min + arrêts de jeu) sauf "
        "mention contraire. Un pari sur un joueur qui ne participe pas au match est remboursé. "
        "Un match annulé ou reporté de plus de 48 h est remboursé."),
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
        if not b.get("debut") or datetime.fromisoformat(b["debut"]) > t - timedelta(hours=DELAI_H):
            continue
        if r.get("tentatives", 0) >= MAX_TENTATIVES:
            continue
        derniere = r.get("derniere_tentative")
        if derniere and datetime.fromisoformat(derniere) > t - timedelta(hours=ATTENTE_H):
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


def demander(client, b: dict) -> tuple[dict, dict]:
    """Un appel à Claude. Renvoie (verdict, usage)."""
    r = client.messages.create(
        model=MODELE, max_tokens=1500,
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": MAX_RECHERCHES,
                "user_location": {"type": "approximate", "country": "FR", "timezone": "Europe/Paris"}}],
        messages=[{"role": "user", "content": consigne(b)}])
    texte = "".join(getattr(c, "text", "") for c in r.content if getattr(c, "type", "") == "text")
    stu = getattr(r.usage, "server_tool_use", None)
    usage = {"entree": r.usage.input_tokens, "sortie": r.usage.output_tokens,
             "recherches": getattr(stu, "web_search_requests", 0) if stu else 0}
    return lire_reponse(texte), usage


def appliquer(b: dict, verdict: dict, quand: datetime) -> None:
    r = b.setdefault("reglement", {})
    r["tentatives"] = int(r.get("tentatives", 0)) + 1
    r["derniere_tentative"] = quand.isoformat(timespec="seconds")
    r.update({k: verdict[k] for k in ("score", "explication", "sources")})
    r["modele"] = MODELE
    if verdict["statut"] in REGLES:
        r["statut"] = verdict["statut"]
        r["regle_le"] = r["derniere_tentative"]
    elif r["tentatives"] >= MAX_TENTATIVES:
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
    """Passage de règlement (nécessite ANTHROPIC_API_KEY). Renvoie un résumé."""
    import anthropic
    client = anthropic.Anthropic()
    t = _maintenant()
    resume = {"soumis": 0, "regles": 0, "inconnus": 0, "erreurs": 0, "recherches": 0, "jetons_entree": 0,
              "jetons_sortie": 0}
    for b in a_regler(base, t):
        resume["soumis"] += 1
        try:
            verdict, usage = demander(client, b)
        except Exception as e:  # une panne de l'API ne casse pas la collecte
            resume["erreurs"] += 1
            resume["derniere_erreur"] = f"{type(e).__name__} : {e}"[:300]
            continue
        appliquer(b, verdict, t)
        resume["regles" if verdict["statut"] in REGLES else "inconnus"] += 1
        resume["recherches"] += usage["recherches"]
        resume["jetons_entree"] += usage["entree"]
        resume["jetons_sortie"] += usage["sortie"]
    return resume
