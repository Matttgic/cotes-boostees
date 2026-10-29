"""Lecteurs de résultats : SofaScore, ESPN, API officielle de la NHL, LiveScore.

Chaque source expose :
- `jour_*(lire, sport, date)` -> liste de résultats d'une journée ;
- `details_*(lire, resultat)` -> complète buteurs / stats de joueurs (appel séparé, seulement si le pari le demande).
`lire(url, proxy=False)` renvoie le JSON décodé ou None (voir recherche.py). Les analyseurs `lire_*` sont des
fonctions pures (JSON -> dict), testées sur des réponses types.

Résultat normalisé :
  source, id, sport, ligue, debut (ISO UTC), equipe_1, equipe_2 (domicile, extérieur), statut
  (« termine » | « annule » | « autre »), score [d, e] (score final, prolongations comprises ; tennis : sets),
  score_reglementaire [d, e] | None (football : 90 min ; hockey : 3 tiers-temps), mi_temps [d, e] | None,
  periodes [[d, e], ...] | None (quarts-temps, tiers-temps ; tennis : jeux par set),
  buteurs [{joueur, equipe (1|2), minute, csc}] | None,
  joueurs {nom: {equipe, a_joue, stats{Points, Rebounds, Assists, Goals}}} | None.
"""
from __future__ import annotations

from datetime import datetime, timezone

SPORTS = {   # nom du bookmaker -> clé interne
    "Football": "football", "Basketball": "basketball", "Hockey sur glace": "hockey", "Tennis": "tennis",
    "Baseball": "baseball", "Football Américain": "football_us", "Foot américain": "football_us",
    "Rugby": "rugby", "Rugby à XV": "rugby", "Rugby à XIII": "rugby", "Handball": "handball",
    "Tennis de table": "tennis_table", "Badminton": "badminton",
}
SOFASCORE_SPORT = {"football": "football", "basketball": "basketball", "hockey": "ice-hockey", "tennis": "tennis",
                   "baseball": "baseball", "football_us": "american-football", "rugby": "rugby",
                   "handball": "handball", "tennis_table": "table-tennis", "badminton": "badminton"}
LIVESCORE_SPORT = {"football": "soccer", "basketball": "basketball", "hockey": "hockey", "tennis": "tennis"}
ESPN_LIGUES = {
    "football": [("soccer", s) for s in ("fra.1", "eng.1", "esp.1", "ger.1", "ita.1", "uefa.champions", "uefa.europa",
                                          "uefa.europa.conf", "por.1", "ned.1", "tur.1", "bel.1", "fra.2", "eng.2",
                                          "sco.1", "usa.1")],
    "basketball": [("basketball", "nba"), ("basketball", "wnba")],
    "hockey": [("hockey", "nhl")],
    "football_us": [("football", "nfl"), ("football", "college-football")],
    "baseball": [("baseball", "mlb")],
}
FINIS_LIVESCORE = {"FT", "AET", "AP", "AOT", "Final"}


def _entier(v):
    try:
        return int(float(v))
    except (TypeError, ValueError):
        return None


def _iso(ts: int | float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).isoformat(timespec="seconds")


def _vide(source: str, sport: str) -> dict:
    return {"source": source, "sport": sport, "ligue": "", "id": None, "debut": None, "equipe_1": "", "equipe_2": "",
            "statut": "autre", "score": None, "score_reglementaire": None, "mi_temps": None, "periodes": None,
            "buteurs": None, "joueurs": None}


