"""Protocole gelé : stratégies B / B0 sur la valeur au premier calcul, bilan limité aux boosts d'après le gel."""
from boosts import simulation


def boost(i, *, vu, ev=None, statut="exacte", cote=3.0, cote_calcul=None, issue=None, debut="2026-10-20T18:00:00+00:00",
          date_calcul="2026-10-19T10:00:00+00:00", mise=20):
    b = {"id": f"winamax|{i}|{i}", "bookmaker": "Winamax", "sport": "Football", "match": f"M{i}", "pari": "p",
         "debut": debut, "premiere_vue": vu, "mise_max": mise, "cote_boostee": cote, "cote_boostee_initiale": cote}
    if ev is not None:
        b["valeur_initiale"] = {"statut": statut, "ev_pct": ev, "cote_boostee": cote_calcul or cote,
                                "cote_juste": 2.5, "date": date_calcul}
    if issue:
        b["reglement"] = {"statut": issue}
    return b


AVANT, APRES = "2026-10-10T10:00:00+00:00", "2026-10-12T10:00:00+00:00"


def base(*bs):
    return {b["id"]: b for b in bs}


def test_seuils_et_statuts():
    b = base(boost(1, vu=APRES, ev=8, issue="gagné"),                    # B et B0
             boost(2, vu=APRES, ev=2, issue="perdu"),                    # B0 seulement
             boost(3, vu=APRES, ev=-4, issue="gagné"),                   # aucun
             boost(4, vu=APRES, ev=12, statut="approx", issue="gagné"),  # combiné lié : jamais
             boost(5, vu=APRES, ev=6, statut="interpolee", issue="perdu"))  # ligne interpolée : admise
    s = simulation.strategies(b)
    assert {p["id"] for p in s["B_valeur"]["paris"]} == {"winamax|1|1", "winamax|5|5"}
    assert {p["id"] for p in s["B0_valeur"]["paris"]} == {"winamax|1|1", "winamax|2|2", "winamax|5|5"}


def test_cote_d_entree_celle_du_premier_calcul():
    b = base(boost(1, vu=APRES, ev=8, cote=3.0, cote_calcul=2.8, issue="gagné"))
    p = simulation.strategies(b)["B_valeur"]["paris"][0]
    assert p["cote"] == 2.8 and p["gain"] == 36.0


def test_calcul_apres_le_coup_d_envoi_refuse():
    b = base(boost(1, vu=APRES, ev=8, date_calcul="2026-10-20T18:30:00+00:00", issue="gagné"))
    assert simulation.strategies(b)["B_valeur"]["paris"] == []


def test_protocole_ne_juge_que_l_apres_gel():
    b = base(boost(1, vu=AVANT, ev=8, issue="gagné"), boost(2, vu=APRES, ev=8, issue="perdu"),
             boost(3, vu=APRES, issue="gagné", cote=2.0, mise=20))
    p = simulation.protocole(b)
    assert p["boosts_apres_gel"] == 2 and p["date_gel"] == simulation.DATE_GEL
    assert p["apres_gel"]["B_valeur"]["global"]["gain_net"] == -20.0          # le 1 (avant gel) est exclu
    assert p["apres_gel"]["A"]["global"]["regles"] == 2
    assert p["apres_gel"]["D_moderee"]["global"]["paris"] == 2                 # cotes 3,0 et 2,0 : dans 1,60–3,50
    assert set(p["apres_gel"]) == set(simulation.SUIVIES)


def test_valeur_moyenne_jouee():
    b = base(boost(1, vu=APRES, ev=8), boost(2, vu=APRES, ev=2), boost(3, vu=APRES))
    g = simulation.bilan(b)["global"]
    assert g["ev_moyenne_pct"] == 5.0 and g["paris_avec_ev"] == 2


def test_olybet_hors_protocole_gele_mais_dans_les_strategies():
    oly = {**boost(4, vu=APRES, issue="gagné"), "id": "olybet|4|4", "bookmaker": "OlyBet"}
    b = base(boost(2, vu=APRES, issue="perdu"), oly)
    p = simulation.protocole(b)
    assert p["boosts_apres_gel"] == 1 and p["bookmakers"] == ["Winamax", "Unibet"]
    assert "OlyBet" in simulation.strategies(b)["A"]["par_bookmaker"]
