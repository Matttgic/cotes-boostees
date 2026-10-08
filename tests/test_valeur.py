"""Valeur des boosts face à Pinnacle (lignes au format de boosts/pinnacle.py) et lecture des jambes."""
import pytest

from boosts import jambes, simulation, valeur
from boosts.evaluation import evaluer_boosts
from boosts.marge import proba_justes


def lignes_marche(sport, mid, dom, ext, debut, marche, periode, ligne_issues, joueur=None):
    """ligne_issues : [(ligne, issue, cote)…] d'UN marché complet ; probabilités justes calculées."""
    p = proba_justes([c for _, _, c in ligne_issues])
    return [{"source": "pinnacle", "sport": sport, "ligue": "L", "match_id": mid, "domicile": dom,
             "exterieur": ext, "debut": debut, "marche": marche, "periode": periode, "ligne": li, "issue": i,
             "joueur": joueur, "cote": c, "proba_juste": pi, "cote_juste": round(1 / pi, 4)}
            for (li, i, c), pi in zip(ligne_issues, p)]


@pytest.fixture
def index():
    l = []
    l += lignes_marche("rugby", 1, "Montauban", "Brive", "2026-10-08T19:00:00Z", "HANDICAP", "MATCH",
                       [(-5.5, "DOM", 2.05), (-5.5, "EXT", 1.80)])
    l += lignes_marche("hockey", 2, "Carolina Hurricanes", "Vancouver Canucks", "2026-10-08T23:00:00Z",
                       "VAINQUEUR", "MATCH", [(None, "DOM", 1.60), (None, "EXT", 2.45)])
    l += lignes_marche("hockey", 3, "Montreal Canadiens", "Nashville Predators", "2026-10-08T23:00:00Z",
                       "VAINQUEUR", "MATCH", [(None, "DOM", 1.70), (None, "EXT", 2.25)])
    l += lignes_marche("hockey", 4, "Philadelphia Flyers", "Ottawa Senators", "2026-10-08T23:00:00Z",
                       "VAINQUEUR", "MATCH", [(None, "DOM", 2.10), (None, "EXT", 1.80)])
    l += lignes_marche("handball", 5, "MT Melsungen", "Nantes", "2026-10-08T18:45:00Z", "RESULTAT_1N2", "MATCH",
                       [(None, "DOM", 2.6), (None, "NUL", 9.0), (None, "EXT", 1.7)])
    l += lignes_marche("handball", 5, "MT Melsungen", "Nantes", "2026-10-08T18:45:00Z", "TOTAL", "MATCH",
                       [(58.5, "PLUS", 1.85), (58.5, "MOINS", 1.95)])
    l += lignes_marche("football_americain", 6, "Dallas Cowboys", "Tampa Bay Buccaneers", "2026-10-09T00:15:00Z",
                       "JOUEUR:Rushing Yards", "MATCH", [(80.5, "PLUS", 1.87), (80.5, "MOINS", 1.87)],
                       joueur="Javonte Williams")
    return valeur.Index(l)


def j(**k):
    base = {"equipe_1": None, "equipe_2": None, "type": "autre", "equipe": None, "sens": None, "ligne": None,
            "periode": "match", "unite": "buts", "joueur": None, "stat": None}
    return {**base, **k}


def boost(sport, cote, debut, origine=None):
    return {"id": "x", "sport": sport, "cote_boostee": cote, "cote_origine": origine, "debut": debut}


def test_handicap_exact(index):
    v = valeur.evaluer(boost("Rugby à XV", 2.25, "2026-10-08T19:00:00+00:00", 2.0),
                       [j(equipe_1="Montauban", equipe_2="CA Brive", type="handicap", equipe="Montauban",
                          ligne=-5.5)], index)
    assert v["statut"] == "exacte"
    p = 1 / v["cote_juste"]
    assert 0.45 < p < 0.48 and v["ev_pct"] == pytest.approx((2.25 * p - 1) * 100, abs=0.2)


