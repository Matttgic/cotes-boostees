"""Recherche d'un résultat réel pour un boost, avec archive de tout ce qui est trouvé.

Pour chaque boost : jambes -> match (équipes, date) -> première source qui le connaît et le donne terminé ->
confirmation par une seconde source (scores identiques) -> détails (buteurs, stats) si le pari les demande.

Archive `resultats.json` (branche donnees), conservée pour les prochains boosts :
- `evenements` : chaque match retrouvé, avec score, mi-temps, buteurs, stats et sources ;
- `sources` : fiabilité de chaque source (succès, échecs, dernière erreur) ;
- `ligues` : quelle source a servi pour quelle ligue (l'ordre d'essai s'en inspire ensuite) ;
- `sans_correspondance` : matchs jamais retrouvés (noms à ajouter à scores/noms.py:ALIAS).
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from ..acces import masquer
from .noms import equipe_proche, joueur_proche, normaliser
from .sources import ORDRE, ORDRE_DEFAUT, SOURCES, SPORTS

ECART_MAX_H = 14
TENNIS = ("tennis", "tennis_table", "badminton")


def archive_vide() -> dict:
    return {"evenements": {}, "sources": {}, "ligues": {}, "sans_correspondance": {}}


class Lecteur:
    """Lecture JSON : directe pour les API publiques, par le proxy français pour les autres."""

    def __init__(self, nav=None):
        self.nav = nav
        self.requetes = 0
        self.derniere_erreur: dict[str, str] = {}

    def __call__(self, url: str, proxy: bool = False):
        from curl_cffi import requests as creq
        self.requetes += 1
        hote = url.split("/")[2]
        kw = {"impersonate": "chrome", "timeout": 40}
        if proxy and self.nav is not None:
            kw.update(proxies=self.nav.proxies, verify=self.nav.verif)
        try:
            r = creq.get(url, **kw)
            if proxy and self.nav is not None:
                self.nav.octets += len(r.content)
            if r.status_code != 200:
                self.derniere_erreur[hote] = f"HTTP {r.status_code}"
                return None
            return r.json()
        except Exception as e:
            self.derniere_erreur[hote] = masquer(f"{type(e).__name__} : {e}")[:200]
            return None


def _dt(s: str | None) -> datetime | None:
    if not s:
        return None
    d = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def equipes_du_boost(b: dict) -> tuple[str, str] | None:
    for j in b.get("jambes") or []:
        if j.get("equipe_1") and j.get("equipe_2"):
            return j["equipe_1"], j["equipe_2"]
    m = str(b.get("match") or "")
    if " - " in m:
        a, _, c = m.partition(" - ")
        return a.strip(), c.strip()
    return None


class Recherche:
    def __init__(self, archive: dict, lire, maintenant: datetime | None = None):
        self.archive = archive
        for k, v in archive_vide().items():
            archive.setdefault(k, v)
        self.lire = lire
        self.t = maintenant or datetime.now(timezone.utc)
        self.jours: dict[tuple, list[dict]] = {}

    # ------------------------------------------------------------------ journées
    def jour(self, source: str, sport: str, date: str) -> list[dict]:
        cle = (source, sport, date)
        if cle in self.jours:
            return self.jours[cle]
        st = self.archive["sources"].setdefault(source, {"ok": 0, "vides": 0, "echecs": 0})
        try:
            lst = SOURCES["jour"][source](self.lire, sport, date)
        except Exception as e:            # une source qui change son format ne casse rien
            lst = []
            st["echecs"] += 1
            st["derniere_erreur"] = f"{type(e).__name__} : {e}"[:200]
        else:
            if lst:
                st["ok"] += 1
                st["dernier_succes"] = self.t.isoformat(timespec="seconds")
            else:
                st["vides"] += 1
        self.jours[cle] = lst
        return lst

    @staticmethod
    def _trouver(lst: list[dict], e1: str, e2: str, debut: datetime | None, sport: str) -> dict | None:
        proche = joueur_proche if sport in TENNIS else equipe_proche
        ok = []
        for r in lst:
            if not ((proche(r["equipe_1"], e1) and proche(r["equipe_2"], e2))
                    or (proche(r["equipe_1"], e2) and proche(r["equipe_2"], e1))):
                continue
            d = _dt(r.get("debut"))
            if debut and d and abs(d - debut) > timedelta(hours=ECART_MAX_H):
                continue
            ok.append(r)
        return ok[0] if len(ok) == 1 else None      # plusieurs candidats (double rencontre) : on s'abstient

    def _dates(self, debut: datetime) -> list[str]:
        d = debut.date()
        return [x.isoformat() for x in (d, d - timedelta(days=1), d + timedelta(days=1))]

    def _ordre(self, sport: str, ligue: str) -> list[str]:
        base = list(ORDRE.get(sport, ORDRE_DEFAUT))
        appris = self.archive["ligues"].get(ligue or "", {})
        return sorted(base, key=lambda s: (-appris.get(s, 0), base.index(s)))

    # ------------------------------------------------------------------- recherche
    def chercher(self, b: dict, details: bool = False) -> dict | None:
        """Résultat archivé ou nouvellement lu, ou None. Ne modifie pas le boost."""
        sport = SPORTS.get(b.get("sport"))
        eq, debut = equipes_du_boost(b), _dt(b.get("debut"))
        if not (sport and eq and debut):
            return None
        e1, e2 = eq
        cle = f"{sport}|{debut.date()}|{normaliser(e1)}|{normaliser(e2)}"
        r = self.archive["evenements"].get(cle)
        if r is None:
            r = self._lire(sport, e1, e2, debut, b.get("ligue", ""))
            if r is None:
                sc = self.archive["sans_correspondance"].setdefault(
                    cle, {"match": b.get("match"), "sport": b.get("sport"), "ligue": b.get("ligue"), "essais": 0})
                sc["essais"] += 1
                sc["derniere"] = self.t.isoformat(timespec="seconds")
                return None
            self.archive["sans_correspondance"].pop(cle, None)
            self.archive["evenements"][cle] = r
        if (details and r["statut"] == "termine" and r.get("details_essais", 0) < 3
                and (r.get("buteurs") is None or r.get("joueurs") is None)):
            r["details_essais"] = r.get("details_essais", 0) + 1
            self._enrichir(r, sport, e1, e2, debut)
        return r

    def _lire(self, sport, e1, e2, debut, ligue) -> dict | None:
        trouve = None
        autres = []
        for source in self._ordre(sport, ligue):
            for date in self._dates(debut):
                r = self._trouver(self.jour(source, sport, date), e1, e2, debut, sport)
                if r is None:
                    continue
                if trouve is None:
                    trouve = dict(r)
                    trouve["recupere_le"] = self.t.isoformat(timespec="seconds")
                    trouve["confirme_par"], trouve["conflit"] = [], False
                    self.archive["ligues"].setdefault(ligue or "", {}).setdefault(source, 0)
                    self.archive["ligues"][ligue or ""][source] += 1
                elif r["statut"] == "termine" and trouve["statut"] == "termine":
                    autres.append((source, r))
                break
            if trouve is not None and trouve["statut"] != "termine":
                break
        for source, r in autres:
            if r["score"] and trouve["score"] and sorted(r["score"]) == sorted(trouve["score"]):
                trouve["confirme_par"].append(source)
            else:
                trouve["conflit"] = True
        return trouve

    def _enrichir(self, r: dict, sport: str, e1: str, e2: str, debut: datetime) -> None:
        """Complète buteurs et stats : la source du résultat d'abord, puis les autres qui savent le faire."""
        for source in [r["source"]] + [s for s in SOURCES["details"] if s != r["source"]]:
            if source not in SOURCES["details"]:
                continue
            cible = r if source == r["source"] else None
            if cible is None:
                for date in self._dates(debut):
                    cible = self._trouver(self.jour(source, sport, date), e1, e2, debut, sport)
                    if cible is not None:
                        break
            if cible is None:
                continue
            try:
                SOURCES["details"][source](self.lire, cible)
            except Exception as e:
                self.archive["sources"].setdefault(source, {})["derniere_erreur"] = f"{type(e).__name__} : {e}"[:200]
                continue
            for k in ("buteurs", "joueurs"):
                if r.get(k) is None and cible.get(k) is not None:
                    r[k] = cible[k]
            if r.get("buteurs") is not None and r.get("joueurs") is not None:
                return
