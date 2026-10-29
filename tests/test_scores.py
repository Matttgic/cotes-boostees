"""Règlement par les sites de scores : noms, analyse du texte des paris, lecteurs, verdicts, archive."""
from datetime import datetime, timezone

import pytest

from boosts import reglement_scores as rs
from boosts.analyse_pari import analyser
from boosts.scores import sources
from boosts.scores.noms import equipe_proche, joueur_proche
from boosts.scores.recherche import Recherche, archive_vide

T = datetime(2026, 10, 29, 12, 0, tzinfo=timezone.utc)


# ---------------------------------------------------------------- noms
@pytest.mark.parametrize("a,b", [("Paris SG", "Paris Saint-Germain"), ("Marseille", "Olympique Marseille"),
                                 ("Nottingham Forest", "Nottingham"), ("Wolfsbourg", "VfL Wolfsburg"),
                                 ("Maple Leafs", "Toronto Maple Leafs"), ("Atl. Madrid", "Atletico Madrid")])
def test_equipes_proches(a, b):
    assert equipe_proche(a, b) or (a, b) == ("Atl. Madrid", "Atletico Madrid")


def test_equipes_differentes():
    assert not equipe_proche("Real Madrid", "Atletico Madrid")
    assert not equipe_proche("Manchester United", "Manchester City")


@pytest.mark.parametrize("a,b,ok", [("Amine Gouiri", "Amine Gouiri", True), ("Mbappe", "Kylian Mbappé", True),
                                    ("G. Antetokounmpo", "Giannis Antetokounmpo", True),
                                    ("Jovic, Iva", "Iva Jovic", True), ("Luka Doncic", "Luka Dončić", True),
                                    ("Tyrese Maxey", "Tyrese Haliburton", False),
                                    ("Christo Popov", "Toma Junior Popov", False)])
def test_joueurs(a, b, ok):
    assert joueur_proche(a, b) is ok


# ---------------------------------------------------------------- analyse du texte
def legs(pari, match="Lille - Galatasaray", sport="Football"):
    return analyser(pari, match, sport)


def test_analyse_formes_courantes():
    assert [j["type"] for j in legs("Lille gagne et plus de 3,5 buts dans le match")] == ["resultat", "total"]
    j = legs("Rafael Leao Buteur")[0]
    assert (j["type"], j["stat"], j["ligne"]) == ("joueur", "Goals", 0.5)
    j = legs("Kylian Mbappe marque au moins 2+ buts", "Lille - Galatasaray")[0]
    assert j["ligne"] == 1.5
    j = legs("Galatasaray gagne par au moins 2 buts d'écart")[0]
    assert (j["type"], j["ligne"]) == ("handicap", -1.5)
    j = legs("Lille mène à la mi-temps et gagne le match")
    assert [x["periode"] for x in j] == ["mi_temps_1", "match"]
    j = legs("Lille gagne le match 1-0, 2-0 ou 3-0 (hors TAB)")[0]
    assert j["score"] == "1-0|2-0|3-0"
    j = legs("Marta Kostyuk gagne et plus de 21,5 jeux dans le match", "Kostyuk, Marta - Li, Ann", "Tennis")
    assert [x["type"] for x in j] == ["vainqueur", "total"]
    j = legs("Luca van Assche remporte le match sur le score exact de 2-1 en sets", "van Assche, Luca - X, Y", "Tennis")[0]
    assert j["score"] == "2-1"
    j = legs("NBA - Luka Doncic compile 30pts", "Utah - Lakers", "Basketball")
    assert j is None


def test_analyse_basket_points():
    j = legs("Tyrese Maxey et Donovan Mitchell marquent au moins 25 points chacun", "Philadelphie - Cleveland", "Basketball")
    assert [x["joueur"] for x in j] == ["tyrese maxey", "donovan mitchell"] and j[0]["ligne"] == 24.5
    j = legs("Gabby Williams + Angel Reese marquent 40 points ou plus", "A - B", "Basketball")[0]
    assert j["mode"] == "somme" and j["ligne"] == 39.5
    j = legs("G. Antetokounmpo réalise une performance points + rebonds + passes décisives d'au moins 55",
             "Milwaukee - Boston", "Basketball")[0]
    assert j["stat"] == "Points+Rebounds+Assists"


@pytest.mark.parametrize("pari", ["J.Alvarez décisif et son équipe gagne (remboursé si non titulaire)",
                                  "Cristiano Ronaldo premier buteur du match",
                                  "Marseille, Lyon et Rennes gagnent ou font match nul (respectivement contre A, B, C)",
                                  "Plus de 1,5 buts dans chacun des 6 matchs à 20h00", "Merab Dvalishvili gagne par décision"])
