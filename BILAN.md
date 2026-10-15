# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (107 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 75 / 107 | 1555 € | **-78,75 €** | **-5,1 %** | -15,6 % (34 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 52 / 75 | 520 € | **+3,50 €** | **+0,7 %** | -16,5 % (24 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (69 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 41 / 69 | 841 € | +190,25 € | +22,6 % |
| **I — cotes modérées, un boost/match** | 27 / 38 | 270 € | +77,50 € | +28,7 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 15/10 14h00 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 188 / 251 | 3865 € | **-124,20 €** | **-3,2 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 5 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 188 / 251 | 1875 € | **-48,45 €** | **-2,6 %** | -337,50 € |
| **D — cote 1,60–3,50** | 130 / 173 | 1300 € | **+38,00 €** | **+2,9 %** | -238,00 € |
| **E — dans les 48 h** | 188 / 213 | 1875 € | **-48,45 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 171 / 188 | 1705 € | **-78,45 €** | **-4,6 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 116 / 128 | 1160 € | **-22,00 €** | **-1,9 %** | -221,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 36 / 39 | 347 € | **-40,17 €** | **-11,6 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 46 / 50 | 445 € | **+68,23 €** | **+15,3 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 49 / 53 | 298 € | **+31,10 €** | **+10,4 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 31 / 35 | 585 € | **+242,77 €** | **+41,5 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 60 gagnés, 124 perdus, 4 remboursés, 63 en attente · cote moyenne 3,36 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 4 / 4 | 85 € | +51,25 € | +60,3 % | 50 % |
| EV 10 % et + (approx) | 3 / 3 | 60 € | +10,00 € | +16,7 % | 33 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 25 / 30 | 500 € | -282,00 € | -56,4 % | 16 % |
| EV < 0 (exacte) | 24 / 26 | 490 € | +244,50 € | +49,9 % | 48 % |
| non évaluable | 129 / 185 | 2670 € | -242,95 € | -9,1 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 2 / 4 | 40 € | +13,00 € | +32,5 % | 50 % |
| NetBet | 1 / 2 | 10 € | +17,50 € | +175,0 % | 100 % |
| OlyBet | 3 / 4 | 35 € | +38,55 € | +108,9 % | 67 % |
| Unibet | 28 / 72 | 700 € | +13,75 € | +2,0 % | 41 % |
| Winamax | 154 / 169 | 3080 € | -207,00 € | -6,7 % | 30 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 38 | 0 € | +0,00 € | – | – |
| match | 188 / 213 | 3865 € | -124,20 € | -3,2 % | 33 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 1 / 3 | 10 € | +17,50 € | +175,0 % | 100 % |
| 20 € | 156 / 173 | 3120 € | -194,00 € | -6,2 % | 30 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 28 / 72 | 700 € | +13,75 € | +2,0 % | 41 % |
| 6.25 € | 1 / 1 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 1 / 4 | 20 € | -20,00 € | -100,0 % | 0 % |
| 2 – 3 | 75 / 103 | 1606 € | +144,00 € | +9,0 % | 44 % |
| 3 – 5 | 102 / 121 | 2040 € | -248,20 € | -12,2 % | 26 % |
| 5 – 10 | 10 / 15 | 200 € | +0,00 € | +0,0 % | 20 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 5 / 5 | 100 € | -52,00 € | -52,0 % | 20 % |
| Basketball | 9 / 38 | 180 € | -118,00 € | -65,6 % | 12 % |
| Football | 103 / 129 | 2115 € | -14,20 € | -0,7 % | 33 % |
| Football Américain | 5 / 5 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 19 / 20 | 380 € | -133,00 € | -35,0 % | 21 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XIII | 0 / 2 | 0 € | +0,00 € | – | – |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 27 / 31 | 570 € | +362,50 € | +63,6 % | 56 % |
| Tennis de table | 2 / 3 | 40 € | +55,00 € | +137,5 % | 50 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 188 / 251 | 3865 € | -124,20 € | -3,2 % | 33 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 20/10 19h00 · Paris Trashtalk 26/27 | PHI 76ers - Les 76ers finissent champions NBA | 9,5 | – | – | 25 € | ⏳ |
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
| 15/10 21h00 · Rennes - OFI Crète | Rennes gagne sur le score exact de 1:0, 2:0 ou 3:0 | 3,0 | – | – | 25 € | ⏳ |
| 15/10 21h00 · Marseille - Olympiakos | Marseille gagne et plus 1,5 Buts | 2,6 | 3,158 | -17,7 % ≈ | 25 € | ⏳ |
| 15/10 21h00 · Rennes - OFI Crète | Esteban Lepaul marque au moins un but en 1ère mi-temps | 3,0 | – | – | 20 € | ⏳ |
| 15/10 21h00 · Celta Vigo - Juventus | Juventus gagne par exactement 1 but d'écart | 4,0 | – | – | 20 € | ⏳ |
| 15/10 21h00 · Marseille - Olympiakos | Marseille gagne à la mi-temps et à la fin du match | 4,0 | 7,642 | -47,7 % ≈ | 20 € | ⏳ |
| 15/10 21h00 · Atalanta - Pafos FC | Atalanta gagne par au moins 3 buts d'écart | 3,35 | 3,652 | -8,3 % | 20 € | ⏳ |
| 15/10 18h45 · Lyon - Crystal Palace  | Lyon marque dans les 2 Mi-temps | 2,85 | – | – | 25 € | ⏳ |
| 15/10 18h45 · CSKA Sofia - Monaco | Monaco mène à la Mi-temps et gagne le Match | 2,25 | 3,172 | -29,1 % ≈ | 25 € | ⏳ |
| 15/10 18h45 · CB - Combi EL /ECL (15/10) | Lyon, Rennes, Marseille et Monaco ne perdent pas leurs matchs respectifs | 2,5 | – | – | 25 € | ⏳ |
| 15/10 18h45 · Lyon - Crystal Palace | Lyon gagne ou fait match nul et plus de 2,5 buts dans le match | 2,4 | 4,02 | -40,3 % ≈ | 20 € | ⏳ |
| 15/10 18h45 · Red Bull Salzbourg - Milan AC | Milan AC gagne sans encaisser de but | 4,15 | – | – | 20 € | ⏳ |
| 15/10 18h45 · CSKA Sofia - Monaco | Monaco marque dans les deux mi-temps | 2,3 | – | – | 20 € | ⏳ |
| 15/10 18h45 · Ligue Conférence | Plus de 0,5 but lors de la première mi-temps de chacun des matchs suivants : FC Lugano - Etoile Rouge de Belgrade, Hajduk Split - Ajax Amsterdam et La Gantoise - Aarhus | 2,3 | – | – | 20 € | ⏳ |
| 15/10 18h45 · Lyon - Crystal Palace | Lyon (vs Crystal Palace), Marseille (vs Olympiakos) et Rennes (vs OFI Crete) marquent tous le premier but de leur match | 4,0 | – | – | 10 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
