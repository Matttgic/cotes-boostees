# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (498 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 498 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 360 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (557 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 557 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 319 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 27/10 18h17 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 739 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 739 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 509 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 666 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 587 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 409 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
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

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 446 en attente · cote moyenne 3,45 · pire série perdante 22

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
| non évaluable | 196 / 634 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 28 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 12 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 11 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 56 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 168 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 464 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 60 | 0 € | +0,00 € | – | – |
| match | 293 / 679 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 1.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 1.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 10 € | 7 / 28 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 2 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 12.5 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.88 € | 1 / 2 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.5 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.63 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.77 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 493 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 23.8 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 52 / 169 | 1300 € | +31,25 € | +2,4 % | 39 % |
| 3.12 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 3.22 € | 0 / 1 | 0 € | +0,00 € | – | – |
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
| 8.33 € | 1 / 4 | 8 € | -8,33 € | -100,0 % | 0 % |
| 9.09 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 13 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 305 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 347 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 55 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 19 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 8 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 12 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 102 | 265 € | -68,00 € | -25,7 % | 25 % |
| Foot américain | 0 / 1 | 0 € | +0,00 € | – | – |
| Football | 159 / 385 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 16 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 5 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 4 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 54 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 3 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 12 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 6 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 14 | 180 € | +84,00 € | +46,7 % | 56 % |
| Ski Alpin | 0 / 1 | 0 € | +0,00 € | – | – |
| Tennis | 40 / 107 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 6 | 120 € | -25,00 € | -20,8 % | 17 % |
| UFC/MMA | 0 / 1 | 0 € | +0,00 € | – | – |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 739 | 6002 € | -235,78 € | -3,9 % | 32 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 28/10 18h30 · Besiktas JK - Olympiakos | Aleksandar Vezenkov marque 25 points ou + | 3,1 | – | – | 20 € | ⏳ |
| 28/10 15h10 · Djokovic, Novak - Humbert, Ugo | Novak Djokovic gagne 2-0 | 1,9 | – | – | 20 € | ⏳ |
| 28/10 04h10 · Los Angeles Lakers - Portland Trail Blazers | Luka Doncic marque au moins 30 points et Los Angeles Lakers gagne | 2,4 | – | – | 20 € | ⏳ |
| 28/10 01h10 · NBA | San Antonio Spurs et New York Knicks gagnent chacun par au moins 7 points d'écart (respectivement contre Sacramento Kings et Detroit Pistons) | 2,7 | – | – | 20 € | ⏳ |
| 28/10 01h00 · NY Knicks - DET Pistons | NBA - Jalen Brunson finit meilleur marqueur du match | 2,4 | – | – | 25 € | ⏳ |
| 28/10 00h40 · Boston Celtics - Brooklyn Nets | Jayson Tatum et Michael Porter Jr. marquent au moins 25 points chacun | 4,0 | – | – | 20 € | ⏳ |
| 27/10 21h15 · Sporting Portugal - Maritimo | Sporting Portugal gagne le match 1-0, 2-0 ou 3-0 (hors prol. et TAB) | 3,25 | – | – | 20 € | ⏳ |
| 27/10 21h00 · Fleetwood Town - Arsenal | Arsenal gagne le match 0-4, 0-5 ou 0-6 (hors prol. et TAB) | 4,1 | – | – | 20 € | ⏳ |
| 27/10 21h00 · Villarreal - Espanyol | Villarreal gagne, les 2 équipes marquent & plus de 3.5 buts | 3,75 | – | – | 9.09 € | ⏳ |
| 27/10 20h45 · Coupe d'Allemagne | Chaque équipe à domicile gagne (4 matchs à 20h45) (hors prol. et TAB) | 5,0 | – | – | 20 € | ⏳ |
| 27/10 20h45 · Torino - Come | Nico Paz buteur et Come gagne | 4,0 | – | – | 20 € | ⏳ |
| 27/10 20h45 · AS Rome - Cagliari | Donyell Malen premier buteur du match | 3,5 | – | – | 20 € | ⏳ |
| 27/10 20h45 · Borussia Dortmund - Werder Brême | Serhou Guirassy marque 2 buts ou plus (hors prol. et TAB) | 4,25 | – | – | 20 € | ⏳ |
| 27/10 20h45 · DFB Pokal | Plus de 2.5 buts dans chacun des 4 matchs de 20h45 | 4,0 | – | – | 8.33 € | ⏳ |
| 27/10 20h00 · Synerglace Ligue Magnus | Plus de 4,5 buts dans chacun des 6 matchs du jour (prol. et TAB inclus) | 5,0 | – | – | 20 € | ⏳ |
| 27/10 20h00 · Flavio Cobolli - Grigor Dimitrov | Flavio Cobolli gagne 2-0 | 2,25 | – | – | 20 € | ⏳ |
| 27/10 20h00 · Serie B | Plus de 1,5 buts dans chacun des 6 matchs à 20h00 | 4,5 | – | – | 20 € | ⏳ |
| 27/10 19h15 · S. Wawrinka - J. Lehecka | Wawrinka gagne au moins 1 set | 2,25 | – | – | 20 € | ⏳ |
| 27/10 18h30 · CB - Serie A (27/10) | Lazio Rome+As Rome+Como 1907 marquent au moins 7 buts en cumulé ? | 2,3 | – | – | 25 € | ⏳ |
| 27/10 18h30 · Sassuolo - Lazio Rome | Lazio Rome gagne et les deux équipes marquent | 3,75 | – | – | 20 € | ⏳ |
| 27/10 18h00 · Coupe d'Allemagne | Eintracht Francfort et Augsbourg gagnent et plus de 2,5 buts dans chaque match (hors prol. et TAB) | 4,5 | – | – | 20 € | ⏳ |
| 27/10 17h00 · Dubai - Paris Basketball | Paris Basketball ne perd pas ou perd de 7 points ou moins et Tyson Etienne marque au moins 15 points | 3,5 | – | – | 20 € | ⏳ |
| 27/10 17h00 · Dubai Basketball - Paris Basketball | Elie Okobo marque 15 points ou + | 2,25 | – | – | 20 € | ⏳ |
| 27/10 15h45 · Mpetshi Perricard, Giovanni - Fils, Arthur | Arthur Fils gagne 2-0 | 1,8 | – | – | 20 € | ⏳ |
| 27/10 15h35 · G.Mpetshi - A.Fils | Les 2 joueurs gagnent un set ? | 2,5 | – | – | 25 € | ⏳ |
| 27/10 15h10 · Giovanni Mpetshi Perricard - Arthur Fils | Arthur Fils mène après 4 jeux lors du match | 4,0 | – | – | 20 € | ⏳ |
| 27/10 15h00 · Salavat Yulaev Ufa - Sotchi | Sheldon Rempal marque au moins 2 points | 2,25 | – | – | 20 € | ⏳ |
| 27/10 14h40 · Karen Khachanov - Carlos Alcaraz | Carlos Alcaraz gagne et plus de 21,5 jeux dans le match | 2,4 | – | – | 20 € | ⏳ |
| 27/10 13h10 · Jerome Kym - Arthur Rinderknech | Arthur Rinderknech gagne 2-0 | 3,6 | – | – | 20 € | ⏳ |
| 27/10 10h30 · Samsung Lions - KIA Tigers | KIA Tigers gagne la 1ère manche | 3,5 | – | – | 20 € | ⏳ |
| 27/10 03h10 · Denver Nuggets - Golden State Warriors | Stephen Curry termine meilleur marqueur du match | 3,25 | – | – | 20 € | ⏳ |
| 27/10 03h00 · DEN Nuggets - GS Warriors | NBA - Nikola Jokic marque 30 pts ou + et son équipe gagne le match | 3,0 | – | – | 25 € | ⏳ |
| 27/10 02h40 · Edmonton Oilers - Detroit Red Wings | C. McDavid buteur et Edmonton Oilers gagne (hors prol. et TAB) | 3,15 | – | – | 20 € | ⏳ |
| 27/10 01h15 · Philadelphia Eagles - Dallas Cowboys | George Pickens marque au moins un touchdown et Dallas Cowboys gagne | 3,25 | – | – | 20 € | ⏳ |
| 27/10 01h10 · New York Rangers - Los Angeles Kings | New York Rangers gagne et plus de 5,5 buts dans le match | 3,85 | – | – | 20 € | ⏳ |
| 27/10 01h10 · Golden State Valkyries - Atlanta Dream | Angel Reese marque au moins 15 points et Atlanta Dream gagne | 3,15 | – | – | 20 € | ⏳ |
| 27/10 01h10 · Oklahoma City Thunder - Phoenix Suns | Shai Gilgeous-Alexander marque au moins 30 points et distribue au moins 7 passes décisives | 2,85 | – | – | 20 € | ⏳ |
| 27/10 00h40 · NBA | Giannis Antetokounmpo et Jayson Tatum marquent au moins 30 points chacun (respectivement contre Dallas Mavericks et Chicago Bulls) | 3,6 | – | – | 20 € | ⏳ |
| 27/10 00h10 · Cleveland Cavaliers - Minnesota Timberwolves | Donovan Mitchell marque au moins 30 points et Cleveland Cavaliers gagne | 4,0 | – | – | 20 € | ⏳ |
| 27/10 00h10 · Cleveland Cavaliers - Minnesota Timberwolves | Anthony Edwards, Donovan Mitchell et LaMelo Ball marquent au moins 20 points chacun | 2,85 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