# ------------------------------------------------------------------ SofaScore
def lire_sofascore_jour(data: dict, sport: str) -> list[dict]:
    out = []
    for e in (data or {}).get("events") or []:
        r = _vide("sofascore", sport)
        r["id"] = e.get("id")
        r["ligue"] = (e.get("tournament") or {}).get("name", "")
        r["equipe_1"] = (e.get("homeTeam") or {}).get("name", "")
        r["equipe_2"] = (e.get("awayTeam") or {}).get("name", "")
        if e.get("startTimestamp"):
            r["debut"] = _iso(e["startTimestamp"])
        st = e.get("status") or {}
        t = st.get("type", "")
        r["statut"] = "termine" if t == "finished" else "annule" if t in ("canceled", "cancelled") else "autre"
        if r["statut"] == "termine" and any(m in str(st.get("description", "")).lower()
                                            for m in ("retire", "walkover", "w.o", "abandon", "default")):
            r["statut"] = "autre"      # abandon : les règles de chaque bookmaker diffèrent, pas de règlement automatique
        h, a = e.get("homeScore") or {}, e.get("awayScore") or {}
        if r["statut"] == "termine" and h.get("current") is not None and a.get("current") is not None:
            r["score"] = [h["current"], a["current"]]
            par = [(h.get(f"period{i}"), a.get(f"period{i}")) for i in range(1, 8)]
            par = [[x, y] for x, y in par if x is not None and y is not None]
            r["periodes"] = par or None
            if sport in ("football", "handball", "rugby"):
                nt_h, nt_a = h.get("normaltime"), a.get("normaltime")
                r["score_reglementaire"] = [nt_h, nt_a] if nt_h is not None and nt_a is not None else r["score"]
                if par:
                    r["mi_temps"] = par[0]
            elif sport == "hockey" and len(par) >= 3:
                r["score_reglementaire"] = [sum(p[0] for p in par[:3]), sum(p[1] for p in par[:3])]
        out.append(r)
    return out


def lire_sofascore_incidents(data: dict) -> list[dict]:
    buteurs = []
    for i in (data or {}).get("incidents") or []:
        if i.get("incidentType") != "goal":
            continue
        classe = str(i.get("incidentClass") or "")
        buteurs.append({"joueur": (i.get("player") or {}).get("name", ""), "equipe": 1 if i.get("isHome") else 2,
                        "minute": _entier(i.get("time")), "csc": classe == "ownGoal"})
    return buteurs


def lire_sofascore_compos(data: dict) -> dict:
    joueurs = {}
    for cote, equipe in (("home", 1), ("away", 2)):
        for p in ((data or {}).get(cote) or {}).get("players") or []:
            nom = (p.get("player") or {}).get("name")
            st = p.get("statistics") or {}
            if not nom or not st:
                continue
            minutes = st.get("minutesPlayed") or st.get("secondsPlayed")
            stats = {"Points": st.get("points"), "Rebounds": st.get("rebounds"), "Assists": st.get("assists"),
                     "Goals": st.get("goals")}
            joueurs[nom] = {"equipe": equipe, "a_joue": bool(minutes), "stats": {k: v for k, v in stats.items() if v is not None}}
    return joueurs


def jour_sofascore(lire, sport: str, date: str) -> list[dict]:
    slug = SOFASCORE_SPORT.get(sport)
    if not slug:
        return []
    return lire_sofascore_jour(lire(f"https://api.sofascore.com/api/v1/sport/{slug}/scheduled-events/{date}", True),
                               sport)


def details_sofascore(lire, r: dict) -> None:
    if r.get("id") is None:
        return
    inc = lire(f"https://api.sofascore.com/api/v1/event/{r['id']}/incidents", True)
    if inc is not None and r["sport"] in ("football", "hockey", "handball", "rugby"):
        r["buteurs"] = lire_sofascore_incidents(inc)
    compos = lire(f"https://api.sofascore.com/api/v1/event/{r['id']}/lineups", True)
    if compos is not None:
        r["joueurs"] = lire_sofascore_compos(compos) or None


