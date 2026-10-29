"""Texte libre d'un pari -> conditions (« jambes ») vérifiables sur un résultat réel, par règles.

Aucune IA : on ne reconnaît que des formulations courantes. Tout ce qui n'est pas reconnu (plusieurs matchs,
« premier buteur », « ou », F1…) renvoie None : le boost reste en attente, jamais deviné.
Les jambes produites servent UNIQUEMENT au règlement (elles ne remplacent pas `jambes`, qui alimente la
valeur Pinnacle). Format d'une jambe : type, equipe, sens, ligne, periode, score, unite, joueur, stat, avec en
plus `joueurs` + `mode` (« chacun » | « somme ») pour plusieurs joueurs.
"""
from __future__ import annotations

import re
import unicodedata

from .scores.noms import equipe_proche, joueur_proche
from .scores.sources import SPORTS

AVEC_NUL = {"football", "handball", "rugby"}
NB = r"(\d+(?:\.\d+)?)"
STATS = {"points": "Points", "rebonds": "Rebounds", "passes decisives": "Assists", "passes": "Assists",
         "buts": "Goals"}


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", str(s or "")).encode("ascii", "ignore").decode().lower()
    s = s.replace("’", "'").replace("`", "'")
    s = re.sub(r"(\d),(\d)", r"\1.\2", s)
    s = re.sub(r"[!?]+", " ", s)
    return " ".join(s.split())


def _jambe(type_, **kw) -> dict:
    return {"type": type_, "equipe": kw.get("equipe"), "sens": kw.get("sens"), "ligne": kw.get("ligne"),
            "periode": kw.get("periode", "match"), "score": kw.get("score"), "unite": kw.get("unite"),
            "joueur": kw.get("joueur"), "stat": kw.get("stat"), "joueurs": kw.get("joueurs"), "mode": kw.get("mode"),
            "ref": kw.get("ref")}


class _Ctx:
    def __init__(self, sport: str, equipes: tuple[str, str], brut: str):
        self.sport = sport
        self.e1, self.e2 = equipes
        self.tennis = sport in ("tennis", "tennis_table", "badminton")
        self.prol_incluse = "prol" in brut and "inclus" in brut

    def equipe(self, nom: str) -> str | None:
        """Nom de l'équipe/joueur visé s'il est l'un des deux protagonistes du match, sinon None."""
        for e in (self.e1, self.e2):
            if e and (joueur_proche(nom, e) if self.tennis else equipe_proche(nom, e)):
                return e
        return None

    def gagne(self, eq: str, periode: str = "match") -> dict:
        if self.sport in AVEC_NUL:
            return _jambe("resultat", equipe=eq, periode=periode)
        if self.sport == "hockey" and not self.prol_incluse:
            return _jambe("resultat", equipe=eq, periode="temps_reglementaire")
        return _jambe("vainqueur", equipe=eq, periode=periode)


def _periode(t: str) -> str:
    if re.search(r"(1ere|1re|premiere) mi-temps", t):
        return "mi_temps_1"
    if re.search(r"(2eme|2e|deuxieme) mi-temps", t):
        return "mi_temps_2"
    return "match"


