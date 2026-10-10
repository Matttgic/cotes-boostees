"""Contrats du cerveau d'observation (uniquement du papier, jamais de placement réel)."""
from copy import deepcopy

from boosts import cerveau

T0 = "2026-10-09T13:00:00+00:00"
T1 = "2026-10-09T14:00:00+00:00"
DEBUT = "2026-10-09T18:00:00+00:00"


def boost(identifiant="1", **overrides):
    b = {
        "id": identifiant, "bookmaker": "Winamax", "sport": "Football",
        "match": "A - B", "pari": "Victoire A", "debut": DEBUT,
        "derniere_vue": T0, "disponible": True,
        "mise_max": 20, "mise_max_supposee": False,
        "cote_boostee": 2.4, "long_terme": False,
        "valeur_derniere": {
            "date": T0, "statut": "exacte",
            "cote_juste": 2.2, "cote_boostee": 2.4,
            "ev_pct": 9.1, "sources": ["Pinnacle"],
            "detail": [{"match": "A - B", "marche": "RESULTAT_1N2"}],
        },
    }
    b.update(overrides)
    return b


def observer(base, registre, at=T0):
    return cerveau.rafraichir(base, registre, at, heure_execution=at)


def test_selection_fictive_et_journal_immuable():
    b = boost()
    original = deepcopy(b)
    journal = {}
    assert observer({"1": b}, journal)["nouveaux_boosts"] == 1
    e = journal["entrees"]["1"]
    assert e["premiere_selection"]["decision"] == "selectionner"
    assert e["premiere_selection"]["mise_fictive"] == 10
    assert e["premiere_selection"]["cote"] == 2.4
    assert e["historique"][0]["version"] == cerveau.VERSION
    assert journal["bilan"]["paris_selectionnes"] == 1
    assert journal["bilan"]["paris_regles"] == 0
    assert b == original


def test_aucune_doublure_au_scan_identique():
    b = boost()
    registre = {}
    observer({"1": b}, registre)
    assert observer({"1": b}, registre)["decisions_enregistrees"] == 0
    assert len(registre["entrees"]["1"]["historique"]) == 1


def test_absence_source_devient_selection_avant_match():
    b = boost()
    b["valeur_derniere"] = {"statut": "non_evaluable", "date": T0}
    journal = {}
    observer({"1": b}, journal)
    assert journal["entrees"]["1"]["premiere_selection"] is None
    assert journal["entrees"]["1"]["historique"][-1]["decision"] == "abstention"
    b["derniere_vue"] = T1
    b["valeur_derniere"] = boost()["valeur_derniere"] | {"date": T1}
    observer({"1": b}, journal, at=T1)
    e = journal["entrees"]["1"]
    assert [v["decision"] for v in e["historique"]] == ["abstention", "selectionner"]
    assert e["premiere_selection"]["horodatage"] == T1


def test_premiere_selection_verrouillee_et_reglement_post_match():
    b = boost()
    registre = {}
    observer({"1": b}, registre)
    b["derniere_vue"] = T1
    b["cote_boostee"] = 3.0
    b["valeur_derniere"] = boost()["valeur_derniere"] | {
        "date": T1, "cote_boostee": 3.0, "cote_juste": 2.8, "ev_pct": 7.1}
    observer({"1": b}, registre, at=T1)
    e = registre["entrees"]["1"]
    assert len(e["historique"]) == 2
    assert e["premiere_selection"]["cote"] == 2.4
    b["reglement"] = {"statut": "gagné", "source": "manuel"}
    nouveau = cerveau.bilan(registre, {"1": b})
    assert nouveau["gain_net"] == 14
    assert nouveau["historique_paris"][0]["resultat_source"] == "manuel"
    assert e["premiere_selection"]["cote"] == 2.4


def test_ne_pas_backfiller_apres_coup():
    b = boost(debut="2026-10-09T12:59:00+00:00")
    registre = {}
    observer({"1": b}, registre)
    assert registre["entrees"] == {}


def test_refuse_scan_debute_avant_le_coup_d_envoi_mais_termine_apres():
    b = boost(debut="2026-10-09T13:30:00+00:00")
    registre = {}
    cerveau.rafraichir({"1": b}, registre, T0, heure_execution=T1)
    assert registre["entrees"] == {}


def test_ne_pas_reprendre_boost_pas_vu_au_scan_courant():
    b = boost(derniere_vue="2026-10-09T12:00:00+00:00")
    registre = {}
    observer({"1": b}, registre)
    assert registre["entrees"] == {}
    b["derniere_vue"] = T0
    b["disponible"] = False
    observer({"1": b}, registre)
    assert registre["entrees"] == {}


def test_regles_de_confiance_et_rejet():
    b = boost()
    b["valeur_derniere"]["statut"] = "approx"
    assert cerveau._calcul(b, T0)["decision"] == "abstention"
    b["valeur_derniere"]["statut"] = "exacte"
    b["valeur_derniere"]["detail"].append({"match": "A - B"})
    assert cerveau._calcul(b, T0)["decision"] == "abstention"
    b["valeur_derniere"]["detail"].pop()
    b["valeur_derniere"]["ev_pct"] = 1
    b["valeur_derniere"]["cote_juste"] = 2.376
    assert cerveau._calcul(b, T0)["decision"] == "ecarter"
    b["valeur_derniere"]["ev_pct"] = 9.1
    assert cerveau._calcul(b, T0)["decision"] == "abstention"