# ----------------------------------------------------------------------- ESPN
def lire_espn_jour(data: dict, sport: str, ligue: str = "") -> list[dict]:
    out = []
    for ev in (data or {}).get("events") or []:
        comp = (ev.get("competitions") or [{}])[0]
        cs = {c.get("homeAway"): c for c in comp.get("competitors") or []}
        if "home" not in cs or "away" not in cs:
            continue
        r = _vide("espn", sport)
        r["id"], r["ligue"] = ev.get("id"), ligue
        r["debut"] = (ev.get("date") or "").replace("Z", "+00:00") or None
        r["equipe_1"] = (cs["home"].get("team") or {}).get("displayName", "")
        r["equipe_2"] = (cs["away"].get("team") or {}).get("displayName", "")
        t = ((ev.get("status") or {}).get("type")) or {}
        r["statut"] = "termine" if t.get("completed") else "annule" if t.get("name") in ("STATUS_CANCELED", "STATUS_POSTPONED") else "autre"
        sh, sa = _entier(cs["home"].get("score")), _entier(cs["away"].get("score"))
        if r["statut"] == "termine" and sh is not None and sa is not None:
            r["score"] = [sh, sa]
            lh = [_entier(x.get("value")) for x in cs["home"].get("linescores") or []]
            la = [_entier(x.get("value")) for x in cs["away"].get("linescores") or []]
            if lh and len(lh) == len(la) and None not in lh + la:
                r["periodes"] = [[x, y] for x, y in zip(lh, la)]
                if sport == "football" and len(lh) == 2:
                    r["mi_temps"] = r["periodes"][0]
                    r["score_reglementaire"] = r["score"]
                elif sport == "hockey" and len(lh) >= 3:
                    r["score_reglementaire"] = [sum(lh[:3]), sum(la[:3])]
            elif sport == "football":
                r["score_reglementaire"] = r["score"]
        ids = {str((c.get("team") or {}).get("id")): (1 if k == "home" else 2) for k, c in cs.items()}
        buteurs = []
        for d in comp.get("details") or []:
            if not d.get("scoringPlay"):
                continue
            joueurs = d.get("athletesInvolved") or []
            texte = str((d.get("type") or {}).get("text", "")).lower()
            buteurs.append({"joueur": (joueurs[0] or {}).get("displayName", "") if joueurs else "",
                            "equipe": ids.get(str((d.get("team") or {}).get("id"))),
                            "minute": _entier(str((d.get("clock") or {}).get("displayValue", "")).split("'")[0].split("+")[0]),
                            "csc": "own" in texte})
        if buteurs and r["statut"] == "termine":
            r["buteurs"] = buteurs
        out.append(r)
    return out


def lire_espn_resume(data: dict) -> dict:
    """Stats de joueurs (basket : PTS, REB, AST) et présents (football : titulaires et remplaçants entrés)."""
    joueurs = {}
    ids = {}
    for eq in ((data or {}).get("boxscore") or {}).get("players") or []:
        ids[str((eq.get("team") or {}).get("id"))] = len(ids) + 1
    for i, eq in enumerate(((data or {}).get("boxscore") or {}).get("players") or [], start=1):
        for bloc in eq.get("statistics") or []:
            labels = bloc.get("labels") or []
            for a in bloc.get("athletes") or []:
                nom = (a.get("athlete") or {}).get("displayName")
                stats = a.get("stats") or []
                if not nom or not stats or a.get("didNotPlay"):
                    continue
                cle = {"PTS": "Points", "REB": "Rebounds", "AST": "Assists"}
                s = {cle[l]: _entier(v) for l, v in zip(labels, stats) if l in cle and _entier(v) is not None}
                joueurs[nom] = {"equipe": i, "a_joue": True, "stats": s}
    for eq in (data or {}).get("rosters") or []:
        cote = 1 if eq.get("homeAway") == "home" else 2
        for p in eq.get("roster") or []:
            nom = (p.get("athlete") or {}).get("displayName")
            if nom and nom not in joueurs:
                joueurs[nom] = {"equipe": cote, "a_joue": bool(p.get("starter") or p.get("subbedIn")), "stats": {}}
    return joueurs


def jour_espn(lire, sport: str, date: str) -> list[dict]:
    out = []
    jour = date.replace("-", "")
    for cat, slug in ESPN_LIGUES.get(sport, []):
        data = lire(f"https://site.api.espn.com/apis/site/v2/sports/{cat}/{slug}/scoreboard?dates={jour}", False)
        for r in lire_espn_jour(data, sport, slug):
            r["cat"] = cat
            out.append(r)
    return out


def details_espn(lire, r: dict) -> None:
    if r.get("id") is None or not r.get("cat") or not r.get("ligue"):
        return
    data = lire(f"https://site.api.espn.com/apis/site/v2/sports/{r['cat']}/{r['ligue']}/summary?event={r['id']}", False)
    if data is not None:
        r["joueurs"] = lire_espn_resume(data) or None


