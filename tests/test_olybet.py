"""Parseur OlyBet sur les vraies réponses swarm du 13/10/2026 (sonde n° 10), sans réseau."""
import json
from pathlib import Path

from boosts import olybet

DONNEES = json.loads((Path(__file__).parent / "olybet_2026-10-13.json").read_text(encoding="utf-8"))


def _boosts():
    return olybet.boosts(DONNEES["jeux"], olybet.selections(DONNEES["boosted_selections"]))


def test_selections_groupees_par_match_sans_doublon():
    s = olybet.selections(DONNEES["boosted_selections"])
    assert len(s) == 6
    assert s[31215827] == {7330380391}


def test_boosts_du_13_octobre():
    b = {x["id"]: x for x in _boosts()}
    assert len(b) == 4                     # 2 sélections annoncées n'ont pas de détail (retirées)
    real = b["olybet|31215827|7330380391"]
    assert real["match"] == "AS Rome - Real Madrid"
    assert real["pari"] == "Real Madrid to win and Vinicius to score"
    assert real["cote_boostee"] == 4.0
    assert real["mise_max"] == 8.33
    assert real["cote_origine"] is None
    assert real["sport"] == "Football"
    assert real["ligue"] == "Ligue des Champions"
    assert real["debut"].startswith("2026-10-14T18:45")
    assert real["bookmaker"] == "OlyBet" and real["disponible"] and not real["long_terme"]
    ars = b["olybet|31213207|7328896155"]
    assert ars["match"] == "Arsenal - Lille"
    assert ars["pari"] == "Les 2 équipes marquent et plus de 2,5 buts"
    assert ars["mise_max"] == 17.24
    tennis = b["olybet|31215805|7330210853"]
    assert tennis["sport"] == "Tennis" and tennis["ligue"] == "ATP Masters Shanghai - Dur"


def test_mise_max_gain_net_25():
    assert olybet.mise_max(4.5) == 7.14
    assert olybet.mise_max(3.5) == 10.0
    assert olybet.mise_max(2.0) == 25.0
    assert olybet.mise_max(1.0) is None


def test_separer_sans_affiche():
    assert olybet.separer("Mbappé marque un doublé (14.10.2026)") == (None, "Mbappé marque un doublé")
    assert olybet.separer("A - B: X gagne") == ("A - B", "X gagne")


class FauxSwarm:
    def __init__(self, *a, **k):
        self.octets = 0
        self.commandes = []

    def appel(self, commande, params):
        self.commandes.append((commande, params))
        if commande == "get_boosted_selections":
            return DONNEES["boosted_selections"]
        if commande == "get":
            assert sorted(params["where"]["game"]["id"]["@in"]) == sorted(
                olybet.selections(DONNEES["boosted_selections"]))
            return DONNEES["jeux"]
        return {"code": 0, "data": {"sid": "x"}}

    def fermer(self):
        pass


def test_collecter_direct(monkeypatch):
    monkeypatch.setattr(olybet.time, "time", lambda: 1791900000)       # 13/10, avant tous les matchs
    monkeypatch.setattr(olybet, "Swarm", FauxSwarm)
    assert len(olybet.collecter(None)) == 4


def test_collecter_secours_proxy(monkeypatch):
    appels = []

    def fabrique(proxies=None, verif=True):
        appels.append(proxies)
        if proxies is None:
            raise ConnectionError("refusé")
        return FauxSwarm()

    class Nav:
        proxies, verif, octets, requetes = {"https": "p"}, "ca", 0, 0

    monkeypatch.setattr(olybet.time, "time", lambda: 1791900000)
    monkeypatch.setattr(olybet, "Swarm", fabrique)
    nav = Nav()
    assert len(olybet.collecter(nav)) == 4
    assert appels == [None, {"https": "p"}] and nav.requetes == 1


def test_matchs_commences_ignores():
    choisis = olybet.selections(DONNEES["boosted_selections"])
    # 13/10/2026 20 h 50 (Paris) : Arsenal - Lille (20 h 45) a commencé
    ids = {b["id"] for b in olybet.boosts(DONNEES["jeux"], choisis, 1791917400)}
    assert "olybet|31213207|7328896155" not in ids and len(ids) == 3
