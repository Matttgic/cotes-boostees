"""BILAN.md : le bilan de la stratégie A, lisible dans l'appli GitHub (branche `donnees`)."""
from __future__ import annotations

from datetime import datetime

from .simulation import PARIS

SYMBOLES = {"gagné": "✅", "perdu": "❌", "remboursé": "↩️", "en attente": "⏳"}


def _e(x) -> str:
    return "–" if x is None else f"{x:+.2f} €".replace(".", ",")


def _pct(x) -> str:
    return "–" if x is None else f"{x:+.1f} %".replace(".", ",")


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


def markdown(b: dict, maj: str) -> str:
    g = b["global"]
    l = ["# Bilan — toutes les cotes boostées à la mise max", "",
         f"Mis à jour le {_heure(maj)} (heure de Paris). Argent fictif : un pari par boost, à la mise max, "
         "à la cote boostée vue au premier passage.", "",
         f"- **Gain net : {_e(g['gain_net'])}** sur {g['mise_totale']:.0f} € misés → **ROI {_pct(g['roi_pct'])}**",
         f"- Paris : {g['paris']} ({g['gagnes']} gagnés, {g['perdus']} perdus, {g['rembourses']} remboursés, "
         f"{g['en_attente']} en attente)",
         f"- Cote moyenne : {str(g['cote_moyenne']).replace('.', ',')} · pire baisse : {_e(g['pire_baisse'])} "
         f"· pire série perdante : {g['pire_serie_perdante']}"]
    if g["boosts_sans_mise_max"]:
        l.append(f"- ⚠️ {g['boosts_sans_mise_max']} boost(s) sans mise max lisible, non joués")
    l += ["", "> Simulation uniquement. Les paris sportifs comportent un risque de perte. "
          "Joueurs Info Service : 09 74 75 13 13.", ""]
    l += _tableau("Par bookmaker", b["par_bookmaker"])
    l += _tableau("Par mise max", b["par_mise"])
    l += _tableau("Par tranche de cote", b["par_tranche_de_cote"])
    l += _tableau("Par sport", b["par_sport"])
    l += _tableau("Par mois", b["par_mois"])
    l += ["### Derniers paris", "", "| Match | Pari | Cote | Mise | Résultat |", "|---|---|---|---|---|"]
    for p in reversed(b["paris"][-40:]):
        res = SYMBOLES[p["statut"]] + ("" if p["gain"] is None else f" {_e(p['gain'])}")
        pari = (p["pari"] or "").replace("|", "/")
        l.append(f"| {_heure(p['debut'])} · {p['match']} | {pari} | {str(p['cote']).replace('.', ',')} "
                 f"| {p['mise']:g} € | {res} |")
    return "\n".join(l) + "\n"
