import unittest
from copy import deepcopy

from boosts.recherche_strategies import observer, simuler, verrouiller_decisions


def historique():
    h = {"observations": {}, "valeurs": {}, "resultats": []}
    for i in range(30):
        identifiant = f"train-{i}"
        h["observations"][identifiant] = {
            "id": identifiant, "bookmaker": "Winamax", "sport": "Tennis", "match": identifiant,
            "pari": "Victoire", "available_at": "2026-01-01T08:00:00Z", "debut": "2026-01-01T12:00:00Z",
            "cote_boostee_initiale": 2.0, "cote_origine": 2.0, "mise_max": 20, "disponible": True}
        h["resultats"].append({"id": identifiant, "statut": "gagné" if i < 20 else "perdu",
                              "available_at": "2026-01-01T20:00:00Z"})
    return h


def cible(h, identifiant="target", date="2026-01-02T08:00:00Z", match=None):
    h["observations"][identifiant] = {
        "id": identifiant, "bookmaker": "Winamax", "sport": "Tennis", "match": match or identifiant,
        "pari": "Victoire", "available_at": date, "debut": "2026-01-02T12:00:00Z",
        "cote_boostee_initiale": 2.0, "cote_origine": 2.0, "mise_max": 20, "disponible": True}


class RechercheChronologique(unittest.TestCase):
    def test_modifier_resultats_futurs_ne_change_aucune_decision_anterieure(self):
        h = historique()
        for i in range(4):
            cible(h, f"target-{i}")
            h["resultats"].append({"id": f"target-{i}", "statut": "gagné", "available_at": "2026-01-03T08:00:00Z"})
        other = deepcopy(h)
        for r in other["resultats"][-4:]:
            r["statut"] = "perdu"
        for policy in ("modele", "adaptative"):
            a, b = simuler(h, policy), simuler(other, policy)
            self.assertEqual(a["replay"]["decisions"], b["replay"]["decisions"])
            self.assertEqual([p["mise"] for p in a["paris"]], [p["mise"] for p in b["paris"]])

    def test_resultats_du_meme_scan_arrivent_apres_decision(self):
        h = historique()
        cible(h, "same-scan", "2026-01-01T20:00:00Z")
        cible(h, "later", "2026-01-01T20:01:00Z")
        r = simuler(h)
        ids = [d["id"] for d in r["replay"]["decisions"]]
        self.assertNotIn("same-scan", ids)
        self.assertIn("later", ids)
        for d in r["replay"]["decisions"]:
            self.assertLess(d["dernier_resultat_utilise"], d["date"])

    def test_fonds_immobilises_et_limites_d_exposition(self):
        h = historique()
        for i in range(25):
            cible(h, f"target-{i:02d}")
        r = simuler(h, "temoin")
        self.assertEqual(len(r["paris"]), 10)
        self.assertEqual(r["replay"]["mises_ouvertes"], 100)
        self.assertEqual(r["replay"]["cash_final"], 900)
        self.assertEqual(r["replay"]["banque_finale"], 1000)

    def test_aucun_prix_de_match_deja_commence(self):
        h = historique()
        cible(h, date="2026-01-02T13:00:00Z")
        self.assertEqual(simuler(h)["global"]["paris"], 0)

    def test_concentration_et_apprentissage_independants_du_gagnant(self):
        h = historique()
        cible(h, "a", match="A - B")
        cible(h, "b", match="A - B")
        h["resultats"].extend([{"id": "a", "statut": "perdu", "available_at": "2026-01-03T08:00:00Z"},
                              {"id": "b", "statut": "gagné", "available_at": "2026-01-03T08:00:00Z"}])
        self.assertEqual([p["id"] for p in simuler(h)["paris"]], ["a"])

    def test_snapshot_utilise_le_prix_accessible_et_reste_immuable(self):
        h = {"observations": {}, "valeurs": {}, "resultats": []}
        b = {"id": "live", "bookmaker": "Winamax", "sport": "Tennis", "match": "A - B",
             "debut": "2026-01-02T12:00:00Z", "derniere_vue": "2026-01-02T08:00:00Z",
             "disponible": True, "cote_boostee_initiale": 3.0, "cote_boostee": 2.2, "mise_max": 20,
             "valeur_initiale": {"statut": "exacte", "date": "2026-01-01T08:00:00Z", "cote_boostee": 3.0}}
        observer({"live": b}, h, "2026-01-02T08:00:00Z")
        self.assertEqual(h["observations"]["live"]["cote_boostee_initiale"], 2.2)
        self.assertNotIn("live", h["valeurs"])
        b["cote_boostee"] = 8.0
        observer({"live": b}, h, "2026-01-02T09:00:00Z")
        self.assertEqual(h["observations"]["live"]["cote_boostee_initiale"], 2.2)

    def test_correction_connue_plus_tard_ne_change_pas_le_passe(self):
        h = historique()
        cible(h)
        other = deepcopy(h)
        other["resultats"].append({"id": "train-0", "statut": "perdu", "available_at": "2026-01-04T08:00:00Z"})
        self.assertEqual(simuler(h)["replay"]["decisions"], simuler(other)["replay"]["decisions"])

    def test_journal_prospectif_refuse_de_recrire_les_mises(self):
        h = {}
        d = {"id": "a", "date": "2026-10-14T08:00:00Z", "joue": True,
             "p_modele": 0.6, "ev_modele_pct": 20, "regle": None}
        r = {"prospectif": {"strategies": {"K": {"paris": [{"id": "a", "mise": 10}], "replay": {"decisions": [d]}}}}}
        verrouiller_decisions(h, r)
        r["prospectif"]["strategies"]["K"]["paris"][0]["mise"] = 20
        with self.assertRaises(ValueError):
            verrouiller_decisions(h, r)

    def test_value_tardive_ne_remonte_pas_dans_le_modele(self):
        h = historique()
        cible(h)
        without = simuler(h)
        h["valeurs"]["target"] = {"statut": "exacte", "available_at": "2026-01-02T13:00:00Z",
                                    "date": "2026-01-02T13:00:00Z", "cote_boostee": 2.5,
                                    "cote_juste": 2.0, "ev_pct": 25}
        self.assertEqual(without["replay"]["decisions"], simuler(h)["replay"]["decisions"])
        self.assertEqual(simuler(h, "valeur")["global"]["paris"], 0)

    def test_scan_commence_avant_match_mais_decision_arrive_apres(self):
        h = {"observations": {}, "valeurs": {}, "resultats": []}
        b = {"id": "late", "debut": "2026-01-02T08:01:00Z", "disponible": True,
             "derniere_vue": "2026-01-02T08:00:00Z", "cote_boostee": 2, "mise_max": 20}
        observer({"late": b}, h, "2026-01-02T08:00:00Z", "2026-01-02T08:02:00Z")
        self.assertNotIn("late", h["observations"])

    def test_reglements_du_meme_instant_ne_creent_pas_de_baisse_artificielle(self):
        h = historique()
        cible(h, "a")
        cible(h, "b")
        h["observations"]["a"]["cote_boostee_initiale"] = 3
        h["resultats"].extend([{"id": "a", "statut": "gagné", "available_at": "2026-01-03T08:00:00Z"},
                              {"id": "b", "statut": "perdu", "available_at": "2026-01-03T08:00:00Z"}])
        r = simuler(h, "temoin")
        self.assertEqual(r["global"]["gain_net"], 10)
        self.assertEqual(r["global"]["pire_baisse"], 0)
        self.assertEqual(len(r["courbe"]), 1)

    def test_cohorte_future_ne_recupere_pas_une_ancienne_perte(self):
        h = historique()
        cible(h, "old")
        h["resultats"].append({"id": "old", "statut": "perdu", "available_at": "2026-01-02T18:00:00Z"})
        cible(h, "new", date="2026-01-03T08:00:00Z")
        h["observations"]["new"]["debut"] = "2026-01-03T12:00:00Z"
        r = simuler(h, "temoin", debut_paris="2026-01-03T00:00:00Z")
        self.assertEqual([p["id"] for p in r["paris"]], ["new"])
        self.assertEqual(r["paris"][0]["bankroll_avant"], 1000)
        self.assertEqual(r["global"]["gain_net"], 0)


if __name__ == "__main__":
    unittest.main()
