"""BILAN.md : les stratégies A et B, lisibles dans l'appli GitHub (branche `donnees`)."""
from __future__ import annotations

from datetime import datetime

from .simulation import PARIS

SYMBOLES = {"gagné": "✅", "perdu": "❌", "remboursé": "↩️", "en attente": "⏳"}
NOMS = {
    "A": "A — tout miser",
    "B_exacte": "B-exacte (EV ≥ 5 %)",
    "B_approx": "B-approx (EV ≥ 5 %)",
    "C_plafond": "C — 10 € maximum",
    "D_moderee": "D — cote 1,60–3,50",
    "E_48h": "E — dans les 48 h",
    "F_ev8": "F — EV exacte ≥ 8 %",
    "G_kelly": "G — quart Kelly",
    "H_1_match": "H — un boost/match",
}


def _e(x) -> str:
    return "–" if x is None else f"{x:+.2f} €".replace(".", ",")


def _pct(x) -> str:
    return "–" if x is None else f"{x:+.1f} %".replace(".", ",")


def _n(x) -> str:
    return "–" if x is None else str(x).replace(".", ",")


def _heure(iso: str | None) -> str:
    if not iso:
        return "?"
    return datetime.fromisoformat(iso).astimezone(PARIS).strftime("%d/%m %Hh%M")


def _tableau(titre: str, groupes: dict) -> list[str]:
    lignes = [f"### {titre}", "", "| | Paris réglés | Misé | Gain net | ROI | Réussite |", "|---|---|---|---|---|---|"]
    for nom, g in groupes.items():
        reussite = "–" if g["reussite_pct"] is None else f"{g['reussite_pct']:.0f} %"
        lignes.append(f"| {nom} | {g['regles']} / {g['paris']} | {g['mise_totale']:.0f} € | {_e(g['gain_net'])} "
                      f"| {_pct(g['roi_pct'])} | {reussite} |")
    return lignes + [""]


def markdown(bilans: dict, maj: str) -> str:
    a = bilans["A"]
    g = a["global"]
    l = ["# Bilan des cotes boostées (stratégies et risques)", "",
         f"Mis à jour le {_heure(maj)} (heure de Paris). Argent fictif : A/B à la mise max ; C-H "
         "avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.", "",
         "| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |", "|---|---|---|---|---|---|"]
    for k, b in bilans.items():
        x = b["global"]
        l.append(f"| **{NOMS.get(k, k)}** | {x['regles']} / {x['paris']} | {x['mise_totale']:.0f} € "
                 f"| **{_e(x['gain_net'])}** | **{_pct(x['roi_pct'])}** | {_e(x['pire_baisse'])} |")
    l += ["",
          "**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; "
          "E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % "
          "et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec "
          "un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. "
          "Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. "
          "Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.",
          "",
          "**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, "
          "les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé "
          "peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de "
          "probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.", ""]
    l += ["",
          "- **A** : chaque boost publié.",
          "- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins "
          "+5 % d'EV, calcul exact (un seul pari, ou des matchs différents).",
          "- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien "
          "entre les conditions ignoré).", "",
          f"A en détail : {g['gagnes']} gagnés, {g['perdus']} perdus, {g['rembourses']} remboursés, "
          f"{g['en_attente']} en attente · cote moyenne {_n(g['cote_moyenne'])} · pire série perdante "
          f"{g['pire_serie_perdante']}"]
    if g["boosts_sans_mise_max"]:
        l.append(f"⚠️ {g['boosts_sans_mise_max']} boost(s) sans mise max lisible, non joués.")
    l += ["", "> Simulation uniquement. Les paris sportifs comportent un risque de perte. "
          "Joueurs Info Service : 09 74 75 13 13.", ""]
    l += _tableau("A par valeur face à Pinnacle (le filtre B marche-t-il ?)", a["par_valeur"])
    l += _tableau("A par bookmaker", a["par_bookmaker"])
    l += _tableau("A par horizon (paris de saison réglés en fin de saison)", a["par_horizon"])
    l += _tableau("A par mise max", a["par_mise"])
    l += _tableau("A par tranche de cote", a["par_tranche_de_cote"])
    l += _tableau("A par sport", a["par_sport"])
    l += _tableau("A par mois", a["par_mois"])
    l += ["### Derniers paris", "", "| Match | Pari | Cote | Juste | EV | Mise | Résultat |",
          "|---|---|---|---|---|---|---|"]
    for p in reversed(a["paris"][-40:]):
        res = SYMBOLES[p["statut"]] + ("" if p["gain"] is None else f" {_e(p['gain'])}")
        pari = (p["pari"] or "").replace("|", "/")
        ev = "–" if p["ev_pct"] is None else _pct(p["ev_pct"]) + ("" if p["valeur"] == "exacte" else " ≈")
        l.append(f"| {_heure(p['debut'])} · {p['match']} | {pari} | {_n(p['cote'])} | {_n(p['cote_juste'])} "
                 f"| {ev} | {p['mise']:g} € | {res} |")
    l += ["", "≈ : calcul approché (conditions liées sur un même match)."]
    return "\n".join(l) + "\n"
