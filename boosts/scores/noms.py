"""Rapprochement des noms d'équipes et de joueurs entre un bookmaker et un site de scores.

Règle de prudence : au moindre doute, pas de correspondance (le boost reste en attente).
Les paires jamais rapprochées sont archivées par recherche.py pour compléter ALIAS plus tard.
"""
from __future__ import annotations

import re
import unicodedata
from difflib import SequenceMatcher

MOTS_VIDES = {"fc", "cf", "ac", "as", "sc", "afc", "sv", "fk", "bk", "cd", "ud", "rc", "ca", "us", "ssc", "if",
              "club", "de", "la", "le", "les", "the", "of", "bc", "hc", "fa", "ks", "sk", "tsg", "vfl", "vfb",
              "rb", "calcio", "futbol", "football", "olympique"}

# variante normalisée -> nom commun (à compléter au fil des « sans correspondance » archivés)
ALIAS = {
    "paris sg": "paris saint germain", "psg": "paris saint germain", "paris saint germain": "paris saint germain",
    "paris saint-germain": "paris saint germain",
    "marseille": "marseille", "om": "marseille", "lyon": "lyon", "lyonnais": "lyon",
    "bayern munich": "bayern", "bayern munchen": "bayern", "bayern": "bayern",
    "inter milan": "inter", "internazionale": "inter", "inter": "inter",
    "milan": "milan", "ac milan": "milan",
    "man united": "manchester united", "man utd": "manchester united", "manchester united": "manchester united",
    "man city": "manchester city", "manchester city": "manchester city",
    "atletico madrid": "atletico madrid", "atl madrid": "atletico madrid", "atletico de madrid": "atletico madrid",
    "wolfsbourg": "wolfsburg", "wolfsburg": "wolfsburg", "fribourg": "freiburg", "freiburg": "freiburg",
    "cologne": "koln", "koln": "koln", "koeln": "koln", "naples": "napoli", "napoli": "napoli",
    "nottingham forest": "nottingham forest", "nottingham": "nottingham forest", "nott'm forest": "nottingham forest",
    "tottenham": "tottenham", "tottenham hotspur": "tottenham", "spurs": "tottenham",
    "newcastle": "newcastle", "newcastle united": "newcastle", "wolves": "wolverhampton",
    "wolverhampton wanderers": "wolverhampton", "brighton": "brighton", "brighton hove albion": "brighton",
    "saint etienne": "saint etienne", "st etienne": "saint etienne", "slavia prague": "slavia prague",
    "slavia praha": "slavia prague", "sparta prague": "sparta prague", "sparta praha": "sparta prague",
    "galatasaray": "galatasaray", "fenerbahce": "fenerbahce", "benfica": "benfica", "sporting cp": "sporting",
    "sporting": "sporting", "sporting lisbonne": "sporting", "barcelone": "barcelona", "barcelona": "barcelona",
    "fc barcelone": "barcelona", "seville": "sevilla", "sevilla": "sevilla", "la corogne": "deportivo",
    "deportivo la coruna": "deportivo", "deportivo la corogne": "deportivo", "deportivo": "deportivo",
    "bale": "basel", "basel": "basel", "anvers": "antwerp", "antwerp": "antwerp", "gand": "gent", "gent": "gent",
    "bruges": "club brugge", "club brugge": "club brugge", "etats unis": "united states", "pays bas": "netherlands",
    "dinamo minsk": "dinamo minsk", "ska st petersbourg": "ska saint petersburg",
    "ska saint petersburg": "ska saint petersburg", "ska st petersburg": "ska saint petersburg",
}


def normaliser(nom: str) -> str:
    """Minuscules, sans accents ni ponctuation ni mots creux, puis alias."""
    s = unicodedata.normalize("NFKD", str(nom or "")).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9' ]+", " ", s.replace("-", " "))
    brut = " ".join(s.split())
    if brut in ALIAS:
        return ALIAS[brut]
    mots = [m for m in brut.split() if m not in MOTS_VIDES and not (m.isdigit() and len(m) >= 2)]
    court = " ".join(mots) or brut
    return ALIAS.get(court, court)


def equipe_proche(a: str, b: str) -> bool:
    na, nb = normaliser(a), normaliser(b)
    if not na or not nb:
        return False
    if na == nb:
        return True
    ta, tb = set(na.split()), set(nb.split())
    petit, grand = (ta, tb) if len(ta) <= len(tb) else (tb, ta)
    if petit and petit <= grand and any(len(m) >= 4 for m in petit):
        return True
    return SequenceMatcher(None, na, nb).ratio() >= 0.88


def _mots_joueur(nom: str) -> list[str]:
    s = unicodedata.normalize("NFKD", str(nom or "")).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z' ]+", " ", s.replace("-", " "))
    if "," in str(nom or ""):                       # « Jovic, Iva » -> « iva jovic »
        gauche, _, droite = str(nom).partition(",")
        s = re.sub(r"[^a-z' ]+", " ", unicodedata.normalize("NFKD", droite + " " + gauche)
                   .encode("ascii", "ignore").decode().lower().replace("-", " "))
    return s.split()


def _meme_ordre(a: list[str], b: list[str]) -> bool:
    fa, fb = a[-1], b[-1]
    if len(a) > 1 and len(b) > 1 and a[-2] in ("van", "de", "von", "da", "di", "del", "le") and a[-2] == b[-2]:
        fa, fb = a[-2] + fa, b[-2] + fb
    if fa != fb:
        # nom seul (« Antetokounmpo ») contre prénom + nom (« Giannis Antetokounmpo »)
        return len(a) == 1 and a[0] in b or len(b) == 1 and b[0] in a
    pa, pb = a[:-1], b[:-1]
    if not pa or not pb:
        return True
    return pa[0][0] == pb[0][0] and (len(pa[0]) <= 2 or len(pb[0]) <= 2 or pa[0][:3] == pb[0][:3])


def joueur_proche(nom_pari: str, nom_source: str) -> bool:
    """Même joueur : même nom de famille, et prénom ou initiale compatible quand ils sont donnés.
    Les noms de tennis arrivent parfois « Nom Prénom » : on essaie aussi l'ordre inversé (deux mots)."""
    a, b = _mots_joueur(nom_pari), _mots_joueur(nom_source)
    if not a or not b:
        return False
    if a == b or _meme_ordre(a, b):
        return True
    return (len(b) == 2 and _meme_ordre(a, b[::-1])) or (len(a) == 2 and _meme_ordre(a[::-1], b))
