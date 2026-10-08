"""Parseur Unibet sur les vraies pages du 8/10/2026 (état serverApp-state), sans réseau."""
from pathlib import Path
from types import SimpleNamespace as NS

from boosts import unibet

DOSSIER = Path(__file__).parent
LISTE = (DOSSIER / "unibet_liste_2026-10-08.html").read_text(encoding="utf-8")
EVENEMENT = (DOSSIER / "unibet_evenement_2026-10-08.html").read_text(encoding="utf-8")


class FauxNavigateur:
    def __init__(self):
        self.urls = []

    def get(self, url):
        self.urls.append(url)
        return NS(status_code=200, text=LISTE if url == unibet.URL else EVENEMENT)


def test_collecte_liste_et_evenement():
    nav, cache = FauxNavigateur(), {}
    lignes = unibet.collecter(nav, cache)
    assert len(lignes) == 20                      # 1 boost de match + 19 boosts du paquet NBA
    assert nav.urls[1].endswith("/3381006/paris-trashtalk-26-27")
    assert len({l["id"] for l in lignes}) == 20
    # deuxième passage : même nombre de paris → page de l'événement non relue
    nav2 = FauxNavigateur()
    assert len(unibet.collecter(nav2, cache)) == 20 and nav2.urls == [unibet.URL]


def test_boost_de_match():
    b = next(l for l in unibet.collecter(FauxNavigateur(), {}) if l["match"] == "Montauban - Brive")
    assert b["pari"] == "Montauban gagne et Johnny Matthews marque au moins 1 essai"
    assert b["cote_origine"] == 2.5 and b["cote_boostee"] == 2.75 and b["hausse_pct"] == 10.0
    assert b["mise_max"] == 25 and not b["mise_max_supposee"]
    assert b["sport"] == "Rugby" and not b["long_terme"] and b["debut"].startswith("2026-10-08T19:00")


def test_boosts_saison_nba():
    lignes = [l for l in unibet.collecter(FauxNavigateur(), {}) if l["ligue"] == "Cotes Boostées NBA"]
    v = next(l for l in lignes if "VanVleet" in l["pari"])
    assert v["pari"] == "HOU Rockets - Fred VanVleet fait 6 passes ou + (moyenne)"
    assert v["cote_origine"] == 1.8 and v["cote_boostee"] == 2.1 and v["mise_max"] == 25
    assert all(l["long_terme"] for l in lignes)   # paquet « Paris Trashtalk 26/27 » : réglé en fin de saison
    sans = [l for l in lignes if l["mise_max_supposee"]]
    assert sans and all(l["mise_max"] == unibet.MISE_DEFAUT for l in sans)
    assert all("(" not in (l["pari"] or "")[-3:] for l in lignes)


def test_page_de_blocage():
    import pytest
    with pytest.raises(unibet.PageInattendue):
        unibet.etat("<html>captcha-delivery</html>")
