# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (50 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 41 / 50 | 845 € | **-276,50 €** | **-32,7 %** | -18,5 % (17 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 28 / 32 | 280 € | **-92,00 €** | **-32,9 %** | -22,6 % (11 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (9 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 5 / 9 | 100 € | -50,00 € | -50,0 % |
| **I — cotes modérées, un boost/match** | 5 / 6 | 50 € | -25,00 € | -50,0 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 14/10 07h02 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 148 / 191 | 3070 € | **-391,00 €** | **-12,7 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 4 / 4 | 80 € | **+145,00 €** | **+181,2 %** | -20,00 € |
| **C — 10 € maximum** | 148 / 191 | 1480 € | **-189,50 €** | **-12,8 %** | -337,50 € |
| **D — cote 1,60–3,50** | 103 / 128 | 1030 € | **-103,50 €** | **-10,0 %** | -238,00 € |
| **E — dans les 48 h** | 148 / 159 | 1480 € | **-189,50 €** | **-12,8 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 139 / 150 | 1390 € | **-156,00 €** | **-11,2 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 96 / 100 | 960 € | **-90,00 €** | **-9,4 %** | -221,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 29 / 33 | 281 € | **-68,10 €** | **-24,2 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 38 / 43 | 365 € | **+21,73 €** | **+6,0 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 41 / 46 | 237 € | **+5,07 €** | **+2,1 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 24 / 29 | 457 € | **+177,52 €** | **+38,8 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 43 gagnés, 105 perdus, 0 remboursés, 43 en attente · cote moyenne 3,41 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 2 / 2 | 40 € | +30,00 € | +75,0 % | 50 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 22 / 22 | 440 € | -222,00 € | -50,5 % | 18 % |
| EV < 0 (exacte) | 18 / 20 | 365 € | +201,50 € | +55,2 % | 50 % |
| non évaluable | 101 / 142 | 2125 € | -455,50 € | -21,4 % | 27 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 0 / 4 | 0 € | +0,00 € | – | – |
| OlyBet | 0 / 3 | 0 € | +0,00 € | – | – |
| Unibet | 22 / 53 | 550 € | -60,00 € | -10,9 % | 36 % |
| Winamax | 126 / 131 | 2520 € | -331,00 € | -13,1 % | 28 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 32 | 0 € | +0,00 € | – | – |
| match | 148 / 159 | 3070 € | -391,00 € | -12,7 % | 29 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 20 € | 126 / 135 | 2520 € | -331,00 € | -13,1 % | 28 % |
| 25 € | 22 / 53 | 550 € | -60,00 € | -10,9 % | 36 % |
| 7.14 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 8.33 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 4 | 0 € | +0,00 € | – | – |
| 2 – 3 | 57 / 71 | 1230 € | +9,00 € | +0,7 % | 40 % |
| 3 – 5 | 84 / 95 | 1700 € | -360,00 € | -21,2 % | 23 % |
| 5 – 10 | 7 / 13 | 140 € | -40,00 € | -28,6 % | 14 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| Baseball | 4 / 4 | 80 € | -32,00 € | -40,0 % | 25 % |
| Basketball | 8 / 33 | 160 € | -118,00 € | -73,8 % | 12 % |
| Football | 80 / 93 | 1665 € | -288,00 € | -17,3 % | 26 % |
| Football Américain | 5 / 5 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 14 / 14 | 280 € | -105,00 € | -37,5 % | 21 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 20 / 24 | 425 € | +307,50 € | +72,4 % | 60 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 148 / 191 | 3070 € | -391,00 € | -12,7 % | 29 % |

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
| 20/10 19h00 · Paris Trashtalk 26/27 | MIA Heat - Le Heat remporte la Division Sud-Est | 3,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CLE Cavaliers - Les Cavaliers remportent la Division Centrale | 3,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | SAC Kings - Maxime Raynaud meilleur rebondeur des Kings (total de rebonds) | 2,5 | – | – | 25 € | ⏳ |
| 15/10 18h45 · CSKA Sofia - Monaco | Monaco gagne 3-0 | 10,5 | – | – | 20 € | ⏳ |
| 15/10 18h45 · Lyon - Crystal Palace | Pavel Sulc Décisif | 2,15 | – | – | 20 € | ⏳ |
| 14/10 21h00 · Manchester City - Paris SG | Le PSG gagne 1-0 | 15,0 | – | – | 20 € | ⏳ |
| 14/10 20h45 · Manchester City - Paris SG | Paris SG gagne et les 2 équipes marquent | 4,5 | – | – | 7.14 € | ⏳ |
| 14/10 20h45 · AS Rome - Real Madrid | Real Madrid to win and Vinicius to score | 4,0 | – | – | 8.33 € | ⏳ |
| 14/10 18h45 · LASK Linz - Liverpool | Barcola Buteur | 2,65 | – | – | 20 € | ⏳ |
| 14/10 10h10 · Badminton | Tomas Junior Popov et Christo Popov gagnent chacun leur match 2-0 (respectivement contre Yudai Okimoto et Hongyang Weng) | 5,25 | – | – | 20 € | ⏳ |
| 14/10 07h15 · C. Ruud - F. Auger-Aliassime | Auger-Aliassime gagne et plus de 20,5 aces dans le match | 3,5 | – | – | 10 € | ⏳ |
| 14/10 07h10 · Casper Ruud - Felix Auger-Aliassime | Casper Ruud gagne et plus de 19,5 jeux dans le match contre Felix Auger-Aliassime | 2,65 | – | – | 20 € | ⏳ |
| 14/10 06h00 · ATP Shanghai | Plus de 2,5 sets dans chacun des matchs suivants : Botic van de Zandschulp - Rafael Jodar et Casper Ruud - Felix Auger-Aliassime | 5,0 | 6,508 | -23,2 % | 20 € | ⏳ |
| 14/10 05h00 · WTA Wuhan | Iga Swiatek, Iva Jovic et Karolina Muchova gagnent chacune leur match 2-0 (respectivement contre Magdalena Frech, Dayana Yastremska et Caty McNally) | 3,75 | 4,462 | -16,0 % | 20 € | ⏳ |
| 14/10 02h45 · NHL | Plus de 5,5 buts lors de chacun des matchs suivants : Nashville Predators - Vegas Golden Knights et Utah Mammoth - Toronto Maple Leafs | 2,5 | 2,776 | -9,9 % | 20 € | ✅ +30,00 € |
| 14/10 02h30 · Boca Juniors - Vasco da Gama | Boca Juniors gagne le match 1-0, 2-0 ou 3-0 | 2,8 | – | – | 20 € | ❌ -20,00 € |
| 14/10 02h00 · Tampa Bay Rays - Cleveland Guardians | Tampa Bay Rays réalise au moins 5 runs | 2,8 | 2,995 | -6,5 % | 20 € | ❌ -20,00 € |
| 14/10 01h30 · Bucaramanga - Aguilas Doradas | Bucaramanga gagne à la mi-temps et à la fin du match | 3,25 | 4,879 | -41,6 % ≈ | 20 € | ❌ -20,00 € |
| 14/10 00h40 · Montreal Canadiens - Buffalo Sabres | Cole Caufield buteur et Montreal Canadiens gagne (hors prol. et TAB) | 3,25 | – | – | 20 € | ❌ -20,00 € |

≈ : calcul approché (conditions liées sur un même match).
