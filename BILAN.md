# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (74 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 47 / 74 | 970 € | **-221,50 €** | **-22,8 %** | -15,1 % (23 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 31 / 51 | 310 € | **-82,00 €** | **-26,5 %** | -17,0 % (16 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (35 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 11 / 35 | 225 € | +5,00 € | +2,2 % |
| **I — cotes modérées, un boost/match** | 8 / 22 | 80 € | -15,00 € | -18,8 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 14/10 17h51 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 154 / 217 | 3195 € | **-336,00 €** | **-10,5 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 4 / 4 | 80 € | **+145,00 €** | **+181,2 %** | -20,00 € |
| **C — 10 € maximum** | 154 / 217 | 1540 € | **-159,50 €** | **-10,4 %** | -337,50 € |
| **D — cote 1,60–3,50** | 106 / 149 | 1060 € | **-93,50 €** | **-8,8 %** | -238,00 € |
| **E — dans les 48 h** | 154 / 181 | 1540 € | **-159,50 €** | **-10,4 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 145 / 166 | 1450 € | **-126,00 €** | **-8,7 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 99 / 113 | 990 € | **-80,00 €** | **-8,1 %** | -221,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 35 / 36 | 337 € | **-40,17 €** | **-11,9 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 44 / 46 | 425 € | **+51,73 €** | **+12,2 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 47 / 49 | 289 € | **+25,69 €** | **+8,9 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 29 / 31 | 545 € | **+209,77 €** | **+38,5 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 45 gagnés, 108 perdus, 1 remboursés, 63 en attente · cote moyenne 3,37 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 3 / 4 | 60 € | +0,00 € | +0,0 % | 33 % |
| EV 10 % et + (approx) | 2 / 2 | 40 € | +30,00 € | +75,0 % | 50 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 22 / 24 | 440 € | -222,00 € | -50,5 % | 18 % |
| EV < 0 (exacte) | 22 / 22 | 450 € | +216,50 € | +48,1 % | 46 % |
| non évaluable | 102 / 162 | 2145 € | -455,50 € | -21,2 % | 27 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 0 / 4 | 0 € | +0,00 € | – | – |
| NetBet | 0 / 1 | 0 € | +0,00 € | – | – |
| OlyBet | 0 / 4 | 0 € | +0,00 € | – | – |
| Unibet | 23 / 62 | 575 € | -85,00 € | -14,8 % | 35 % |
| Winamax | 131 / 146 | 2620 € | -251,00 € | -9,6 % | 28 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 36 | 0 € | +0,00 € | – | – |
| match | 154 / 181 | 3195 € | -336,00 € | -10,5 % | 29 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 20 € | 131 / 150 | 2620 € | -251,00 € | -9,6 % | 28 % |
| 20.83 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 23 / 62 | 575 € | -85,00 € | -14,8 % | 35 % |
| 6.25 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 8.33 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 4 | 0 € | +0,00 € | – | – |
| 2 – 3 | 59 / 87 | 1275 € | -16,00 € | -1,3 % | 40 % |
| 3 – 5 | 87 / 104 | 1760 € | -360,00 € | -20,5 % | 23 % |
| 5 – 10 | 8 / 14 | 160 € | +40,00 € | +25,0 % | 25 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| Baseball | 4 / 5 | 80 € | -32,00 € | -40,0 % | 25 % |
| Basketball | 8 / 36 | 160 € | -118,00 € | -73,8 % | 12 % |
| Football | 80 / 106 | 1665 € | -288,00 € | -17,3 % | 26 % |
| Football Américain | 5 / 5 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 2 / 3 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 14 / 17 | 280 € | -105,00 € | -37,5 % | 21 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XIII | 0 / 1 | 0 € | +0,00 € | – | – |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 26 / 27 | 550 € | +362,50 € | +65,9 % | 56 % |
| Tennis de table | 1 / 2 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 154 / 217 | 3195 € | -336,00 € | -10,5 % | 29 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 20/10 19h00 · Paris Trashtalk 26/27 | IND Pacers - Les Pacers remportent la Division Centrale | 4,25 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MEM Grizzlies - Cameron Boozer prend 8 rebonds ou + (moyenne) | 1,8 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | LA Clippers - Darius Garland fait 7 passes ou + (moyenne) | 1,6 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | HOU Rockets - Fred VanVleet fait 6 passes ou + (moyenne) | 2,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | BOS Celtics - Les Celtics se qualifient pour les Finales NBA | 7,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | POR TBlazers - Les Blazers ne se qualifient pas pour les Playoffs | 2,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | PHX Suns - Les Suns se qualifient pour les Playoffs | 1,66 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | GS Warriors - Les Warriors se qualifient pour les Playoffs | 1,58 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | DAL Mavericks - Les Mavericks se qualifient pour le PlayIn | 2,15 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | ATL Hawks - Dyson Daniels meilleur intercepteur NBA en saison régulière (moyenne interceptions/match, perdant si moins de 58 matchs joués) | 6,4 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | WAS Wizards - Trae Young meilleur passeur NBA en saison régulière (moyenne passes/match, perdant si moins de 58 matchs joués) | 3,3 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | TOR Raptors - Scottie Barnes meilleur passeur des Raptors (total de passes) | 2,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | BKN Nets - Mikel Brown Jr meilleur passeur des Nets (total de passes) | 3,3 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MIN TWolves - Rudy Gobert meilleur rebondeur NBA en saison régulière (moyenne rebonds/match, perdant si moins de 58 matchs joués) | 11,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CHA Hornets - Moussa Diabate meilleur rebondeur des Hornets (total de rebonds) | 1,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | UTA Jazz - Darryn Peterson meilleur marqueur du Jazz (total de points) | 7,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | ORL Magic - Paolo Banchero meilleur marqueur du Magic (total de points) | 1,6 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | NO Pelicans - Zion Williamson meilleur marqueur des Pelicans (total de points) | 2,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MIL Bucks - Tyler Herro meilleur marqueur des Bucks (total de points) | 1,35 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | LA Lakers - Luka Doncic meilleur marqueur NBA en saison régulière (moyenne points/match, perdant si moins de 58 matchs joués) | 1,87 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CHI Bulls - Caleb Wilson meilleur marqueur des Bulls (total de points) | 5,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | SA Spurs - Les Spurs finissent champions NBA | 4,2 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MIA Heat - Le Heat remporte la Division Sud-Est | 3,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CLE Cavaliers - Les Cavaliers remportent la Division Centrale | 3,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | SAC Kings - Maxime Raynaud meilleur rebondeur des Kings (total de rebonds) | 2,5 | – | – | 25 € | ⏳ |
| 15/10 18h45 · CSKA Sofia - Monaco | Monaco gagne 3-0 | 10,5 | – | – | 20 € | ⏳ |
| 15/10 18h45 · Lyon - Crystal Palace | Pavel Sulc Décisif | 2,15 | – | – | 20 € | ⏳ |
| 15/10 11h05 · Australie - NlleZélande | Le duo Jamayne Isaako/Tom Trbojevic marque 2 essais ou + | 2,8 | – | – | 25 € | ⏳ |
| 15/10 02h00 · Los Angeles Dodgers - Milwaukee Brewers | Los Angeles Dodgers gagne et moins de 8,5 runs dans le match | 2,5 | 2,695 | -7,2 % ≈ | 20 € | ⏳ |
| 14/10 21h00 · Man. City - Paris SG | R.Cherki décisif et les deux équipes marquent (remboursé si non titulaire) | 2,4 | – | – | 25 € | ⏳ |
| 14/10 21h00 · CB - ChampionsLeague (14/10) | Man.City ou Paris SG ou Real Madrid ou Dortmund marque le but le plus rapide du Multiplex de 21h (7 matchs) ? | 3,0 | – | – | 25 € | ⏳ |
| 14/10 21h00 · AS Rome - Real Madrid | Real Madrid gagne le match et les deux équipes marquent ? | 3,05 | 2,907 | +4,9 % ≈ | 25 € | ⏳ |
| 14/10 21h00 · Man. City - Paris SG | Man. City ou Paris SG gagne et au moins 4 buts marqués dans le match ? | 2,7 | – | – | 25 € | ⏳ |
| 14/10 21h00 · Manchester City - Paris SG | E. Haaland buteur sur une passe de R. Cherki | 6,5 | – | – | 20 € | ⏳ |
| 14/10 21h00 · Manchester City - Paris SG | K. Kvaratskhelia + D. Doué + O. Dembélé marquent 2 buts ou plus | 3,25 | – | – | 20 € | ⏳ |
| 14/10 21h00 · AS Rome - Real Madrid | K. Mbappe buteur et Real Madrid gagne | 2,5 | – | – | 20 € | ⏳ |
| 14/10 21h00 · O.Dembélé décisif et le PSG - City | O.Dembélé décisif et le PSG (vs City) ne perd pas ? | 2,75 | – | – | 10 € | ⏳ |
| 14/10 21h00 · Manchester City - Paris SG | Le PSG gagne 1-0 | 15,0 | – | – | 20 € | ⏳ |
| 14/10 20h45 · Paris - Virtus Bologne | Euroleague - Nadir Hifi finit meilleur marqueur du match | 2,4 | – | – | 25 € | ⏳ |
| 14/10 20h45 · Paris Basketball - Virtus Bologne | N. Hifi marque au moins 20 points et Paris Basketball gagne | 2,75 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