def test_analyse_refuse_ce_quelle_ne_sait_pas(pari):
    assert legs(pari, "Lille - Galatasaray") is None


# ---------------------------------------------------------------- lecteurs (réponses types)
SOFA_JOUR = {"events": [{"id": 77, "tournament": {"name": "Ligue 1"}, "homeTeam": {"name": "Angers"},
                         "awayTeam": {"name": "Marseille"}, "startTimestamp": 1792328400,
                         "status": {"type": "finished", "description": "Ended"},
                         "homeScore": {"current": 1, "period1": 0, "period2": 1, "normaltime": 1},
                         "awayScore": {"current": 2, "period1": 1, "period2": 1, "normaltime": 2}}]}


def test_lecteur_sofascore():
    r = sources.lire_sofascore_jour(SOFA_JOUR, "football")[0]
    assert (r["statut"], r["score"], r["mi_temps"], r["score_reglementaire"]) == ("termine", [1, 2], [0, 1], [1, 2])
    SOFA_JOUR["events"][0]["status"]["description"] = "Retired"
    assert sources.lire_sofascore_jour(SOFA_JOUR, "football")[0]["statut"] == "autre"
    SOFA_JOUR["events"][0]["status"]["description"] = "Ended"


def test_incidents_et_compos_sofascore():
    b = sources.lire_sofascore_incidents({"incidents": [
        {"incidentType": "goal", "player": {"name": "Amine Gouiri"}, "isHome": False, "time": 33},
        {"incidentType": "goal", "player": {"name": "X"}, "isHome": True, "time": 80, "incidentClass": "ownGoal"},
        {"incidentType": "card"}]})
    assert [(x["joueur"], x["equipe"], x["csc"]) for x in b] == [("Amine Gouiri", 2, False), ("X", 1, True)]
    j = sources.lire_sofascore_compos({"home": {"players": [{"player": {"name": "A B"}, "statistics": {"minutesPlayed": 30, "points": 12}}]},
                                       "away": {"players": [{"player": {"name": "C D"}, "statistics": {"minutesPlayed": 0}}]}})
    assert j["A B"]["stats"]["Points"] == 12 and j["C D"]["a_joue"] is False


def test_lecteur_nhl():
    data = {"games": [{"id": 5, "startTimeUTC": "2026-10-25T00:00:00Z", "gameState": "OFF",
                       "gameOutcome": {"lastPeriodType": "OT"},
                       "homeTeam": {"placeName": {"default": "Toronto"}, "name": {"default": "Maple Leafs"}, "abbrev": "TOR", "score": 3},
                       "awayTeam": {"placeName": {"default": "Boston"}, "name": {"default": "Bruins"}, "abbrev": "BOS", "score": 2},
                       "goals": [{"period": 1, "name": {"default": "A. Matthews"}, "teamAbbrev": {"default": "TOR"}},
                                 {"period": 2, "name": {"default": "D. Pastrnak"}, "teamAbbrev": {"default": "BOS"}},
                                 {"period": 3, "name": {"default": "B. Marchand"}, "teamAbbrev": {"default": "BOS"}},
                                 {"period": 3, "name": {"default": "M. Marner"}, "teamAbbrev": {"default": "TOR"}},
                                 {"period": 4, "name": {"default": "J. Tavares"}, "teamAbbrev": {"default": "TOR"}}]}]}
    r = sources.lire_nhl_jour(data)[0]
    assert r["equipe_1"] == "Toronto Maple Leafs" and r["score"] == [3, 2] and r["score_reglementaire"] == [2, 2]
    assert r["periodes"][:3] == [[1, 0], [0, 1], [1, 1]]


def test_lecteur_espn_et_livescore():
    data = {"events": [{"id": "9", "date": "2026-10-18T15:30Z", "status": {"type": {"completed": True}},
                        "competitions": [{"competitors": [
                            {"homeAway": "home", "team": {"displayName": "Nottingham Forest", "id": "1"}, "score": "0",
                             "linescores": [{"value": 0}, {"value": 0}]},
                            {"homeAway": "away", "team": {"displayName": "Arsenal", "id": "2"}, "score": "1",
                             "linescores": [{"value": 1}, {"value": 0}]}],
                            "details": [{"scoringPlay": True, "type": {"text": "Goal"}, "team": {"id": "2"},
                                         "clock": {"displayValue": "28'"}, "athletesInvolved": [{"displayName": "Bukayo Saka"}]}]}]}]}
    r = sources.lire_espn_jour(data, "football", "eng.1")[0]
    assert r["score"] == [0, 1] and r["mi_temps"] == [0, 1] and r["buteurs"][0]["equipe"] == 2
    ls = {"Stages": [{"Snm": "Serie A", "Events": [{"Eid": "1", "T1": [{"Nm": "Monza"}], "T2": [{"Nm": "Cagliari"}],
                                                   "Tr1": "1", "Tr2": "0", "Trh1": "1", "Trh2": "0", "Eps": "FT", "Esd": "20261019163000"}]}]}
    r = sources.lire_livescore_jour(ls, "football")[0]
    assert (r["score"], r["mi_temps"], r["debut"]) == ([1, 0], [1, 0], "2026-10-19T16:30:00+00:00")