def test_triple_sur_trois_matchs_est_exact(index):
    jj = [j(equipe_1="Carolina Hurricanes", equipe_2="Vancouver Canucks", type="vainqueur", equipe="Carolina Hurricanes"),
          j(equipe_1="Montreal Canadiens", equipe_2="Nashville Predators", type="vainqueur", equipe="Montreal Canadiens"),
          j(equipe_1="Ottawa Senators", equipe_2="Philadelphia Flyers", type="vainqueur", equipe="Ottawa Senators")]
    v = valeur.evaluer(boost("Hockey sur glace", 3.5, "2026-10-08T23:00:00+00:00"), jj, index)
    assert v["statut"] == "exacte" and len(v["detail"]) == 3     # Ottawa à l'extérieur : ordre inversé géré
    assert v["detail"][2]["issue"] == "EXT"


def test_combine_meme_match_est_approx(index):
    jj = [j(equipe_1="Melsungen", equipe_2="Nantes", type="resultat", equipe="Nantes"),
          j(equipe_1="Melsungen", equipe_2="Nantes", type="total", sens="plus", ligne=58.5)]
    v = valeur.evaluer(boost("Handball", 4.25, "2026-10-08T18:45:00+00:00", 3.65), jj, index)
    assert v["statut"] == "approx" and v["cote_juste"] > 3


def test_pari_joueur(index):
    v = valeur.evaluer(boost("Football Américain", 2.4, "2026-10-09T00:15:00+00:00"),
                       [j(equipe_1="Dallas Cowboys", equipe_2="Tampa Bay Buccaneers", type="joueur",
                          joueur="Javonte Williams", stat="Rushing Yards", sens="plus", ligne=80.5)], index)
    assert v["statut"] == "exacte" and v["ev_pct"] == pytest.approx(20.0, abs=0.5)   # 2,40 × 0,5


def test_non_evaluables(index):
    debut = "2026-10-08T19:00:00+00:00"
    autre_ligne = [j(equipe_1="Montauban", equipe_2="Brive", type="handicap", equipe="Montauban", ligne=-9.5)]
    assert valeur.evaluer(boost("Rugby à XV", 3, debut), autre_ligne, index)["statut"] == "non_evaluable"
    assert valeur.evaluer(boost("Rugby à XV", 3, debut), [j(type="autre")], index)["statut"] == "non_evaluable"
    inconnu = [j(equipe_1="Toulon", equipe_2="Pau", type="vainqueur", equipe="Toulon")]
    assert "introuvable" in valeur.evaluer(boost("Rugby à XV", 3, debut), inconnu, index)["raison"]
    assert valeur.evaluer(boost("Curling", 3, debut), autre_ligne, index)["statut"] == "non_evaluable"


def test_lecture_jambes():
    t = '{"jambes": [{"equipe_1": "A", "equipe_2": "B", "type": "Total", "sens": "plus", "ligne": "58,5"},' \
        ' {"type": "inventé"}]}'
    jj = jambes.lire(t)
    assert jj[0]["type"] == "total" and jj[0]["ligne"] == 58.5 and jj[1]["type"] == "autre"
    assert jambes.lire("rien") is None and jambes.lire('{"jambes": []}') is None


def test_evaluation_complete_et_strategie_b(monkeypatch, index):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    b = {"id": "winamax|1|1", "bookmaker": "Winamax", "sport": "Rugby à XV", "match": "Montauban - CA Brive",
         "pari": "Montauban gagne par au moins 6 points d'écart", "cote_origine": 2.0, "cote_boostee": 2.25,
         "cote_boostee_initiale": 2.25, "mise_max": 20, "debut": "2026-10-08T19:00:00+00:00",
         "jambes": [j(equipe_1="Montauban", equipe_2="CA Brive", type="handicap", equipe="Montauban", ligne=-5.5)]}
    base = {b["id"]: b}
    r = evaluer_boosts(base, "2026-10-08T18:00:00+00:00",
                       collecter_pinnacle=lambda ids: [l for ls in index.lignes.values() for l in ls])
    assert r["exactes"] == 1 and b["valeur_initiale"]["statut"] == "exacte"
    s = simulation.strategies(base)
    assert s["A"]["global"]["paris"] == 1
    attendu = 1 if b["valeur_initiale"]["ev_pct"] >= simulation.EV_MIN_B else 0
    assert s["B_exacte"]["global"]["paris"] == attendu and s["B_approx"]["global"]["paris"] == 0
