# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (181 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 154 / 181 | 3250 € | **-333,75 €** | **-10,3 %** | -16,5 % (61 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 110 / 128 | 1100 € | **-129,00 €** | **-11,7 %** | -15,6 % (42 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (159 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 132 / 159 | 2692 € | -16,83 € | -0,6 % |
| **I — cotes modérées, un boost/match** | 83 / 96 | 830 € | +4,50 € | +0,5 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 18/10 03h10 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 281 / 341 | 5757 € | **-328,28 €** | **-5,7 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 5 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 281 / 341 | 2805 € | **-139,95 €** | **-5,0 %** | -337,50 € |
| **D — cote 1,60–3,50** | 199 / 239 | 1990 € | **-30,00 €** | **-1,5 %** | -238,00 € |
| **E — dans les 48 h** | 279 / 293 | 2785 € | **-119,95 €** | **-4,3 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 249 / 267 | 2485 € | **-155,95 €** | **-6,3 %** | -322,95 € |
| **I — cotes modérées, un boost/match** | 172 / 186 | 1720 € | **-96,00 €** | **-5,6 %** | -274,50 € |
| **B — valeur ≥ +5 %** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B0 — valeur ≥ 0 %** | 3 / 3 | 50 € | **-50,00 €** | **-100,0 %** | -50,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 44 / 45 | 424 € | **+19,39 €** | **+4,6 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 60 / 65 | 585 € | **+110,73 €** | **+18,9 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 63 / 67 | 411 € | **+35,34 €** | **+8,6 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 44 / 49 | 839 € | **+329,38 €** | **+39,3 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 87 gagnés, 190 perdus, 4 remboursés, 60 en attente · cote moyenne 3,35 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 4 / 4 | 85 € | +51,25 € | +60,3 % | 50 % |
| EV 0 à 5 % (exacte) | 1 / 1 | 10 € | -10,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 3 / 3 | 60 € | +10,00 € | +16,7 % | 33 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV 5 à 10 % (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV < 0 (approx) | 39 / 42 | 782 € | -366,70 € | -46,9 % | 20 % |
| EV < 0 (exacte) | 40 / 46 | 790 € | +134,50 € | +17,0 % | 36 % |
| non évaluable | 190 / 241 | 3950 € | -222,33 € | -5,6 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 11 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 3 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 3 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 9 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 51 / 93 | 1275 € | -1,25 € | -0,1 % | 38 % |
| Winamax | 210 / 222 | 4200 € | -447,00 € | -10,6 % | 28 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 42 | 0 € | +0,00 € | – | – |
| match | 281 / 299 | 5757 € | -328,28 € | -5,7 % | 31 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 7 / 9 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 1 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 13.88 € | 1 / 1 | 14 € | +24,98 € | +180,0 % | 100 % |
| 20 € | 217 / 233 | 4340 € | -421,00 € | -9,7 % | 28 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 51 / 93 | 1275 € | -1,25 € | -0,1 % | 38 % |
| 6.25 € | 1 / 1 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 5 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 118 / 141 | 2525 € | +54,48 € | +2,2 % | 41 % |
| 3 – 5 | 145 / 165 | 2892 € | -342,76 € | -11,9 % | 26 % |
| 5 – 10 | 13 / 20 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 10 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 8 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 43 | 265 € | -68,00 € | -25,7 % | 25 % |
| Football | 153 / 176 | 3092 € | -103,03 € | -3,3 % | 32 % |
| Football Américain | 6 / 6 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 30 / 32 | 600 € | -239,00 € | -39,8 % | 20 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 0 / 1 | 0 € | +0,00 € | – | – |
| Rugby | 6 / 6 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 4 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 9 | 180 € | +84,00 € | +46,7 % | 56 % |
| Tennis | 38 / 41 | 810 € | +501,25 € | +61,9 % | 53 % |
| Tennis de table | 5 / 5 | 100 € | -5,00 € | -5,0 % | 20 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 281 / 341 | 5757 € | -328,28 € | -5,7 % | 31 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 20/10 19h00 · Paris Trashtalk 26/27 | IND Pacers - Les Pacers remportent la Division Centrale | 4,25 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MEM Grizzlies - Cameron Boozer prend 8 rebonds ou + (moyenne) | 1,8 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | LA Clippers - Darius Garland fait 7 passes ou + (moyenne) | 1,6 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | HOU Rockets - Fred VanVleet fait 6 passes ou + (moyenne) | 2,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | DEN Nuggets - Les Nuggets se qualifient pour les Finales de Conférence | 5,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | BOS Celtics - Les Celtics se qualifient pour les Finales NBA | 7,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | POR TBlazers - Les Blazers ne se qualifient pas pour les Playoffs | 2,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | PHX Suns - Les Suns se qualifient pour les Playoffs | 1,66 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | GS Warriors - Les Warriors se qualifient pour les Playoffs | 1,58 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | DAL Mavericks - Les Mavericks se qualifient pour le PlayIn | 2,15 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | ATL Hawks - Dyson Daniels meilleur intercepteur NBA en saison régulière (moyenne interceptions/match, perdant si moins de 58 matchs joués) | 6,4 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | WAS Wizards - Trae Young meilleur passeur NBA en saison régulière (moyenne passes/match, perdant si moins de 58 matchs joués) | 3,3 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | TOR Raptors - Scottie Barnes meilleur passeur des Raptors (total de passes) | 2,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | DET Pistons - Cade Cunningham meilleur passeur NBA en saison régulière (moyenne passes/match, perdant si moins de 58 matchs joués) | 4,7 | – | – | 25 € | ⏳ |
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
| 20/10 19h00 · Paris Trashtalk 26/27 | PHI 76ers - Les 76ers finissent champions NBA | 9,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MIA Heat - Le Heat remporte la Division Sud-Est | 3,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CLE Cavaliers - Les Cavaliers remportent la Division Centrale | 3,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | SAC Kings - Maxime Raynaud meilleur rebondeur des Kings (total de rebonds) | 2,5 | – | – | 25 € | ⏳ |
| 19/10 18h30 · Monza - Cagliari | Monza gagne 1-0 | 8,0 | – | – | 20 € | ⏳ |
| 19/10 17h20 · Abha Club - Al-Kholood | Nabil Fekir Buteur | 4,05 | – | – | 20 € | ⏳ |
| 18/10 17h30 · Nottingham Forest - Arsenal | Arsenal mène à la mi-temps et gagne le match | 2,1 | 3,854 | -45,5 % ≈ | 20 € | ⏳ |
| 18/10 15h00 · Angers - Marseille | Amine Gouiri Buteur! | 2,55 | – | – | 20 € | ⏳ |
| 18/10 10h40 · R.Jodar - A.Davidovich | Les 2 joueurs gagnent un set ? | 2,3 | 2,501 | -8,0 % | 25 € | ⏳ |
| 18/10 10h00 · Alejandro Davidovich Fokina - Rafael Jodar | Exactement 3 sets lors du match | 2,3 | 2,501 | -8,0 % | 20 € | ⏳ |
| 18/10 07h00 · K-League 1 | Plus de 2,5 buts lors de chacun des matchs suivants : Daejon Citizen - Gwangju FC et Jeonbuk Motors - Jeju United | 2,9 | 3,283 | -11,7 % | 20 € | ⏳ |
| 18/10 04h30 · MLS | Nashville SC et Seattle Sounders marquent chacun au moins 2 buts (respectivement contre San Jose Earthquakes et Montreal) | 2,3 | 2,384 | -3,5 % | 20 € | ⏳ |
| 18/10 04h15 · NHL | Plus de 5,5 buts lors de chacun des matchs suivants : Utah Mammoth - Edmonton Oilers et Vegas Golden Knights - Pittsburgh Penguins | 2,3 | 2,509 | -8,3 % | 20 € | ⏳ |
| 18/10 03h45 · Joaquin Buckley - Mike Malott | J. Buckley gagne par KO, KO technique ou disqualification | 3,0 | – | – | 20 € | ⏳ |
| 18/10 02h30 · MLS | Les 2 équipes marquent dans chacun des 3 matchs à 2h30 | 3,75 | – | – | 20 € | ⏳ |
| 18/10 01h30 · MLS | Au moins un but marqué en première mi-temps lors de chacun des 5 matchs à 1h30 | 2,75 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