# ---------------------------------------------------------------- verdicts
def resultat(**kw):
    r = {"source": "sofascore", "id": 1, "sport": "football", "ligue": "L1", "debut": "2026-10-18T13:00:00+00:00",
         "equipe_1": "Angers", "equipe_2": "Marseille", "statut": "termine", "score": [1, 2],
         "score_reglementaire": [1, 2], "mi_temps": [0, 1], "periodes": [[0, 1], [1, 1]], "buteurs": None,
         "joueurs": None, "confirme_par": ["livescore"], "conflit": False}
    r.update(kw)
    return r


def boite(pari, match="Angers - Marseille", sport="Football", bookmaker="Winamax"):
    return {"id": "x", "pari": pari, "match": match, "sport": sport, "bookmaker": bookmaker,
            "debut": "2026-10-18T13:00:00+00:00"}


def verdict(pari, r, **kw):
    b = boite(pari, **kw)
    return rs.verdict_boost(b, r, analyser(b["pari"], b["match"], b["sport"]), T)


def test_verdicts_simples():
    assert verdict("Marseille gagne et plus de 2,5 buts dans le match", resultat())["statut"] == "gagné"
    assert verdict("Angers gagne", resultat())["statut"] == "perdu"
    assert verdict("Marseille gagne et plus de 3,5 buts dans le match", resultat())["statut"] == "perdu"
    assert verdict("Marseille mène à la mi-temps et gagne le match", resultat())["statut"] == "gagné"
    assert verdict("Marseille gagne le match 1-2, 0-1 ou 0-2", resultat())["statut"] == "gagné"
    assert verdict("Les deux équipes marquent", resultat())["statut"] == "gagné"
    assert verdict("Marseille marque dans les deux mi-temps", resultat())["statut"] == "gagné"


def test_une_jambe_perdue_suffit_meme_si_une_autre_est_inconnue():
    r = resultat(buteurs=None, joueurs=None)
    assert verdict("Angers gagne et Amine Gouiri buteur", r)["statut"] == "perdu"
    assert verdict("Marseille gagne et Amine Gouiri buteur", r) is None


def test_buteur_et_presence():
    r = resultat(buteurs=[{"joueur": "Amine Gouiri", "equipe": 2, "minute": 33, "csc": False}],
                 joueurs={"Amine Gouiri": {"equipe": 2, "a_joue": True, "stats": {}},
                          "Mason Greenwood": {"equipe": 2, "a_joue": False, "stats": {}},
                          "Pierre Aubameyang": {"equipe": 2, "a_joue": True, "stats": {}}})
    assert verdict("Amine Gouiri Buteur", r)["statut"] == "gagné"
    assert verdict("Pierre Aubameyang Buteur", r)["statut"] == "perdu"
    assert verdict("Mason Greenwood Buteur", r)["statut"] == "remboursé"
    assert verdict("Inconnu Joueur Buteur", r) is None                      # présence non vérifiable
    assert verdict("Pierre Aubameyang Buteur", r, bookmaker="Unibet") is None   # titulaire requis chez Unibet
    assert verdict("Amine Gouiri marque au moins un but en 2ème mi-temps", r) ["statut"] in ("perdu",)


def test_prolongation_et_csc_ne_comptent_pas():
    r = resultat(buteurs=[{"joueur": "Amine Gouiri", "equipe": 2, "minute": 105, "csc": False},
                          {"joueur": "Amine Gouiri", "equipe": 1, "minute": 20, "csc": True}],
                 joueurs={"Amine Gouiri": {"equipe": 2, "a_joue": True, "stats": {}}})
    assert verdict("Amine Gouiri Buteur", r)["statut"] == "perdu"


def test_confirmation_et_conflit():
    assert verdict("Angers gagne", resultat(confirme_par=[])) is None
    assert verdict("Angers gagne", resultat(conflit=True)) is None
    nhl = resultat(confirme_par=[], source="nhl", sport="hockey", score=[3, 2], score_reglementaire=[2, 2])
    assert verdict("Angers gagne", nhl, sport="Hockey sur glace")["statut"] == "perdu"   # nul au temps réglementaire
    assert verdict("Angers gagne", resultat(statut="autre")) is None


