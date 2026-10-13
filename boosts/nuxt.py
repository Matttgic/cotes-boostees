"""Lecture de l'état Nuxt (`window.__NUXT__=(function(a,b,…){return {…}}(v1,v2,…))`) SANS exécuter de JavaScript.

Les sites Sportnco (Genybet, NetBet) rendent leur page côté serveur et y joignent leur état sous cette forme :
une fonction dont les paramètres servent d'abréviations pour les valeurs répétées, précédée d'affectations
(« eT.header={…}; ») qui complètent les objets passés en argument. On analyse le littéral
(objets, tableaux, chaînes, nombres, true/false/null, void 0, Array(n), noms de paramètres) puis on
remplace chaque paramètre par sa valeur. Toute autre construction JavaScript lève une erreur.
"""
from __future__ import annotations

import json
import re

RE_SCRIPT = re.compile(r"<script[^>]*>\s*window\.__NUXT__\s*=\s*(.*?);?\s*</script>", re.S)
RE_NOMBRE = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?")
RE_NOM = re.compile(r"[A-Za-z_$][\w$]*")


class EtatIllisible(ValueError):
    pass


class _Ref:
    __slots__ = ("nom",)

    def __init__(self, nom: str):
        self.nom = nom


class _Lecteur:
    def __init__(self, s: str):
        self.s, self.i = s, 0

    def blancs(self) -> None:
        while self.i < len(self.s) and self.s[self.i] in " \t\r\n":
            self.i += 1

    def voir(self, texte: str) -> bool:
        self.blancs()
        return self.s.startswith(texte, self.i)

    def lire(self, texte: str) -> None:
        if not self.voir(texte):
            raise EtatIllisible(f"« {texte} » attendu à la position {self.i} : {self.s[self.i:self.i + 40]!r}")
        self.i += len(texte)

    def chaine(self) -> str:
        q = self.s[self.i]
        j = self.i + 1
        while j < len(self.s) and self.s[j] != q:
            j += 2 if self.s[j] == "\\" else 1
        brut = self.s[self.i + 1:j]
        self.i = j + 1
        if q == "'":
            brut = brut.replace("\\'", "'").replace('"', '\\"')
        return json.loads(f'"{brut}"')

    def valeur(self):
        self.blancs()
        c = self.s[self.i:self.i + 1]
        if c == "{":
            self.i += 1
            out = {}
            while not self.voir("}"):
                self.blancs()
                if self.s[self.i] in "\"'":
                    cle = self.chaine()
                else:
                    m = RE_NOM.match(self.s, self.i) or RE_NOMBRE.match(self.s, self.i)
                    if not m:
                        raise EtatIllisible(f"clé illisible à la position {self.i}")
                    cle, self.i = m.group(0), m.end()
                self.lire(":")
                out[cle] = self.valeur()
                if not self.voir("}"):
                    self.lire(",")
            self.lire("}")
            return out
        if c == "[":
            self.i += 1
            out = []
            while not self.voir("]"):
                out.append(self.valeur())
                if not self.voir("]"):
                    self.lire(",")
            self.lire("]")
            return out
        if c in "\"'":
            return self.chaine()
        m = RE_NOMBRE.match(self.s, self.i)
        if m:
            self.i = m.end()
            t = m.group(0)
            return float(t) if any(x in t for x in ".eE") else int(t)
        if self.voir("void 0"):
            self.i += 6
            return None
        m = RE_NOM.match(self.s, self.i)
        if not m:
            raise EtatIllisible(f"valeur illisible à la position {self.i} : {self.s[self.i:self.i + 40]!r}")
        nom, self.i = m.group(0), m.end()
        if nom == "Array" and self.voir("("):
            self.lire("(")
            n = self.valeur()
            self.lire(")")
            return [None] * int(n)
        return {"true": True, "false": False, "null": None, "undefined": None}.get(nom, _Ref(nom)) \
            if nom in ("true", "false", "null", "undefined") else _Ref(nom)


def _resoudre(v, valeurs: dict):
    if isinstance(v, _Ref):
        if v.nom not in valeurs:
            raise EtatIllisible(f"nom inconnu : {v.nom}")
        return valeurs[v.nom]
    if isinstance(v, dict):
        return {k: _resoudre(x, valeurs) for k, x in v.items()}
    if isinstance(v, list):
        return [_resoudre(x, valeurs) for x in v]
    return v


def etat(html: str) -> dict:
    m = RE_SCRIPT.search(html)
    if not m:
        raise EtatIllisible("window.__NUXT__ absent (page de blocage ou site modifié)")
    lec = _Lecteur(m.group(1).strip())
    if not lec.voir("(function"):                       # état littéral simple
        return _resoudre(lec.valeur(), {})
    lec.lire("(function")
    lec.lire("(")
    params = []
    while not lec.voir(")"):
        lec.blancs()
        p = RE_NOM.match(lec.s, lec.i)
        if not p:
            raise EtatIllisible("paramètres illisibles")
        params.append(p.group(0))
        lec.i = p.end()
        if not lec.voir(")"):
            lec.lire(",")
    lec.lire(")")
    lec.lire("{")
    # affectations éventuelles avant le « return » : « eT.header={…};eX[0]=…; »
    affectations = []
    while not lec.voir("return"):
        lec.blancs()
        m = RE_NOM.match(lec.s, lec.i)
        if not m:
            raise EtatIllisible(f"instruction illisible à la position {lec.i}")
        lec.i = m.end()
        chemin: list = [m.group(0)]
        while True:
            if lec.voir("."):
                lec.lire(".")
                p = RE_NOM.match(lec.s, lec.i)
                if not p:
                    raise EtatIllisible(f"propriété illisible à la position {lec.i}")
                chemin.append(p.group(0))
                lec.i = p.end()
            elif lec.voir("["):
                lec.lire("[")
                chemin.append(lec.valeur())
                lec.lire("]")
            else:
                break
        lec.lire("=")
        affectations.append((chemin, lec.valeur()))
        if lec.voir(";"):
            lec.lire(";")
    lec.lire("return")
    corps = lec.valeur()
    lec.lire("}")
    lec.lire("(")
    args = []
    while not lec.voir(")"):
        args.append(lec.valeur())
        if not lec.voir(")"):
            lec.lire(",")
    lec.lire(")")
    valeurs = {p: (args[k] if k < len(args) else None) for k, p in enumerate(params)}
    for chemin, v in affectations:            # dans l'ordre, sur les objets passés en argument (même identité)
        if len(chemin) < 2 or chemin[0] not in valeurs:
            raise EtatIllisible(f"affectation non prise en charge : {chemin}")
        cible = valeurs[chemin[0]]
        for cle in chemin[1:-1]:
            cible = cible[cle] if isinstance(cible, list) else cible.setdefault(cle, {})
        cle = chemin[-1]
        if isinstance(cible, list):
            while len(cible) <= int(cle):
                cible.append(None)
            cible[int(cle)] = _resoudre(v, valeurs)
        else:
            cible[str(cle)] = _resoudre(v, valeurs)
    return _resoudre(corps, valeurs)
