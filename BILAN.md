# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (366 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 366 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 267 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (382 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 382 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 225 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 23/10 20h28 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 564 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 564 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 400 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 497 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 446 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 315 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
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

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 271 en attente · cote moyenne 3,35 · pire série perdante 22

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
| non évaluable | 196 / 459 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 23 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 8 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 8 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 25 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 139 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 361 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 55 | 0 € | +0,00 € | – | – |
| match | 293 / 509 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 1.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 10 € | 7 / 21 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 1 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 13.88 € | 1 / 2 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 384 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 23.8 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 52 / 139 | 1300 € | +31,25 € | +2,4 % | 39 % |
| 3.12 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 3.84 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 5.55 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5.74 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 6.25 € | 1 / 2 | 6 € | +21,88 € | +350,1 % | 100 % |
| 7.69 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |
| 9.09 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 8 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 242 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 262 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 36 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 16 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 6 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 10 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 76 | 265 € | -68,00 € | -25,7 % | 25 % |
| Football | 159 / 294 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 13 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 47 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 9 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 4 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 11 | 180 € | +84,00 € | +46,7 % | 56 % |
| Tennis | 40 / 79 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 6 | 120 € | -25,00 € | -20,8 % | 17 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 564 | 6002 € | -235,78 € | -3,9 % | 32 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 26/10 20h30 · Paris SG - Lyon | Maghnes Akliouche Buteur! | 2,85 | – | – | 20 € | ⏳ |
| 25/10 17h15 · Marseille - Le Havre | Amine Harit PASSEUR DECISIF | 3,75 | – | – | 20 € | ⏳ |
| 25/10 15h00 · Monaco - Lille | Monaco gagne 2-0 | 10,0 | – | – | 20 € | ⏳ |
| 24/10 18h30 · Chelsea - Tottenham | Cold Palmer Buteur! | 2,6 | – | – | 20 € | ⏳ |
| 24/10 13h30 · Aston Villa - Manchester City | Rayan Cherki Buteur | 3,25 | – | – | 20 € | ⏳ |
| 24/10 03h40 · NBA | V. Wembanyama et L. Doncic marquent au moins 30 points chacun (respectivement contre Houston Rockets et Los Angeles Clippers) | 4,0 | – | – | 20 € | ⏳ |
| 24/10 03h30 · SA Spurs - HOU Rockets | Victor Wembanyama : 20 points ou +, 10 rebonds ou +, 3 passes ou + | 2,85 | – | – | 25 € | ⏳ |
| 24/10 02h10 · Miami Heat - Detroit Pistons | Miami Heat gagne et plus de 225,5 points dans le match | 2,6 | – | – | 20 € | ⏳ |
| 24/10 02h00 · Milwaukee Brewers - Tampa Bay Rays | Jackson Chourio marque au moins 1 run et Milwaukee Brewers gagne le match | 2,8 | – | – | 20 € | ⏳ |
| 24/10 01h10 · Boston Celtics - New York Knicks | Jayson Tatum marque au moins 25 points et Boston Celtics gagne | 2,75 | – | – | 20 € | ⏳ |
| 24/10 01h00 · BOS Celtics - NY Knicks | NBA - Jayson Tatum & Jalen Brunson marquent 25 Points ou + chacun | 3,0 | – | – | 25 € | ⏳ |
| 23/10 22h00 · Milwaukee Bucks - Chicago Bulls | Tyler Herro marque au moins 20 points et Milwaukee Bucks gagne | 2,5 | – | – | 20 € | ⏳ |
| 23/10 21h00 · Alaves - Malaga | Alaves gagne et plus de 2,5 buts dans le match | 2,8 | – | – | 20 € | ⏳ |
| 23/10 21h00 · Ipswich Town - Nottingham Forest | Nottingham Forest gagne le match 0-1, 0-2 ou 0-3 | 4,75 | – | – | 20 € | ⏳ |
| 23/10 20h45 · Brest - Nice | Brest ou Nice gagne et les deux équipes marquent | 2,4 | – | – | 25 € | ⏳ |
| 23/10 20h45 · Brest - Nice | L. Ajorque ou E. Wahi marque au moins un but en 1ère mi-temps | 3,5 | – | – | 20 € | ⏳ |
| 23/10 20h45 · Paris Basketball - Valence Basket | Paris Basketball gagne à la mi-temps et à la fin du match | 4,0 | – | – | 20 € | ⏳ |
| 23/10 20h45 · Brest - OGC Nice | OGC Nice gagne et Elye Wahi marque au moins 1+ buts | 6,0 | – | – | 5 € | ⏳ |
| 23/10 20h45 · Brest - OGC Nice | Brest gagne et les deux équipes marquent | 3,75 | – | – | 9.09 € | ⏳ |
| 23/10 20h45 · Brest / Nice : Plus de 2,5 buts (mise max 10 €) | Brest / Nice : Plus de 2,5 buts (mise max 10 €) | 1,8 | – | – | 10 € | ⏳ |
| 23/10 20h30 · Rouen - Angers | T. Simonsen buteur et Rouen gagne (hors prol. et TAB) | 3,5 | – | – | 20 € | ⏳ |
| 23/10 20h30 · Stuttgart - Borussia M'Gladbach | Stuttgart gagne sans encaisser de but | 3,0 | – | – | 20 € | ⏳ |
| 23/10 20h30 · Luca van Assche - Lorenzo Musetti | Luca van Assche remporte le match sur le score exact de 2-1 en sets | 6,0 | – | – | 5 € | ⏳ |
| 23/10 20h15 · Olympiakos - Fenerbahce | Plus de 179,5 points lors du match | 3,75 | – | – | 20 € | ⏳ |
| 23/10 20h00 · Ligue 2 - 22/10 | Plus de 1,5 buts dans chacun des 5 matchs de 20:00 | 3,45 | – | – | 25 € | ⏳ |
| 23/10 20h00 · Ligue 2 BKT® | Plus de 1,5 buts dans chacun des 5 matchs du jour | 3,25 | – | – | 20 € | ⏳ |
| 23/10 20h00 · TOUS VAINQUEURS | Metz, En Avant Guingamp, Nancy et Pau FC (Ligue 2 - 23.10.2026) | 16,0 | – | – | 1.66 € | ⏳ |
| 23/10 19h30 · Pro D2 | Chaque équipe à domicile gagne (6 matchs à partir de 19h30) | 2,5 | – | – | 20 € | ⏳ |
| 23/10 19h00 · Narbonne - CA Brive | CA Brive gagne par au moins 14 points d'écart | 2,85 | – | – | 20 € | ⏳ |
| 23/10 19h00 · Cobolli, Flavio - Nakashima, Brandon | Nakashima gagne 2-0 | 2,35 | – | – | 20 € | ⏳ |
| 23/10 18h30 · A.Fils - A.Michelsen | A.Fils gagne le 1er set 6-4 ou 7-5 ou 7-6 ? | 2,7 | – | – | 25 € | ⏳ |
| 23/10 18h30 · Arthur Fils - Alex Michelsen | Arthur Fils gagne et plus de 22,5 jeux dans le match | 3,0 | – | – | 20 € | ⏳ |
| 23/10 18h30 · Arthur Fils - Alex Michelsen | Chaque joueur au moins 10+ aces et plus de 2.5 sets dans le match | 5,5 | – | – | 5.55 € | ⏳ |
| 23/10 17h30 · Liiga | Plus de 4,5 buts dans chacun des 4 matchs à 17h30 | 4,0 | – | – | 20 € | ⏳ |
| 23/10 17h30 · Saudi Pro League | Al-Ittihad FC et Al-Hilal marquent chacun le 1er but (respectivement contre Diriyah Club et Al-Qadsiah) | 3,0 | – | – | 20 € | ⏳ |
| 23/10 15h30 · Al-Faisaly - Al Nassr | Cristiano Ronaldo premier buteur du match | 3,75 | – | – | 20 € | ⏳ |
| 23/10 14h00 · Corentin Moutet - Tommy Paul | Corentin Moutet gagne le premier set | 3,0 | – | – | 20 € | ⏳ |
| 23/10 14h00 · Corentin Moutet - Tommy Paul | Corentin Moutet remporte le match sur le score exact de 2-0 en sets | 7,5 | – | – | 3.84 € | ⏳ |
| 23/10 14h00 · Clement Chidekh - Francisco Cerundolo | Clement Chidekh gagne et plus de 22.5 jeux | 4,25 | – | – | 7.69 € | ⏳ |
| 23/10 13h00 · Elena Rybakina - Katarzyna Kawa | Elena Rybakina gagne et plus de 17.5 jeux | 2,05 | – | – | 23.8 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