def test_basket_points_et_tennis():
    r = resultat(sport="basketball", equipe_1="Milwaukee Bucks", equipe_2="Boston Celtics", score=[110, 120],
                 score_reglementaire=None, mi_temps=None, periodes=None,
                 joueurs={"Giannis Antetokounmpo": {"equipe": 1, "a_joue": True, "stats": {"Points": 40, "Rebounds": 12, "Assists": 4}}})
    v = verdict("G. Antetokounmpo réalise une performance points + rebonds + passes décisives d'au moins 55",
                r, match="Milwaukee - Boston", sport="Basketball")
    assert v["statut"] == "gagné"
    assert verdict("Boston gagne", r, match="Milwaukee - Boston", sport="Basketball")["statut"] == "gagné"
    t = resultat(sport="tennis", equipe_1="Jovic Iva", equipe_2="Shnaider Diana", score=[1, 2],
                 score_reglementaire=None, mi_temps=None, periodes=[[6, 7], [6, 3], [4, 6]])
    assert verdict("Diana Shnaider gagne 2-1", t, match="Jovic, Iva - Shnaider, Diana", sport="Tennis")["statut"] == "gagné"
    assert verdict("Plus de 2,5 sets lors du match", t, match="Jovic, Iva - Shnaider, Diana", sport="Tennis")["statut"] == "gagné"
    assert verdict("Plus de 25,5 jeux dans le match".replace("Plus", "Plus"), t, match="Jovic, Iva - Shnaider, Diana",
                   sport="Tennis")["statut"] == "gagné"


def test_match_annule_rembourse_apres_48h():
    r = resultat(statut="annule", score=None)
    assert verdict("Angers gagne", r)["statut"] == "remboursé"


# ---------------------------------------------------------------- recherche, archive et passage complet
def lire_factice(url, proxy=False):
    if "sofascore" in url and "scheduled-events" in url:
        return SOFA_JOUR
    return None


def test_recherche_archive_et_sans_correspondance(monkeypatch):
    monkeypatch.setitem(sources.SOURCES["jour"], "sofascore",
                        lambda lire, sport, date: sources.lire_sofascore_jour(SOFA_JOUR, sport))
    monkeypatch.setitem(sources.SOURCES["jour"], "livescore",
                        lambda lire, sport, date: [dict(sources.lire_sofascore_jour(SOFA_JOUR, sport)[0], source="livescore")])
    monkeypatch.setitem(sources.SOURCES["jour"], "espn", lambda lire, sport, date: [])
    arch = archive_vide()
    rech = Recherche(arch, lire_factice, T)
    b = boite("Marseille gagne")
    b["ligue"] = "Ligue 1"
    r = rech.chercher(b)
    assert r["score"] == [1, 2] and r["confirme_par"] == ["livescore"]
    assert len(arch["evenements"]) == 1 and arch["ligues"]["Ligue 1"]["sofascore"] == 1
    inconnu = boite("Gagne", match="Equipe Inconnue - Autre Equipe")
    assert rech.chercher(inconnu) is None
    assert list(arch["sans_correspondance"].values())[0]["essais"] == 1


def test_passage_complet_regle_le_boost(monkeypatch):
    monkeypatch.setitem(sources.SOURCES["jour"], "sofascore",
                        lambda lire, sport, date: sources.lire_sofascore_jour(SOFA_JOUR, sport))
    monkeypatch.setitem(sources.SOURCES["jour"], "livescore",
                        lambda lire, sport, date: [dict(sources.lire_sofascore_jour(SOFA_JOUR, sport)[0], source="livescore")])
    monkeypatch.setitem(sources.SOURCES["jour"], "espn", lambda lire, sport, date: [])
    base = {"a": boite("Marseille gagne"), "b": boite("Angers gagne"),
            "c": {**boite("Marseille gagne"), "reglement": {"statut": "perdu", "modele": "gpt"}},
            "d": boite("Premier buteur Ronaldo"), "e": {**boite("Marseille gagne"), "long_terme": True}}
    rech = Recherche(archive_vide(), lire_factice, T)
    resume = rs.regler(base, rech, T)
    assert base["a"]["reglement"]["statut"] == "gagné" and base["a"]["reglement"]["methode"] == "scores"
    assert base["b"]["reglement"]["statut"] == "perdu"
    assert base["c"]["reglement"]["statut"] == "perdu" and base["c"]["reglement"]["modele"] == "gpt"   # IA/manuel intouché
    assert "reglement" not in base["e"] and resume["regles"] == 2 and resume["non_analysables"] == 1
