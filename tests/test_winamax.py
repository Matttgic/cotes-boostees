"""Parseur Winamax sur une vraie page réduite (boosts du 8/10/2026) et fusion dans l'historique."""
from pathlib import Path

import pytest

from boosts import stockage, winamax

HTML = (Path(__file__).parent / "winamax_2026-10-08.html").read_text(encoding="utf-8")


@pytest.fixture
def lignes():
    return winamax.boosts(winamax.etat(HTML))


def test_onze_boosts_et_pas_le_match_normal(lignes):
    assert len(lignes) == 11
    assert all(l["bookmaker"] == "Winamax" for l in lignes)
    assert not any(l["match"] == "PSG - OM" for l in lignes)


def test_champs_du_boost_handball(lignes):
    b = next(l for l in lignes if "Nantes" in (l["match"] or ""))
    assert b["match"] == "Melsungen - Nantes"            # préfixe « Cote Boostée : » retiré
    assert b["pari"] == "Nantes gagne et plus de 58,5 buts dans le match"
    assert b["cote_origine"] == 3.65 and b["cote_boostee"] == 4.25
    assert b["hausse_pct"] == 16.4
    assert b["mise_max"] == 20
    assert b["sport"] == "Handball"
    assert b["type"] == "cote boostée"
    assert b["debut"].startswith("2026-")
    assert b["id"].startswith("winamax|")


def test_intitules_nettoyes_et_cotes_arrondies(lignes):
    assert not any("\t" in (l["pari"] or "") or "\t" in (l["match"] or "") for l in lignes)
    nhl = next(l for l in lignes if l["match"] == "NHL")
    assert nhl["cote_origine"] == 3.09                    # 3.0901640000000006 côté Winamax


def test_identifiants_uniques(lignes):
    assert len({l["id"] for l in lignes}) == len(lignes)


def test_page_de_blocage():
    with pytest.raises(winamax.PageInattendue):
        winamax.etat("<html>403 ERROR The request could not be satisfied</html>")


def test_mise_max_depuis_le_tournoi():
    assert winamax._mise_max(None, "Grosse cote boostée",
                             "Mise maximale de 10 € pour les Grosses Cotes Boostées.") == 10


def test_fusion_historique(lignes):
    base = {}
    assert stockage.fusionner(base, lignes, "2026-10-08T18:00:00+00:00") == (11, 0)
    # même passage une heure plus tard, une cote a bougé
    modifiees = [dict(l) for l in lignes]
    modifiees[0]["cote_boostee"] = 9.99
    assert stockage.fusionner(base, modifiees, "2026-10-08T19:00:00+00:00") == (0, 1)
    b = base[modifiees[0]["id"]]
    assert b["cote_boostee"] == 9.99 and b["cote_boostee_initiale"] == lignes[0]["cote_boostee"]
    assert b["historique_cotes"] == [{"jusqu_a": "2026-10-08T19:00:00+00:00",
                                      "cote_boostee": lignes[0]["cote_boostee"]}]
    assert b["nb_vues"] == 2 and b["premiere_vue"] == "2026-10-08T18:00:00+00:00"


def test_fusion_ne_touche_pas_aux_champs_ajoutes(lignes):
    base = {}
    stockage.fusionner(base, lignes[:1], "t1")
    base[lignes[0]["id"]]["statut"] = "gagné"           # ajouté plus tard par le règlement
    stockage.fusionner(base, lignes[:1], "t2")
    assert base[lignes[0]["id"]]["statut"] == "gagné"



def test_titre_nba_classe_long_terme_et_historique_corrige():
    assert winamax.est_long_terme("NBA 2026 - 2027", "New York Knicks gagne le titre NBA")
    ancien = {"winamax|715030061|2216203536": {
        "id": "winamax|715030061|2216203536", "bookmaker": "Winamax",
        "match": "NBA 2026 - 2027", "pari": "New York Knicks gagne le titre NBA",
        "debut": "2026-10-09T17:00:00+00:00",
        "reglement": {"tentatives": 1, "derniere_tentative": "2026-10-09T21:08:28+00:00"},
    }}
    assert winamax.corriger_long_terme(ancien) == 1
    assert ancien["winamax|715030061|2216203536"]["long_terme"] is True
    assert winamax.corriger_long_terme(ancien) == 0
    from datetime import datetime, timezone
    from boosts.reglement import a_regler
    assert a_regler(ancien, datetime(2026, 10, 10, 2, tzinfo=timezone.utc)) == []


def test_matchs_normaux_non_marqués_long_terme():
    for titre, pari in [
        ("Lyon - Lens", "Lens gagne la rencontre"),
        ("NBA", "New York Knicks - Boston Celtics : plus de 220,5 points"),
        ("Coupe du monde", "Finale : l'équipe A gagne"),
        ("NBA 2026 - 2027", "Plus de 230,5 points Lakers - Bucks"),
    ]:
        assert winamax.est_long_terme(titre, pari) is False
    assert winamax.est_long_terme("NBA 2026 - 2027", "Chicago Bulls champion de la conférence") is True