# ------------------------------------------------------------------------ NHL
def lire_nhl_jour(data: dict) -> list[dict]:
    def nom(v):
        return v.get("default", "") if isinstance(v, dict) else str(v or "")

    out = []
    for g in (data or {}).get("games") or []:
        dom, ext = g.get("homeTeam") or {}, g.get("awayTeam") or {}
        r = _vide("nhl", "hockey")
        r["id"], r["ligue"], r["debut"] = g.get("id"), "NHL", g.get("startTimeUTC")
        r["equipe_1"] = (nom(dom.get("placeName")) + " " + nom(dom.get("name"))).strip()
        r["equipe_2"] = (nom(ext.get("placeName")) + " " + nom(ext.get("name"))).strip()
        fini = g.get("gameState") in ("OFF", "FINAL")
        r["statut"] = "termine" if fini else "autre"
        if fini and dom.get("score") is not None and ext.get("score") is not None:
            r["score"] = [dom["score"], ext["score"]]
            fin = ((g.get("gameOutcome") or {}).get("lastPeriodType")) or ((g.get("periodDescriptor") or {}).get("periodType"))
            if fin == "REG":
                r["score_reglementaire"] = r["score"]
            elif fin in ("OT", "SO"):
                m = min(r["score"])
                r["score_reglementaire"] = [m, m]
            ab_dom, ab_ext = dom.get("abbrev"), ext.get("abbrev")
            buteurs, par = [], {}
            for b in g.get("goals") or []:
                ab = nom(b.get("teamAbbrev"))
                eq = 1 if ab == ab_dom else 2 if ab == ab_ext else None
                nm = nom(b.get("name")) or (nom(b.get("firstName")) + " " + nom(b.get("lastName"))).strip()
                buteurs.append({"joueur": nm, "equipe": eq, "minute": None, "csc": False})
                p = int(b.get("period") or 0)
                if eq and p:
                    par.setdefault(p, [0, 0])[eq - 1] += 1
            if buteurs:
                r["buteurs"] = buteurs
            if par and sum(r["score"]) == len(buteurs):
                r["periodes"] = [par.get(i, [0, 0]) for i in range(1, max(par) + 1)]
        out.append(r)
    return out


def jour_nhl(lire, sport: str, date: str) -> list[dict]:
    return lire_nhl_jour(lire(f"https://api-web.nhle.com/v1/score/{date}", False)) if sport == "hockey" else []


# ------------------------------------------------------------------- LiveScore
def lire_livescore_jour(data: dict, sport: str) -> list[dict]:
    out = []
    for st in (data or {}).get("Stages") or []:
        for e in st.get("Events") or []:
            t1, t2 = (e.get("T1") or [{}])[0], (e.get("T2") or [{}])[0]
            r = _vide("livescore", sport)
            r["id"], r["ligue"] = e.get("Eid"), st.get("Snm", "")
            r["equipe_1"], r["equipe_2"] = t1.get("Nm", ""), t2.get("Nm", "")
            esd = str(e.get("Esd") or "")
            if len(esd) >= 12:
                r["debut"] = f"{esd[:4]}-{esd[4:6]}-{esd[6:8]}T{esd[8:10]}:{esd[10:12]}:00+00:00"
            eps = e.get("Eps")
            h, a = _entier(e.get("Tr1")), _entier(e.get("Tr2"))
            if eps in FINIS_LIVESCORE and h is not None and a is not None:
                r["statut"], r["score"] = "termine", [h, a]
                if sport == "football" and eps == "FT":
                    r["score_reglementaire"] = r["score"]
                    mh, ma = _entier(e.get("Trh1")), _entier(e.get("Trh2"))
                    if mh is not None and ma is not None:
                        r["mi_temps"] = [mh, ma]
            elif eps in ("Canc", "Postp", "Aband"):
                r["statut"] = "annule"
            out.append(r)
    return out


def jour_livescore(lire, sport: str, date: str) -> list[dict]:
    slug = LIVESCORE_SPORT.get(sport)
    if not slug:
        return []
    url = f"https://prod-cdn-public-api.livescore.com/v1/api/app/date/{slug}/{date.replace('-', '')}/0"
    return lire_livescore_jour(lire(url, True), sport)


# Ordre d'essai par sport : sources officielles/gratuites d'abord, puis couverture large.
SOURCES = {
    "jour": {"nhl": jour_nhl, "espn": jour_espn, "sofascore": jour_sofascore, "livescore": jour_livescore},
    "details": {"sofascore": details_sofascore, "espn": details_espn},
}
ORDRE = {
    "football": ("espn", "sofascore", "livescore"),
    "basketball": ("espn", "sofascore", "livescore"),
    "hockey": ("nhl", "espn", "sofascore", "livescore"),
    "tennis": ("sofascore", "livescore"),
    "baseball": ("espn", "sofascore"),
    "football_us": ("espn", "sofascore"),
}
ORDRE_DEFAUT = ("sofascore",)
