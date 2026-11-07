# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (845 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 845 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 632 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (969 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 969 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 586 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 07/11 17h13 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 1151 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 1151 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 833 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 1058 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 931 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 676 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
| **B — valeur ≥ +5 %** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B0 — valeur ≥ 0 %** | 3 / 3 | 50 € | **-50,00 €** | **-100,0 %** | -50,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 44 / 54 | 424 € | **+19,39 €** | **+4,6 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 62 / 74 | 605 € | **+136,73 €** | **+22,6 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 65 / 77 | 430 € | **+60,82 €** | **+14,1 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 46 / 54 | 879 € | **+381,38 €** | **+43,4 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 858 en attente · cote moyenne 3,33 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 4 / 4 | 85 € | +51,25 € | +60,3 % | 50 % |
| EV 0 à 5 % (exacte) | 1 / 1 | 10 € | -10,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 3 / 5 | 60 € | +10,00 € | +16,7 % | 33 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV 5 à 10 % (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV < 0 (approx) | 40 / 45 | 802 € | -386,70 € | -48,2 % | 20 % |
| EV < 0 (exacte) | 45 / 46 | 895 € | +237,00 € | +26,5 % | 41 % |
| non évaluable | 196 / 1046 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 51 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 22 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 19 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 80 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 245 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 734 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 75 | 0 € | +0,00 € | – | – |
| match | 293 / 1076 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 1.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 1.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 10 € | 7 / 47 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 4 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.36 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 12.5 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.15 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.51 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 13.88 € | 1 / 3 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 5 | 0 € | +0,00 € | – | – |
| 15.62 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 16.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 17.24 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 17.85 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.5 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.63 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.77 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 786 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 22.72 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 23.8 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 52 / 246 | 1300 € | +31,25 € | +2,4 % | 39 % |
| 3.12 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 3.22 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 3.57 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 3.84 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 4.16 € | 0 / 3 | 0 € | +0,00 € | – | – |
| 4.54 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5 € | 0 / 3 | 0 € | +0,00 € | – | – |
| 5.26 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5.49 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5.55 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 5.74 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5.88 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 6.25 € | 1 / 2 | 6 € | +21,88 € | +350,1 % | 100 % |
| 6.66 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 7.14 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 7.69 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 8.06 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 8.33 € | 1 / 5 | 8 € | -8,33 € | -100,0 % | 0 % |
| 8.92 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 9.09 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 9.61 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 13 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 498 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 545 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 67 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 28 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 9 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 15 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 161 | 265 € | -68,00 € | -25,7 % | 25 % |
| Foot américain | 0 / 1 | 0 € | +0,00 € | – | – |
| Football | 159 / 603 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 20 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 7 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 5 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 88 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 3 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 16 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 7 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 15 | 180 € | +84,00 € | +46,7 % | 56 % |
| Ski Alpin | 0 / 1 | 0 € | +0,00 € | – | – |
| Tennis | 40 / 184 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 13 | 120 € | -25,00 € | -20,8 % | 17 % |
| UFC/MMA | 0 / 1 | 0 € | +0,00 € | – | – |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 886 | 6002 € | -235,78 € | -3,9 % | 32 % |
| 2026-11 | 0 / 265 | 0 € | +0,00 € | – | – |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 09/11 12h00 · Vallejo, Adolfo Daniel - Humbert, Ugo | Ugo Humbert gagne 2 sets 0 | 2,0 | – | – | 20 € | ⏳ |
| 08/11 17h15 · Brest - Lyon | Keito Nakamura Décisif | 2,3 | – | – | 20 € | ⏳ |
| 08/11 15h00 · Rennes - Lille | Boulaye Dia Buteur! | 2,85 | – | – | 20 € | ⏳ |
| 08/11 02h10 · Cleveland Cavaliers - New York Knicks | Jalen Brunson + Karl-Anthony Towns marquent 50 points ou plus | 2,3 | – | – | 20 € | ⏳ |
| 07/11 23h00 · IND Pacers - DEN Nuggets | NBA - Nikola Jokic termine meilleur marqueur du match et son équipe gagne | 2,5 | – | – | 25 € | ⏳ |
| 07/11 21h10 · France - Fidji | Joyeux Anniversaire - Cameron Woki marque un essai ou + | 2,8 | – | – | 25 € | ⏳ |
| 07/11 21h05 · Paris SG - Troyes | F.Torres buteur et son équipe gagne de 3 buts ou + (remboursé si non titulaire) | 2,5 | – | – | 25 € | ⏳ |
| 07/11 21h05 · Paris SG - Troyes | Paris SG gagne et plus de 4,5 buts dans le match | 3,0 | – | – | 20 € | ⏳ |
| 07/11 21h05 · PSG/Troyes - Paris gagne 4/0, 5/0 ou 6/0 ? | PSG/Troyes - Paris gagne 4/0, 5/0 ou 6/0 ? | 4,5 | – | – | 10 € | ⏳ |
| 07/11 21h00 · CF Valence - Real Madrid | Kylian Mbappé buteur et son équipe gagne les 2 mi-temps (remboursé si non titulaire) | 3,0 | – | – | 25 € | ⏳ |
| 07/11 21h00 · Valence - Real Madrid | Real Madrid gagne le match 0-1, 0-2 ou 0-3 | 3,0 | – | – | 20 € | ⏳ |
| 07/11 20h45 · AS Rome - Sassuolo | AS Rome gagne et plus de 4,5 buts dans le match | 3,25 | – | – | 20 € | ⏳ |
| 07/11 20h00 · Ligue 2 BKT® | Pau et Saint-Etienne marquent chacun au moins 2 buts (respectivement contre Nantes et Laval) | 4,0 | – | – | 20 € | ⏳ |
| 07/11 19h00 · Auxerre - Paris FC | L.Sinayoko ou C.Archer buteur et les deux équipes marquent (remboursé si non titulaire) | 2,35 | – | – | 25 € | ⏳ |
| 07/11 19h00 · Auxerre - Paris FC | L.Sinayoko ou C.Archer buteur et les deux équipes marquent (remboursé si non titulaire) | 2,35 | – | – | 25 € | ⏳ |
| 07/11 18h30 · Nottingham Forest - Manchester City | Manchester City gagne et les deux équipes marquent | 3,25 | – | – | 20 € | ⏳ |
| 07/11 18h30 · Nottingham Forest - Manchester City | Manchester City gagne et E. Haaland buteur | 2,4 | – | – | 17.85 € | ⏳ |
| 07/11 17h15 · C.Ruud - C.Alcaraz | C.Alcaraz gagne le 1er set 6-3 ou 6-4 ? | 2,6 | – | – | 25 € | ⏳ |
| 07/11 17h00 · Casper Ruud - Carlos Alcaraz | Plus de 2,5 sets lors du match | 2,75 | – | – | 20 € | ⏳ |
| 07/11 16h00 · Arsenal - Hull City | Arsenal gagne et moins de 2,5 buts dans le match | 3,5 | – | – | 20 € | ⏳ |
| 07/11 16h00 · Arsenal - Hull City | Noni Madueke Décisif | 2,05 | – | – | 20 € | ⏳ |
| 07/11 15h30 · Multi Bundesliga 1 | Plus de 2.5 buts dans chacun des 4 matchs de 15:30 | 3,1 | – | – | 25 € | ⏳ |
| 07/11 15h30 · Bundesliga | Borussia Dortmund et Bayern Munich gagnent chacun par au moins 2 buts d'écart (respectivement contre Elversberg et Mayence) | 3,0 | – | – | 20 € | ⏳ |
| 07/11 15h30 · Bundesliga | Plus de 2,5 buts dans chacun des 4 matchs à 15h30 | 3,0 | – | – | 20 € | ⏳ |
| 07/11 14h30 · Luca Van Assche - Ben Shelton | L. Van Assche gagne le match | 3,75 | – | – | 20 € | ⏳ |
| 07/11 13h30 · Leeds - Tottenham | Tottenham gagne et plus de 2,5 buts dans le match | 4,0 | – | – | 20 € | ⏳ |
| 07/11 13h30 · Leeds - Tottenham | Tottenham mène à la mi-temps et gagne le match | 3,75 | – | – | 20 € | ⏳ |
| 07/11 09h30 · Melbourne United - Brisbane Bullets | Plus de 199,5 points lors du match | 2,5 | – | – | 20 € | ⏳ |
| 07/11 09h00 · Maria Sakkari - Alexandra Eala | Au moins un Tie-break lors du match | 2,55 | – | – | 20 € | ⏳ |
| 07/11 04h10 · Sacramento Kings - San Antonio Spurs | Victor Wembanyama marque au moins 25 points, prend au moins 10 rebonds et réalise au moins 3 contres | 2,75 | – | – | 20 € | ⏳ |
| 07/11 04h00 · SAC Kings - SA Spurs | NBA - V.Wembanyama marque 32 pts ou + et son équipe gagne | 2,65 | – | – | 25 € | ⏳ |
| 07/11 02h10 · NHL | Calgary Flames et Minnesota Wild gagnent chacun par au moins 2 buts d'écart (respectivement contre Anaheim Ducks et San Jose Sharks) | 4,5 | – | – | 20 € | ⏳ |
| 07/11 02h10 · Memphis Grizzlies - Oklahoma City Thunder | Shai Gilgeous-Alexander marque au moins 30 points et distribue au moins 7 passes décisives | 2,75 | – | – | 20 € | ⏳ |
| 07/11 01h40 · NBA | Philadelphia 76ers et Los Angeles Lakers gagnent chacun par au moins 3 points d'écart (respectivement contre Cleveland Cavaliers et Portland Trail Blazers) | 3,5 | – | – | 20 € | ⏳ |
| 07/11 01h10 · Buffalo Sabres - Columbus Blue Jackets | T. Thompson buteur et Buffalo Sabres gagne (hors prol. et TAB) | 3,25 | – | – | 20 € | ⏳ |
| 06/11 21h10 · Irlande - Argentine | Irlande gagne et Mack Hansen marque un essai ou + | 3,0 | – | – | 25 € | ⏳ |
| 06/11 21h00 · Everton - Coventry | Everton gagne et les deux équipes marquent | 3,25 | – | – | 20 € | ⏳ |
| 06/11 21h00 · FC Séville - Alaves | FC Séville gagne le match 1-0, 2-0 ou 3-0 | 3,1 | – | – | 20 € | ⏳ |
| 06/11 20h45 · Toulouse - Strasbourg | Casper Tengstedt buteur et les deux équipes marquent (remboursé si non titulaire) | 3,5 | – | – | 25 € | ⏳ |
| 06/11 20h45 · Toulouse - Strasbourg | Toulouse marque dans les deux mi-temps | 2,8 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
