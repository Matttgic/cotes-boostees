"""Vérifications des six challengers (hors réseau) et prévention du look-ahead."""
from copy import deepcopy

from boosts import simulation
from boosts.strategies_experimentales import _valeur_initiale, construire


def exemple(identifiant="1", *, statut="gagné", debut="2026-10-10T12:00:00+00:00",
            premiere_vue="2026-10-09T11:00:00+00:00", cote=2.5, mise=50, match="A - B"):
    b = {"id": identifiant, "match": match, "pari": "Total", "sport": "Football",
         "bookmaker": "Winamax", "debut": debut, "premiere_vue": premiere_vue,
         "mise_max": mise, "cote_boostee_initiale": cote, "cote_boostee": cote,
         "long_terme": False, "reglement": {"statut": statut}}
    return b


def evaluation(b, *, cote=2.2, juste=2.0, ev=10, date="2026-10-09T11:10:00+00:00", statut="exacte"):
    b["valeur_initiale"] = {"statut": statut, "ev_pct": ev, "cote_juste": juste,
                           "cote_boostee": cote, "date": date}
    return b


def test_garde_les_trois_strategies_initiales_et_en_ajoute_six():
    b = exemple()
    original = deepcopy(b)
    bilans = simulation.strategies({b["id"]: b})
    assert list(bilans) == ["A", "B_exacte", "B_approx", "C_plafond",
                            "D_moderee", "E_48h", "F_ev8", "G_kelly", "H_1_match"]
    assert bilans["A"]["global"]["gain_net"] == 75.0
    assert bilans["C_plafond"]["global"]["gain_net"] == 15.0
    assert bilans["C_plafond"]["global"]["mise_totale"] == 10
    assert b == original


def test_tranche_cote_reference_initiale_pas_derniere_cote():
    a = exemple("a", cote=3.2)
    a["cote_boostee"] = 8.0
    b = exemple("b", cote=4.2)
    choix = construire({x["id"]: x for x in [a, b]})["D_moderee"]
    assert len(choix["paris"]) == 1
    assert choix["paris"][0]["cote"] == 3.2
    assert choix["paris"][0]["mise"] == 10


def test_48_heures_depuis_premiere_observation_pas_derniere():
    a = exemple("a")
    a["derniere_vue"] = "2026-10-10T11:00:00+00:00"
    b = exemple("b", premiere_vue="2026-10-05T11:00:00+00:00")
    c = exemple("c", premiere_vue="2026-10-10T13:00:00+00:00")
    d = exemple("d")
    d["long_terme"] = True
    choix = construire({x["id"]: x for x in [a, b, c, d]})["E_48h"]
    assert [x["id"] for x in choix["paris"]] == ["a"]


def test_ev_au_prix_observe_lors_evaluation_pas_au_prix_passe():
    b = evaluation(exemple(cote=3.0), cote=2.2, juste=2, ev=10)
    bilans = simulation.strategies({b["id"]: b})
    f = bilans["F_ev8"]
    assert f["global"]["regles"] == 1
    assert f["global"]["mise_totale"] == 10
    assert f["paris"][0]["cote"] == 2.2
    assert f["global"]["gain_net"] == 12.0
    assert bilans["A"]["paris"][0]["cote"] == 3.0


def test_aucune_evaluation_apres_match_ou_approximation():
    a = evaluation(exemple("a"), date="2026-10-11T10:00:00+00:00")
    b = evaluation(exemple("b"), statut="approx")
    c = evaluation(exemple("c"), date=None)
    d = evaluation(exemple("d"), cote=2.2, juste=2, ev=35)  # EV incohérente avec le prix
    bilans = construire({x["id"]: x for x in [a, b, c, d]})
    assert bilans["F_ev8"]["global"]["paris"] == 0
    assert bilans["G_kelly"]["global"]["paris"] == 0


def test_kelly_quart_plafond_et_prix_coherent():
    b = evaluation(exemple(mise=50), cote=3.0, juste=2.85, ev=5.3)
    bilans = construire({b["id"]: b})
    g = bilans["G_kelly"]
    assert g["global"]["regles"] == 1
    assert g["paris"][0]["mise"] == 6.58
    assert g["paris"][0]["cote"] == 3.0
    assert g["global"]["gain_net"] == 13.16


def test_concentration_choisit_premier_boost_avant_resultat():
    a = exemple("a", statut="perdu", premiere_vue="2026-10-09T10:00:00+00:00")
    b = exemple("b", statut="gagné", premiere_vue="2026-10-09T11:00:00+00:00")
    c = exemple("c", match="Autre match")
    h = construire({x["id"]: x for x in [a, b, c]})["H_1_match"]
    assert {p["id"] for p in h["paris"]} == {"a", "c"}
    assert h["global"]["gain_net"] == 5


def test_ev_incomplete_reste_non_jouee():
    b = exemple()
    b["valeur_initiale"] = {"statut": "exacte", "ev_pct": 10, "cote_juste": 2}
    assert _valeur_initiale(b, 5, 4) is None
    assert construire({b["id"]: b})["F_ev8"]["global"]["regles"] == 0