def test_mises_et_disponibilite_non_confirmees_sont_abstention():
    assert cerveau._calcul(boost(mise_max=None), T0)["decision"] == "abstention"
    assert cerveau._calcul(boost(mise_max_supposee=True), T0)["decision"] == "abstention"
    assert cerveau._calcul(boost(long_terme=True), T0)["decision"] == "hors_perimetre"
    assert cerveau._calcul(boost(debut="2026-11-09T13:00:00+00:00"), T0)["decision"] == "hors_perimetre"


def test_les_reglements_sur_boosts_non_selectionnes_ne_creent_ni_profit_ni_pari():
    b = boost()
    b["valeur_derniere"] = {"date": T0, "statut": "non_evaluable"}
    registre = {}
    observer({"1": b}, registre)
    b["reglement"] = {"statut": "gagné"}
    x = cerveau.bilan(registre, {"1": b})
    assert x["paris_selectionnes"] == 0 and x["gain_net"] == 0


def test_les_pertes_et_remboursements():
    a, b, c = boost("a"), boost("b"), boost("c")
    registre = {}
    observer({"a": a, "b": b, "c": c}, registre)
    a["reglement"], b["reglement"], c["reglement"] = (
        {"statut": "perdu"}, {"statut": "gagné"}, {"statut": "remboursé"})
    stats = cerveau.bilan(registre, {"a": a, "b": b, "c": c})
    assert stats["paris_regles"] == 3
    assert stats["gain_net"] == 4
    assert stats["mises_reglees"] == 30
    assert stats["pire_baisse"] == -10
    assert stats["gagnes"] == 1 and stats["perdus"] == 1


def test_un_changement_de_decision_est_conserve_dans_historique():
    b = boost()
    registre = {}
    observer({"1": b}, registre)
    b["derniere_vue"] = T1
    b["valeur_derniere"] = boost()["valeur_derniere"] | {
        "date": T1, "cote_juste": 2.6, "ev_pct": -7.7}
    observer({"1": b}, registre, at=T1)
    e = registre["entrees"]["1"]
    assert len(e["historique"]) == 2
    assert e["historique"][-1]["decision"] == "ecarter"
    assert e["premiere_selection"]["decision"] == "selectionner"


def test_combine_vraiment_distinct_avec_ev_exacte_est_selectionne():
    b = boost()
    b["valeur_derniere"]["detail"] = [
        {"match": "Nantes - Lyon", "source": "Pinnacle"},
        {"match": "Braga - Sporting Portugal", "source": "Betfair"},
    ]
    d = cerveau._calcul(b, T0)
    assert d["decision"] == "selectionner"
    assert d["mise_fictive"] == 10
    assert d["motif_code"] == "ev_positive"
    assert any("2 rencontres" in r for r in d["raisons"])


def test_combine_meme_match_inverse_ou_nom_variation_reste_abstention():
    b = boost()
    b["valeur_derniere"]["detail"] = [
        {"match": "Paris SG - Lyon"},
        {"match": "Lyon - Paris SG"},
    ]
    d = cerveau._calcul(b, T0)
    assert d["decision"] == "abstention"
    assert d["motif_code"] == "independance_non_verifiee"
    b["valeur_derniere"]["detail"][1]["match"] = "Lyon - Paris SG FC"
    assert cerveau._calcul(b, T0)["decision"] == "abstention"


def test_combine_sans_rencontres_identifiables_reste_abstention():
    b = boost()
    b["valeur_derniere"]["detail"] = [{"match": "Nantes - Lyon"}, {"marche": "TOTAL"}]
    assert cerveau._calcul(b, T0)["motif_code"] == "independance_non_verifiee"


def test_combine_lie_avec_ev_approximative_ne_se_selectionne_pas():
    b = boost()
    b["valeur_derniere"]["statut"] = "approx"
    b["valeur_derniere"]["detail"] = [{"match": "Nantes - Lyon"}, {"match": "Nantes - Lyon"}]
    d = cerveau._calcul(b, T0)
    assert d["decision"] == "abstention"
    assert d["motif_code"] == "combiné_lie"


def test_diagnostic_precis_marche_introuvable_et_sport_non_suivi():
    b = boost()
    b["valeur_derniere"] = {"statut": "non_evaluable", "date": T0,
                            "raison": "Pinnacle : match introuvable (X - Y)"}
    v = cerveau._calcul(b, T0)
    assert v["motif_code"] == "match_introuvable"
    assert v["reference_raison"].startswith("Pinnacle")
    b["valeur_derniere"]["raison"] = "sport non suivi (Judo)"
    assert cerveau._calcul(b, T0)["motif_code"] == "sport_non_suivi"
    b["valeur_derniere"]["raison"] = "Betfair : ligne absente (JOUEUR MATCH)"
    assert cerveau._calcul(b, T0)["motif_code"] == "ligne_absente"


def test_hors_perimetre_separe_et_journal_retrospectif_preserve():
    b = boost(long_terme=True)
    registre = {}
    observer({"1": b}, registre)
    stats = registre["bilan"]
    assert stats["decisions_courantes"]["hors_perimetre"] == 1
    assert stats["decisions_courantes"]["abstention"] == 0
    assert stats["motifs_courants"]["long_terme"] == 1
    assert stats["paris_selectionnes"] == 0
    # Historique ancien : il reste lisible et aucune décision n'est reconstruite rétroactivement.
    ancien = {"schema": 1, "entrees": {"ancien": {
        "id": "ancien", "historique": [{"decision": "abstention", "cote": 2,
          "ev_pct": None, "cote_juste": None, "mise_fictive": None,
          "raisons": ["Paris long terme ou horaire non vérifiable"]}],
        "premiere_selection": None
    }}}
    vieux = cerveau.bilan(ancien, {})
    assert vieux["decisions_courantes"]["abstention"] == 1
    assert vieux["motifs_courants"]["ancien_format"] == 1