def _clause(t: str, c: _Ctx) -> list[dict] | None:
    t = re.sub(r"\s*\((?!respectivement).*?\)\s*$", "", t).strip()
    if "respectivement" in t or "chacun leur match" in t or "chacun des" in t:
        return None
    m = re.fullmatch(rf"(plus|moins) de {NB} (buts|jeux|sets|points|runs)( dans le match| lors du match)?", t)
    if m:
        return [_jambe("total", sens=m[1], ligne=float(m[2]), unite=m[3])]
    if t in ("les deux equipes marquent", "les deux equipes marquent dans le match"):
        return [_jambe("les_deux_marquent")]
    m = re.fullmatch(r"exactement (\d) sets lors du match", t)
    if m and c.tennis:
        return [_jambe("total_exact", ligne=float(m[1]), unite="sets")]
    if t in ("les 2 joueurs gagnent un set", "les deux joueurs gagnent un set") and c.tennis:
        return [_jambe("total", sens="plus", ligne=2.5, unite="sets")]
    m = re.fullmatch(r"(.+?) gagne le premier set(?: et le match)?", t)
    if m and c.tennis and c.equipe(m[1]):
        eq = c.equipe(m[1])
        legs = [_jambe("vainqueur", equipe=eq, periode="set_1")]
        return legs + [c.gagne(eq)] if t.endswith("et le match") else legs
    m = re.fullmatch(r"(.+?) gagne la (?:premiere|1ere) mi-temps", t)
    if m and c.sport == "football" and c.equipe(m[1]):
        return [c.gagne(c.equipe(m[1]), "mi_temps_1")]
    m = re.fullmatch(r"(.+?) gagne ou fait match nul", t)
    if m and c.sport == "football" and c.equipe(m[1]):
        return [_jambe("double_chance", equipe=c.equipe(m[1]))]
    m = re.fullmatch(r"(.+?) gagne le match (\d-\d(?:, \d-\d)*(?:,? ou \d-\d)?)(?: \(hors tab\))?", t)
    if m and c.sport == "football" and c.equipe(m[1]):
        scores = re.findall(r"\d-\d", m[2])
        return [_jambe("score_exact_liste", equipe=c.equipe(m[1]), score="|".join(scores), ref=c.e1)]
    m = re.fullmatch(r"(.+?) (?:gagne|remporte le match|l'emporte)(?: le match)? (\d)-(\d)(?: en sets)?", t)
    if m and c.tennis and c.equipe(m[1]):
        return [_jambe("score_sets", equipe=c.equipe(m[1]), score=f"{m[2]}-{m[3]}")]
    m = re.fullmatch(r"(.+?) remporte le match sur le score exact de (\d)-(\d)(?: en sets)?", t)
    if m and c.tennis and c.equipe(m[1]):
        return [_jambe("score_sets", equipe=c.equipe(m[1]), score=f"{m[2]}-{m[3]}")]
    m = re.fullmatch(r"(.+?) gagne (\d+)-(\d+)", t)
    if m and c.sport == "football" and c.equipe(m[1]):
        return [_jambe("score_exact", equipe=c.equipe(m[1]), score=f"{m[2]}-{m[3]}", ref=c.e1)]
    m = re.fullmatch(r"(.+?) gagne par au moins (\d+) (?:points?|buts?)(?: d'ecart)?", t)
    if m and c.equipe(m[1]):
        unite = "buts" if c.sport in ("football", "hockey", "handball", "rugby") else "points"
        return [_jambe("handicap", equipe=c.equipe(m[1]), ligne=-(int(m[2]) - 0.5), unite=unite)]
    m = re.fullmatch(r"(.+?) (?:mene|menait) a la mi-temps et gagne(?: le match)?", t)
    if m and c.sport == "football" and c.equipe(m[1]):
        eq = c.equipe(m[1])
        return [c.gagne(eq, "mi_temps_1"), c.gagne(eq)]
    m = re.fullmatch(r"(.+?) remporte les deux mi-temps", t)
    if m and c.sport == "football" and c.equipe(m[1]):
        eq = c.equipe(m[1])
        return [c.gagne(eq, "mi_temps_1"), c.gagne(eq, "mi_temps_2")]
    m = re.fullmatch(r"(.+?) marque dans les deux mi-temps", t)
    if m and c.sport == "football" and c.equipe(m[1]):
        eq = c.equipe(m[1])
        return [_jambe("total_equipe", equipe=eq, sens="plus", ligne=0.5, unite="buts", periode="mi_temps_1"),
                _jambe("total_equipe", equipe=eq, sens="plus", ligne=0.5, unite="buts", periode="mi_temps_2")]
    m = re.fullmatch(rf"(.+?) gagne et plus de {NB} jeux dans le match", t)
    if m and c.equipe(m[1]):
        return [c.gagne(c.equipe(m[1])), _jambe("total", sens="plus", ligne=float(m[2]), unite="jeux")]
    m = re.fullmatch(r"(.+?) (?:gagne|remporte le match|l'emporte)(?: le match)?", t)
    if m and c.equipe(m[1]):
        return [c.gagne(c.equipe(m[1]))]
    m = re.fullmatch(rf"(.+?) marque au moins {NB} buts(?: contre .+)?", t)
    if m and c.equipe(m[1]):
        return [_jambe("total_equipe", equipe=c.equipe(m[1]), sens="plus", ligne=float(m[2]) - 0.5, unite="buts")]
    m = re.fullmatch(r"(.+?) buteur", t)
    if m and not c.equipe(m[1]):
        return [_jambe("joueur", joueur=m[1].strip(), stat="Goals", sens="plus", ligne=0.5)]
    m = re.fullmatch(rf"(.+?) marque (?:au moins )?(un|{NB})\+?(?: ou \+| ou plus)? ?(?:but|buts)"
                     r"(?: en (?:1ere|1re|2eme|2e) mi-temps)?", t)
    if m and not c.equipe(m[1]):
        n = 1.0 if m[2] == "un" else float(m[3])
        return [_jambe("joueur", joueur=m[1].strip(), stat="Goals", sens="plus", ligne=n - 0.5, periode=_periode(t))]
    m = re.fullmatch(rf"(.+?) marque (?:au moins )?(?:un|1) but(?: en (?:1ere|1re|2eme|2e) mi-temps)?", t)
    if m and not c.equipe(m[1]):
        return [_jambe("joueur", joueur=m[1].strip(), stat="Goals", sens="plus", ligne=0.5, periode=_periode(t))]
    m = re.fullmatch(rf"(.+?) (?:marque|marquent) (?:au moins )?{NB}\+? ?(?:pts|points)(?: ou \+| ou plus)?( chacun)?", t)
    if m:
        noms = [x.strip() for x in re.split(r" et | \+ ", m[1])]
        if any(c.equipe(n) for n in noms):
            return None
        ligne = float(m[2]) - 0.5
        if len(noms) == 1:
            return [_jambe("joueur", joueur=noms[0], stat="Points", sens="plus", ligne=ligne)]
        if m[3] or " et " in m[1]:
            return [_jambe("joueur", joueur=n, stat="Points", sens="plus", ligne=ligne) for n in noms]
        return [_jambe("joueur", joueurs=noms, mode="somme", stat="Points", sens="plus", ligne=ligne)]
    m = re.fullmatch(r"(.+?) realise une performance ((?:points|rebonds|passes decisives|passes)"
                     rf"(?: \+ (?:points|rebonds|passes decisives|passes))*) d'au moins {NB}", t)
    if m:
        stats = "+".join(STATS[s.strip()] for s in m[2].split("+"))
        return [_jambe("joueur", joueur=m[1].strip(), stat=stats, sens="plus", ligne=float(m[3]) - 0.5)]
    return None


def analyser(pari: str, match: str, sport_bookmaker: str) -> list[dict] | None:
    """Jambes du pari, ou None si une partie n'est pas reconnue."""
    sport = SPORTS.get(sport_bookmaker)
    if not sport or not pari or " - " not in str(match or ""):
        return None
    e1, _, e2 = str(match).partition(" - ")
    brut = _norm(pari)
    if "titulaire" in brut or "rembours" in brut or "premier buteur" in brut:
        return None          # règles de remboursement particulières : jamais devinées
    c = _Ctx(sport, (e1.strip(), e2.strip()), brut)
    direct = _clause(brut, c)
    if direct:
        return direct
    parties = [p.strip() for p in re.split(r" et |, | & ", brut)]
    if len(parties) < 2:
        return None
    legs = []
    for p in parties:
        r = _clause(p, c)
        if not r:
            return None
        legs += r
    return legs
