"""Flash Boosts Betsson France sur les vraies réponses de l'API du 13/10/2026, sans réseau."""
import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace as NS

import pytest

from boosts import betsson

DONNEES = json.loads((Path(__file__).parent / "betsson_2026-10-13.json").read_text(encoding="utf-8"))
AVANT = datetime(2026, 10, 13, 19, 0, tzinfo=timezone.utc)


def _boosts(quand=AVANT):
    return {b["id"]: b for b in betsson.boosts(DONNEES["cartes"], DONNEES["marches"], quand)}


def test_quatre_flash_boosts_cartes_perimees_ignorees():
    b = _boosts()
    assert len(betsson.cartes(DONNEES["cartes"])) == 9 and len(b) == 4
    barcola = b["betsson|93666744.1|393253164.1"]
    assert barcola["pari"] == "Barcola Buteur"
    assert barcola["match"] == "LASK Linz - Liverpool"
    assert (barcola["cote_origine"], barcola["cote_boostee"], barcola["hausse_pct"]) == (2.25, 2.65, 17.8)
    assert barcola["mise_max"] == 20.0 and not barcola["mise_max_supposee"]
    assert barcola["sport"] == "Football" and barcola["ligue"] == "Ligue des Champions"
    assert barcola["debut"] == "2026-10-14T16:45+00:00" and barcola["disponible"]
    psg = b["betsson|93668376.1|393257032.1"]
    assert psg["pari"] == "Le PSG gagne 1-0" and (psg["cote_origine"], psg["cote_boostee"]) == (13.0, 15.0)


def test_match_commence_ignore():
    apres = datetime(2026, 10, 14, 17, 0, tzinfo=timezone.utc)
    assert "betsson|93666744.1|393253164.1" not in _boosts(apres) and len(_boosts(apres)) == 3


def test_nettoyer_et_cote_fractionnaire():
    assert betsson.nettoyer("🐘 Monaco gagne 3-0 (Max 20€) - Flash Boost") == "Monaco gagne 3-0"
    assert betsson.cote({"currentpriceup": "33", "currentpricedown": "20"}) == 2.65
    assert betsson.cote({"currentpriceup": None}) is None


class FauxNav:
    """Refuse les deux premières IP (géolocalisation), puis répond comme l'API."""

    def __init__(self, refus=2):
        self.refus, self.proxies_vus, self.requetes = refus, [], 0

    def post(self, url, json=None, headers=None, proxies=None):
        self.requetes += 1
        self.proxies_vus.append(proxies["https"])
        if self.refus:
            self.refus -= 1
            return NS(status_code=403, json=lambda: {}, text="Geoloc redirection")
        t, i = json["contentId"]["type"], json["contentId"]["id"]
        rep = DONNEES["cartes"] if t == "headline" else DONNEES["marches"].get(i, {})
        return NS(status_code=200, json=lambda: rep)


@pytest.fixture
def secrets(monkeypatch):
    for k, v in {"BRIGHTDATA_CUSTOMER_ID": "c", "BRIGHTDATA_ZONE": "z", "BRIGHTDATA_PASSWORD": "p"}.items():
        monkeypatch.setenv(k, v)
    monkeypatch.setattr(betsson, "datetime", type("H", (datetime,), {"now": classmethod(lambda c, tz=None: AVANT)}))


def test_collecter_change_d_ip_et_garde_la_bonne(secrets):
    nav, cache = FauxNav(refus=2), {}
    assert len(betsson.collecter(nav, cache)) == 4
    assert cache["essais"] == 3 and cache["session"] in nav.proxies_vus[2]
    nav2 = FauxNav(refus=0)
    betsson.collecter(nav2, cache)
    assert cache["session"] in nav2.proxies_vus[0]          # la session gardée sert d'abord


def test_collecter_aucune_ip(secrets):
    with pytest.raises(betsson.PageInattendue):
        betsson.collecter(FauxNav(refus=99), {})
