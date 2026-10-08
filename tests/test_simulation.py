"""Stratégie A (mise max sur chaque boost), règlement et rapport — sans réseau."""
from datetime import datetime, timezone

from boosts import rapport, reglement, simulation


def boost(i, mise, cote, debut="2026-10-08T18:45:00+00:00", statut=None, sport="Handball"):
    b = {"id": f"winamax|{i}|{i}", "bookmaker": "Winamax", "sport": sport, "match": f"Match {i}",
         "pari": f"Pari {i}", "debut": debut, "mise_max": mise, "cote_origine": cote - 0.3,
         "cote_boostee": cote, "cote_boostee_initiale": cote}
    if statut:
        b["reglement"] = {"statut": statut}
    return b


def test_gains_a_la_mise_max():
    base = {b["id"]: b for b in [
        boost(1, 50, 2.5, statut="gagné"),       # +75
        boost(2, 20, 4.25, statut="perdu"),      # -20
        boost(3, 10, 8.0, statut="remboursé"),   # 0
        boost(4, 20, 2.4),                       # en attente
        boost(5, None, 3.0),                     # mise inconnue : pas joué
    ]}
    b = simulation.bilan(base)
    g = b["global"]
    assert g["paris"] == 4 and g["regles"] == 3 and g["en_attente"] == 1
    assert g["boosts_sans_mise_max"] == 1
    assert g["mise_totale"] == 80 and g["gain_net"] == 55.0
    assert g["roi_pct"] == 68.8
    assert g["reussite_pct"] == 50.0
    assert b["par_mise"]["50 €"]["gain_net"] == 75.0
    assert b["par_tranche_de_cote"]["5 – 10"]["rembourses"] == 1


def test_la_cote_jouee_est_celle_du_premier_passage():
    b = boost(1, 20, 3.0, statut="gagné")
    b["cote_boostee"] = 2.5                       # baissée plus tard : le parieur avait déjà 3,0
    assert simulation.pari(b)["gain"] == 40.0


def test_pire_baisse_et_serie():
    base = {}
    for i, (s, h) in enumerate([("gagné", 1), ("perdu", 2), ("perdu", 3), ("perdu", 4), ("gagné", 5)]):
        x = boost(i, 20, 2.0, debut=f"2026-10-08T{h:02d}:00:00+00:00", statut=s)
        base[x["id"]] = x
    g = simulation.bilan(base)["global"]
    assert g["pire_serie_perdante"] == 3 and g["pire_baisse"] == -60.0


def test_lecture_reponse_claude():
    t = 'Voici : {"statut": "Gagne", "score": "32-30", "explication": "ok", "sources": ["https://a.fr", "x"]}'
    v = reglement.lire_reponse(t)
    assert v["statut"] == "gagné" and v["sources"] == ["https://a.fr"]
    assert reglement.lire_reponse("pas de json")["statut"] == "inconnu"
    assert reglement.lire_reponse('{"statut": "peut-être"}')["statut"] == "inconnu"


def test_selection_des_boosts_a_regler():
    t = datetime(2026, 10, 9, 12, 0, tzinfo=timezone.utc)
    base = {b["id"]: b for b in [
        boost(1, 20, 2.0, debut="2026-10-09T10:00:00+00:00"),            # trop récent (< 4 h)
        boost(2, 20, 2.0, debut="2026-10-08T18:00:00+00:00"),            # à régler
        boost(3, 20, 2.0, debut="2026-10-08T18:00:00+00:00", statut="perdu"),
    ]}
    base["winamax|4|4"] = {**boost(4, 20, 2.0, debut="2026-10-08T17:00:00+00:00"),
                           "reglement": {"tentatives": 1, "derniere_tentative": "2026-10-09T09:00:00+00:00"}}
    assert [b["id"] for b in reglement.a_regler(base, t)] == ["winamax|2|2"]


def test_inconnu_ne_regle_pas_et_passe_a_la_main():
    b = boost(1, 20, 2.0)
    t = datetime(2026, 10, 9, tzinfo=timezone.utc)
    for _ in range(reglement.MAX_TENTATIVES):
        reglement.appliquer(b, {"statut": "inconnu", "score": "", "explication": "", "sources": []}, t)
    assert "statut" not in b["reglement"] and b["reglement"]["a_la_main"] is True
    assert simulation.statut(b) == "en attente"


def test_choix_du_modele(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-test")
    assert reglement.fournisseur() == "openai"
    assert reglement.modele("openai", 0) == "gpt-6-luna"
    assert reglement.modele("openai", 2) == "gpt-6.1-sol"     # le modèle éco n'a pas su trancher
    monkeypatch.delenv("OPENAI_API_KEY")
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    assert reglement.fournisseur() is None


def test_reglement_manuel_prioritaire():
    b = boost(1, 20, 2.0, statut="perdu")
    base = {b["id"]: b}
    assert reglement.appliquer_manuels(base, {b["id"]: "Gagné", "inconnu": "perdu"}, "t") == 1
    assert b["reglement"]["statut"] == "gagné" and b["reglement"]["source"] == "manuel"


def test_consigne_contient_le_pari_et_les_regles():
    c = reglement.consigne(boost(1, 20, 2.0, sport="Hockey sur glace"))
    assert "Pari 1" in c and "temps réglementaire" in c and "08/10/2026 20h45" in c


def test_rapport_markdown():
    base = {b["id"]: b for b in [boost(1, 50, 2.5, statut="gagné"), boost(2, 20, 4.25)]}
    md = rapport.markdown(simulation.strategies(base), "2026-10-08T18:00:00+00:00")
    assert "+75,00 €" in md and "ROI" in md and "⏳" in md


def test_appel_openai_simule():
    """Chemin complet avec un faux client OpenAI (aucun appel réseau)."""
    from types import SimpleNamespace as NS

    class Faux:
        class responses:
            @staticmethod
            def create(**kw):
                assert kw["tools"][0]["type"] == "web_search" and "Pari 1" in kw["input"]
                return NS(output=[NS(type="web_search_call"), NS(type="web_search_call"), NS(type="message")],
                          output_text='{"statut": "perdu", "score": "28-30", "explication": "x", "sources": []}',
                          usage=NS(input_tokens=1200, output_tokens=80))

    b = boost(1, 20, 2.0)
    verdict, usage = reglement.demander("openai", Faux, b)
    assert verdict["statut"] == "perdu" and usage["recherches"] == 2 and usage["modele"] == "gpt-6-luna"
    reglement.appliquer(b, verdict, datetime(2026, 10, 9, tzinfo=timezone.utc), usage["modele"])
    assert simulation.pari(b)["gain"] == -20.0
