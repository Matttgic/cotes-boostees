"""Super Cotes Genybet / NetBet (Sportnco) sur les vraies pages du 13/10/2026, sans réseau."""
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace as NS

from boosts import nuxt, sportnco

DOSSIER = Path(__file__).parent
GENY = (DOSSIER / "genybet_super-cotes_2026-10-13.html").read_text(encoding="utf-8")
NETBET_VIDE = (DOSSIER / "netbet_super-cotes_vide_2026-10-13.html").read_text(encoding="utf-8")
AVANT = datetime(2026, 10, 13, 18, 0, tzinfo=timezone.utc)


def test_etat_nuxt_lu_sans_javascript():
    etat = nuxt.etat(GENY)
    assert etat["routePath"] == "/super-cotes"
    assert len(sportnco.evenements(etat)) == 1


def test_super_cote_genybet():
    (b,) = sportnco.boosts(nuxt.etat(GENY), "genybet", AVANT)
    assert b["id"] == "genybet|12244000|4829779607"
    assert b["bookmaker"] == "Genybet" and b["sport"] == "Football"
    assert b["match"] == "Lille - Arsenal"
    assert b["pari"] == "Lille (vs Arsenal) marque au moins 1 but"
    assert b["cote_boostee"] == 2.1 and b["cote_origine"] is None
    assert b["mise_max"] == 10.0 and not b["mise_max_supposee"]
    assert b["debut"] == "2026-10-13T19:00+00:00"
    assert "temps réglementaire" in b["intitule_brut"]


def test_match_commence_ignore():
    assert sportnco.boosts(nuxt.etat(GENY), "genybet", datetime(2026, 10, 13, 19, 5, tzinfo=timezone.utc)) == []


def test_netbet_sans_super_cote():
    assert sportnco.boosts(nuxt.etat(NETBET_VIDE), "netbet", AVANT) == []


def test_separer():
    assert sportnco.separer("PSG (vs OM) gagne") == ("PSG - OM", "PSG (vs OM) gagne")
    assert sportnco.separer("Mbappé marque") == (None, "Mbappé marque")


def test_affectations_et_parametres():
    html = ('<script>window.__NUXT__=(function(a,b,c){b.x=[a,c];b["y"]=Array(2);return {s:b,t:"\\u002Fz",'
            'u:void 0,v:-1.5,w:true}}(1,{},"c"));</script>')
    assert nuxt.etat(html) == {"s": {"x": [1, "c"], "y": [None, None]}, "t": "/z", "u": None, "v": -1.5, "w": True}


class FauxNavigateur:
    def __init__(self, pages):
        self.pages, self.urls = pages, []

    def get(self, url):
        self.urls.append(url)
        return NS(status_code=200, text=self.pages[url])


def test_collecter(monkeypatch):
    class Horloge(datetime):
        @classmethod
        def now(cls, tz=None):
            return AVANT
    monkeypatch.setattr(sportnco, "datetime", Horloge)
    nav = FauxNavigateur({"https://sport.genybet.fr/super-cotes": GENY,
                          "https://www.netbet.fr/super-cotes": NETBET_VIDE})
    assert len(sportnco.collecter_genybet(nav)) == 1
    assert sportnco.collecter_netbet(nav) == []
    assert nav.urls == ["https://sport.genybet.fr/super-cotes", "https://www.netbet.fr/super-cotes"]
