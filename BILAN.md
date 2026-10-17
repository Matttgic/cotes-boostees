# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (172 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 138 / 172 | 2900 € | **-362,50 €** | **-12,5 %** | -17,0 % (55 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 99 / 121 | 990 € | **-141,00 €** | **-14,2 %** | -16,6 % (37 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (150 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 111 / 150 | 2271 € | +5,53 € | +0,2 % |
| **I — cotes modérées, un boost/match** | 70 / 89 | 700 € | -7,50 € | -1,1 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 17/10 19h13 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 260 / 332 | 5336 € | **-305,92 €** | **-5,7 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 5 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 260 / 332 | 2595 € | **-116,95 €** | **-4,5 %** | -337,50 € |
| **D — cote 1,60–3,50** | 184 / 232 | 1840 € | **-22,00 €** | **-1,2 %** | -238,00 € |
| **E — dans les 48 h** | 260 / 284 | 2595 € | **-116,95 €** | **-4,5 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 230 / 258 | 2295 € | **-152,95 €** | **-6,7 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 159 / 179 | 1590 € | **-108,00 €** | **-6,8 %** | -244,00 € |
| **B — valeur ≥ +5 %** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B0 — valeur ≥ 0 %** | 3 / 3 | 50 € | **-50,00 €** | **-100,0 %** | -50,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 44 / 45 | 424 € | **+19,39 €** | **+4,6 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 59 / 63 | 575 € | **+120,73 €** | **+21,0 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 62 / 65 | 407 € | **+39,06 €** | **+9,6 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 43 / 47 | 819 € | **+349,38 €** | **+42,7 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 81 gagnés, 175 perdus, 4 remboursés, 72 en attente · cote moyenne 3,36 · pire série perdante 22

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
| EV < 0 (approx) | 38 / 41 | 762 € | -346,70 € | -45,5 % | 21 % |
| EV < 0 (exacte) | 36 / 41 | 720 € | +184,50 € | +25,6 % | 37 % |
| non évaluable | 174 / 238 | 3619 € | -269,97 € | -7,5 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 5 / 11 | 100 € | +66,00 € | +66,0 % | 60 % |
| Genybet | 2 / 3 | 20 € | -20,00 € | -100,0 % | 0 % |
| NetBet | 2 / 3 | 20 € | +7,50 € | +37,5 % | 50 % |
| OlyBet | 6 / 9 | 71 € | +117,58 € | +165,8 % | 83 % |
| Unibet | 45 / 92 | 1125 € | -75,00 € | -6,7 % | 36 % |
| Winamax | 200 / 214 | 4000 € | -402,00 € | -10,1 % | 28 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 42 | 0 € | +0,00 € | – | – |
| match | 260 / 290 | 5336 € | -305,92 € | -5,7 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 5 / 9 | 50 € | +12,50 € | +25,0 % | 40 % |
| 11.11 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 13.88 € | 1 / 1 | 14 € | +24,98 € | +180,0 % | 100 % |
| 20 € | 205 / 225 | 4100 € | -336,00 € | -8,2 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 45 / 92 | 1125 € | -75,00 € | -6,7 % | 36 % |
| 6.25 € | 1 / 1 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 2 / 5 | 40 € | -40,00 € | -100,0 % | 0 % |
| 2 – 3 | 106 / 135 | 2280 € | +143,23 € | +6,3 % | 43 % |
| 3 – 5 | 139 / 162 | 2776 € | -469,15 € | -16,9 % | 25 % |
| 5 – 10 | 11 / 20 | 220 € | +80,00 € | +36,4 % | 27 % |
| < 2 | 2 / 10 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 8 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 11 / 43 | 220 € | -158,00 € | -71,8 % | 10 % |
| Football | 140 / 171 | 2846 € | -120,67 € | -4,2 % | 32 % |
| Football Américain | 6 / 6 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 28 / 30 | 560 € | -199,00 € | -35,5 % | 21 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 0 / 1 | 0 € | +0,00 € | – | – |
| Rugby | 4 / 6 | 100 € | -37,50 € | -37,5 % | 25 % |
| Rugby à XIII | 4 / 4 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 8 / 9 | 160 € | +104,00 € | +65,0 % | 62 % |
| Tennis | 38 / 39 | 810 € | +501,25 € | +61,9 % | 53 % |
| Tennis de table | 4 / 5 | 80 € | +15,00 € | +18,8 % | 25 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 260 / 332 | 5336 € | -305,92 € | -5,7 % | 32 % |

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
| 18/10 03h45 · Joaquin Buckley - Mike Malott | J. Buckley gagne par KO, KO technique ou disqualification | 3,0 | – | – | 20 € | ⏳ |
| 17/10 21h45 · NHL | Plus de 5,5 buts lors de chacun des matchs suivants : Winnipeg Jets - Carolina Hurricanes et Tampa Bay Lightning - Vancouver Canucks (prol. et TAB inclus) | 2,6 | 2,82 | -7,8 % | 20 € | ⏳ |
| 17/10 21h30 · GS Valkyries - ATL Dream | WNBA FINALS - Gabby Williams et Allisha Gray marquent 40pts ou + en cumulé | 2,8 | – | – | 25 € | ⏳ |
| 17/10 21h30 · Golden State Valkyries - Atlanta Dream | Gabby Williams marque au moins 20 points et Golden State Valkyries gagne | 3,25 | – | – | 20 € | ⏳ |
| 17/10 21h00 · Bath - Montpellier | Lenni Nouchi ou Justo Piccardo marque au moins 1 essai | 2,3 | – | – | 25 € | ⏳ |
| 17/10 20h45 · Ligue 1 (17/10) | Lille et Lens marquent chacun le 1er but et gagnent leur match respectif | 4,2 | – | – | 25 € | ⏳ |
| 17/10 20h45 · Football | Plus de 2,5 buts lors de chacun des matchs suivants : AS Rome - Genoa et Valence - Athletic Bilbao | 3,75 | 4,378 | -14,3 % | 20 € | ⏳ |
| 17/10 20h45 · Ligue 1 McDonald's® | Lille et Lens marquent chacun au moins 2 buts | 3,0 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
