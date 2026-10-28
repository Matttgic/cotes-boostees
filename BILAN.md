# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (537 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 537 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 388 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (603 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 603 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 347 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 28/10 23h51 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 785 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 785 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 541 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 711 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 628 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 437 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
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

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 492 en attente · cote moyenne 3,44 · pire série perdante 22

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
| non évaluable | 196 / 680 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 30 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 14 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 11 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 59 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 172 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 499 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 61 | 0 € | +0,00 € | – | – |
| match | 293 / 724 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 1.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 1.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 10 € | 7 / 31 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 2 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 12.5 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.88 € | 1 / 2 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.5 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.63 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.77 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 530 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 23.8 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 52 / 173 | 1300 € | +31,25 € | +2,4 % | 39 % |
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
| 8.06 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 8.33 € | 1 / 4 | 8 € | -8,33 € | -100,0 % | 0 % |
| 9.09 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 9.61 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 13 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 322 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 373 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 56 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 21 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 8 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 14 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 110 | 265 € | -68,00 € | -25,7 % | 25 % |
| Foot américain | 0 / 1 | 0 € | +0,00 € | – | – |
| Football | 159 / 406 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 16 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 5 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 5 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 58 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 3 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 12 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 6 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 14 | 180 € | +84,00 € | +46,7 % | 56 % |
| Ski Alpin | 0 / 1 | 0 € | +0,00 € | – | – |
| Tennis | 40 / 114 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 9 | 120 € | -25,00 € | -20,8 % | 17 % |
| UFC/MMA | 0 / 1 | 0 € | +0,00 € | – | – |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 785 | 6002 € | -235,78 € | -3,9 % | 32 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 29/10 19h00 · Al Nassr Club - Al-Kholood | Joao Felix Buteur | 2,05 | – | – | 20 € | ⏳ |
| 29/10 18h45 · Paris FC - Hacken Gothenburg | Paris FC gagne 1-0 | 9,5 | – | – | 20 € | ⏳ |
| 29/10 04h30 · Leylah Fernandez - Elise Mertens | Elise Mertens gagne 2-0 | 2,65 | – | – | 20 € | ⏳ |
| 29/10 04h00 · Club América - Club Tijuana | Club América gagne le match 1-0, 2-0 ou 3-0 | 3,35 | – | – | 20 € | ⏳ |
| 29/10 02h30 · Dallas Mavericks - Oklahoma City Thunder | Oklahoma City Thunder gagne et plus de 227,5 points dans le match | 2,7 | – | – | 20 € | ⏳ |
| 29/10 02h30 · Alycia Parks - Kimberly Birrell | Exactement 3 sets lors du match | 2,5 | – | – | 20 € | ⏳ |
| 29/10 02h10 · Colorado Avalanche - New Jersey Devils | M. Necas + J. Hughes + N. MacKinnon marquent 2 buts ou plus (hors prol. et TAB) | 2,6 | – | – | 20 € | ⏳ |
| 29/10 01h40 · Edmonton Oilers - Calgary Flames | L. Draisaitl buteur et Edmonton Oilers gagne (hors prol. et TAB) | 2,75 | – | – | 20 € | ⏳ |
| 29/10 01h30 · Bahia - Sao Paulo | Bahia gagne la première mi-temps | 2,4 | – | – | 20 € | ⏳ |
| 29/10 01h10 · Tampa Bay Rays - Milwaukee Brewers | Les deux équipes marquent chacune au moins 3 runs | 2,75 | – | – | 20 € | ⏳ |
| 29/10 00h30 · Inter Miami - Cincinnati FC | Lionel Messi marque 2 buts ou plus | 3,1 | – | – | 20 € | ⏳ |
| 29/10 00h10 · NBA | Tyrese Maxey et Donovan Mitchell marquent au moins 25 points chacun (respectivement contre Indiana Pacers et Washington Wizards) | 3,25 | – | – | 20 € | ⏳ |
| 29/10 00h10 · Atlanta Hawks - Miami Heat | G. Antetokounmpo réalise une performance points + rebonds + passes décisives d'au moins 55 | 3,25 | – | – | 20 € | ⏳ |
| 29/10 00h00 · IND Pacers - PHI 76ers | NBA - Jaylen Brown : 20 points ou +, 5 rebonds ou +, 3 passes ou + | 2,75 | – | – | 25 € | ⏳ |
| 28/10 21h00 · Liverpool - Chelsea | Liverpool ou Chelsea gagne et au moins 4 buts marqués dans le match ? | 2,75 | – | – | 25 € | ⏳ |
| 28/10 21h00 · OL Lyonnes (F) - Inter (F) | OL Lyonnes (F) marque au moins 5 buts | 3,0 | – | – | 20 € | ⏳ |
| 28/10 21h00 · Liverpool - Chelsea | Liverpool gagne la première mi-temps | 2,5 | – | – | 20 € | ⏳ |
| 28/10 21h00 · Liverpool - Chelsea | Plus de 4.5 buts dans le match | 3,5 | – | – | 10 € | ⏳ |
| 28/10 21h00 · Liverpool / Chelsea : Plus de 2,5 buts (mise max 10 €) | Liverpool / Chelsea : Plus de 2,5 buts (mise max 10 €) | 1,6 | – | – | 10 € | ⏳ |
| 28/10 20h45 · Paris SG - Aalborg | Elohim Prandi marque 6 buts ou plus et son équipe gagne | 3,5 | – | – | 20 € | ⏳ |
| 28/10 20h45 · Bayern Munich - Magdebourg | Plus de 2,5 buts lors de la première mi-temps du match | 2,5 | – | – | 20 € | ⏳ |
| 28/10 20h45 · Serie A | Plus de 2,5 buts lors de chacun des matchs suivants : Genoa - Juventus et Monza - Naples | 3,75 | – | – | 20 € | ⏳ |
| 28/10 20h30 · Manchester City - Brighton | Manchester City gagne le match 2-1, 3-1 ou 4-1 (hors TAB) | 4,5 | – | – | 20 € | ⏳ |
| 28/10 20h15 · Tennis de Table | Alexis Lebrun et Jia Nan Yuan gagnent chacun leur match (respectivement contre Patrick Franziska et Sabine Winter) | 4,5 | – | – | 20 € | ⏳ |
| 28/10 20h00 · ASVEL - Partizan Belgrade | ASVEL gagne et plus de 168,5 points dans le match | 3,25 | – | – | 20 € | ⏳ |
| 28/10 19h30 · H. Hurkacz - H. Rune | Hurkacz gagne et plus de 2.5 sets | 3,6 | – | – | 9.61 € | ⏳ |
| 28/10 19h05 · Tomokazu Harimoto - Simon Gauzy | Simon Gauzy gagne le premier set | 4,0 | – | – | 20 € | ⏳ |
| 28/10 18h30 · CB - Serie A (28/10) | Plus de 1,5 buts dans chacun des 5 matchs du jour | 3,4 | – | – | 25 € | ⏳ |
| 28/10 18h30 · Besiktas - Olympiakos | Sasha Vezenkov marque au moins 20 points et Olympiakos gagne | 2,75 | – | – | 20 € | ⏳ |
| 28/10 18h30 · Milan AC - Bologne | Milan AC gagne et les deux équipes marquent | 4,1 | – | – | 20 € | ⏳ |
| 28/10 18h30 · Milan AC - Bologne | Milan AC gagne et les deux équipes marquent | 4,25 | – | – | 20 € | ⏳ |
| 28/10 18h30 · Venise - Inter Milan | Inter Milan gagne et plus de 3,5 buts dans le match | 2,3 | – | – | 20 € | ⏳ |
| 28/10 18h30 · ALL TO WIN | AC Milan, Inter Milan & Naples (Serie A / 28.10.2026) | 4,1 | – | – | 8.06 € | ⏳ |
| 28/10 18h30 · Besiktas JK - Olympiakos | Aleksandar Vezenkov marque 25 points ou + | 3,1 | – | – | 20 € | ⏳ |
| 28/10 18h00 · Coupe d'Allemagne | Stuttgart et Fribourg marquent chacun au moins 2 buts (respectivement contre Paderborn et Wolfsbourg) (hors prol. et TAB) | 2,1 | – | – | 20 € | ⏳ |
| 28/10 18h00 · Coupe d'Allemagne | Au moins un but marqué en première mi-temps lors de chacun des 8 matchs du jour | 4,0 | – | – | 20 € | ⏳ |
| 28/10 18h00 · ATP Bale | Taylor Fritz et Hubert Hurkacz gagnent chacun leur match 2-0 (respectivement contre Rinky Hijikata et Holger Rune) | 3,25 | – | – | 20 € | ⏳ |
| 28/10 16h15 · N.Djokovic - U.Humbert | Les 2 joueurs gagnent un set ? | 2,5 | – | – | 25 € | ⏳ |
| 28/10 16h05 · Flavien Coton - Woojin Jang | Flavien Coton gagne le match | 3,25 | – | – | 20 € | ⏳ |
| 28/10 15h50 · Jakub Mensik - Adrian Mannarino | Adrian Mannarino gagne le premier set | 3,6 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
