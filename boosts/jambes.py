"""Traduction d'un boost (texte libre Winamax) en « jambes » structurées, par l'IA (sans recherche web).

« Nantes gagne et plus de 58,5 buts dans le match » →
  [{type: resultat, equipe: Nantes}, {type: total, sens: plus, ligne: 58.5}]

Chaque jambe est ensuite cherchée telle quelle chez Pinnacle (boosts/valeur.py). Tout ce que
Pinnacle ne cote pas (score exact, « les deux équipes marquent » hors football, etc.) devient
une jambe « autre » : le boost est alors « non évaluable », jamais deviné.
Appel fait une seule fois par boost, avec le modèle économique (quelques centièmes de centime).
"""
from __future__ import annotations

import json
import os
import re

from .reglement import MODELES, client_ia, fournisseur

TYPES = {"resultat", "vainqueur", "handicap", "total", "total_equipe", "les_deux_marquent", "joueur", "autre"}

CONSIGNE = """Décompose ce pari sportif en conditions élémentaires (« jambes »). Toutes doivent être vraies
pour que le pari soit gagné.

Sport : {sport}
Titre Winamax : {match}
Pari : « {pari} »

Réponds UNIQUEMENT par un objet JSON :
{{"jambes": [{{
  "equipe_1": "équipe à domicile du match concerné (première citée dans le titre, sinon dans le pari)",
  "equipe_2": "équipe à l'extérieur de ce match",
  "type": "resultat | vainqueur | handicap | total | total_equipe | les_deux_marquent | joueur | autre",
  "equipe": "équipe visée (ou \\"nul\\" pour un match nul), sinon null",
  "sens": "plus | moins | null",
  "ligne": nombre ou null,
  "periode": "match | temps_reglementaire | mi_temps_1",
  "unite": "buts | sets | jeux | corners",
  "joueur": "nom complet du joueur ou null",
  "stat": "statistique du joueur en anglais façon bookmaker (Goals, Points, Rebounds, Assists, Shots On Goal, Rushing Yards, Receiving Yards, Passing Yards, Touchdowns, Hits, Strikeouts…) ou null"
}}]}}

Règles de traduction :
- « X gagne » : type resultat si le nul existe sur la période (football, handball, rugby, hockey en temps
  réglementaire) ; type vainqueur sinon (tennis, basket, baseball, football américain, hockey quand
  l'intitulé dit « prol. et TAB inclus », MMA…). Au hockey : periode temps_reglementaire, sauf « prol. et
  TAB inclus » → periode match.
- « X gagne par au moins N points/buts d'écart » → type handicap, equipe X, ligne = -(N - 0,5).
- « plus de N,5 » → sens plus, ligne N,5 ; « au moins N » → sens plus, ligne N - 0,5 ;
  « moins de N,5 » → sens moins, ligne N,5.
- « X marque au moins N buts » → type total_equipe, equipe X, sens plus, ligne N - 0,5.
- « plus de 2,5 sets » → type total, unite sets. Total de jeux au tennis → unite jeux.
- Joueur : « Y buteur » → type joueur, stat Goals, sens plus, ligne 0,5 ; « Y marque au moins un
  touchdown » → stat Touchdowns, ligne 0,5 ; « Y réalise au moins 81 yards à la course » → stat
  Rushing Yards, sens plus, ligne 80,5.
- Plusieurs matchs (« A, B et C gagnent chacun leur match (respectivement contre D, E et F) ») : une jambe
  par match, avec ses deux équipes.
- « Les deux équipes marquent » au football → les_deux_marquent ; dans un autre sport (« chacune au moins
  3 runs ») → une jambe total_equipe par équipe.
- Tout le reste (score exact, buteur à un moment précis, statistique impossible à exprimer ainsi…) → autre.
- Noms d'équipes et de joueurs écrits comme dans le titre ou le pari, sans traduction."""


def consigne(b: dict) -> str:
    return CONSIGNE.format(sport=b.get("sport"), match=b.get("match"), pari=b.get("pari"))


def _nombre(x):
    if x is None or x == "":
        return None
    try:
        return float(str(x).replace(",", "."))
    except ValueError:
        return None


def lire(texte: str) -> list[dict] | None:
    """Jambes validées, ou None si la réponse est inutilisable."""
    for brut in reversed(re.findall(r"\{.*\}", texte or "", re.S)):
        try:
            d = json.loads(brut)
        except json.JSONDecodeError:
            continue
        jambes = d.get("jambes") if isinstance(d, dict) else None
        if not isinstance(jambes, list) or not jambes:
            continue
        out = []
        for j in jambes:
            if not isinstance(j, dict):
                return None
            t = str(j.get("type") or "autre").strip().lower()
            out.append({
                "equipe_1": (j.get("equipe_1") or "").strip() or None,
                "equipe_2": (j.get("equipe_2") or "").strip() or None,
                "type": t if t in TYPES else "autre",
                "equipe": (str(j["equipe"]).strip() or None) if j.get("equipe") else None,
                "sens": (str(j.get("sens") or "").lower() or None) if j.get("sens") in ("plus", "moins") else None,
                "ligne": _nombre(j.get("ligne")),
                "periode": j.get("periode") if j.get("periode") in ("match", "temps_reglementaire", "mi_temps_1")
                else "match",
                "unite": j.get("unite") if j.get("unite") in ("buts", "sets", "jeux", "corners") else "buts",
                "joueur": (str(j["joueur"]).strip() or None) if j.get("joueur") else None,
                "stat": (str(j["stat"]).strip() or None) if j.get("stat") else None,
            })
        return out
    return None


def decomposer(b: dict, client=None, fourn: str | None = None) -> tuple[list[dict] | None, str]:
    """Appel à l'IA ; renvoie (jambes ou None, modèle utilisé)."""
    fourn = fourn or fournisseur()
    if fourn is None:
        return None, ""
    client = client or client_ia(fourn)
    m = os.environ.get("JAMBES_MODELE", "").strip() or MODELES[fourn][0]
    if fourn == "openai":
        r = client.responses.create(model=m, input=consigne(b))
        texte = r.output_text or ""
    else:
        r = client.messages.create(model=m, max_tokens=1200, messages=[{"role": "user", "content": consigne(b)}])
        texte = "".join(getattr(c, "text", "") for c in r.content if getattr(c, "type", "") == "text")
    return lire(texte), m
