# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (87 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 73 / 87 | 1515 € | **-106,75 €** | **-7,0 %** | -13,5 % (28 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 51 / 61 | 510 € | **-10,50 €** | **-2,1 %** | -15,0 % (20 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (48 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 39 / 48 | 801 € | +162,25 € | +20,3 % |
| **I — cotes modérées, un boost/match** | 26 / 30 | 260 € | +63,50 € | +24,4 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 15/10 07h50 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 186 / 230 | 3825 € | **-152,20 €** | **-4,0 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 5 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 186 / 230 | 1855 € | **-62,45 €** | **-3,4 %** | -337,50 € |
| **D — cote 1,60–3,50** | 129 / 159 | 1290 € | **+24,00 €** | **+1,9 %** | -238,00 € |
| **E — dans les 48 h** | 186 / 194 | 1855 € | **-62,45 €** | **-3,4 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 169 / 177 | 1685 € | **-92,45 €** | **-5,5 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 115 / 121 | 1150 € | **-36,00 €** | **-3,1 %** | -221,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 35 / 38 | 337 € | **-40,17 €** | **-11,9 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 45 / 48 | 435 € | **+68,23 €** | **+15,7 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 48 / 51 | 293 € | **+31,10 €** | **+10,6 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 30 / 33 | 565 € | **+242,77 €** | **+43,0 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 59 gagnés, 124 perdus, 3 remboursés, 44 en attente · cote moyenne 3,36 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 4 / 4 | 85 € | +51,25 € | +60,3 % | 50 % |
| EV 10 % et + (approx) | 3 / 3 | 60 € | +10,00 € | +16,7 % | 33 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 25 / 26 | 500 € | -282,00 € | -56,4 % | 16 % |
| EV < 0 (exacte) | 22 / 24 | 450 € | +216,50 € | +48,1 % | 46 % |
| non évaluable | 129 / 170 | 2670 € | -242,95 € | -9,1 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 2 / 4 | 40 € | +13,00 € | +32,5 % | 50 % |
| NetBet | 1 / 1 | 10 € | +17,50 € | +175,0 % | 100 % |
| OlyBet | 3 / 4 | 35 € | +38,55 € | +108,9 % | 67 % |
| Unibet | 28 / 65 | 700 € | +13,75 € | +2,0 % | 41 % |
| Winamax | 152 / 156 | 3040 € | -235,00 € | -7,7 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 36 | 0 € | +0,00 € | – | – |
| match | 186 / 194 | 3825 € | -152,20 € | -4,0 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 1 / 2 | 10 € | +17,50 € | +175,0 % | 100 % |
| 20 € | 154 / 160 | 3080 € | -222,00 € | -7,2 % | 30 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 28 / 65 | 700 € | +13,75 € | +2,0 % | 41 % |
| 6.25 € | 1 / 1 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 1 / 4 | 20 € | -20,00 € | -100,0 % | 0 % |
| 2 – 3 | 74 / 92 | 1586 € | +116,00 € | +7,3 % | 44 % |
| 3 – 5 | 101 / 112 | 2020 € | -248,20 € | -12,3 % | 26 % |
| 5 – 10 | 10 / 14 | 200 € | +0,00 € | +0,0 % | 20 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 5 / 5 | 100 € | -52,00 € | -52,0 % | 20 % |
| Basketball | 9 / 37 | 180 € | -118,00 € | -65,6 % | 12 % |
| Football | 102 / 114 | 2095 € | -42,20 € | -2,0 % | 33 % |
| Football Américain | 5 / 5 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 19 / 19 | 380 € | -133,00 € | -35,0 % | 21 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XIII | 0 / 1 | 0 € | +0,00 € | – | – |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 26 / 29 | 550 € | +362,50 € | +65,9 % | 56 % |
| Tennis de table | 2 / 2 | 40 € | +55,00 € | +137,5 % | 50 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 186 / 230 | 3825 € | -152,20 € | -4,0 % | 32 % |

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
| 15/10 12h00 · A.Zverev - A.De Minaur | A.Zverev remporte le 1er set 6-3 ou 6-4 ? | 2,8 | – | – | 25 € | ⏳ |
| 15/10 11h05 · Australie - NlleZélande | Le duo Jamayne Isaako/Tom Trbojevic marque 2 essais ou + | 2,8 | – | – | 25 € | ⏳ |
| 15/10 10h30 · Brisbane Bullets - SE Melbourne Phoenix | SE Melbourne Phoenix gagne et plus de 192,5 points dans le match | 2,45 | 2,548 | -3,9 % ≈ | 20 € | ⏳ |
| 15/10 08h30 · Arthur Gea - Alejandro Davidovich Fokina | Arthur Gea gagne 2-1 | 4,75 | 4,85 | -2,1 % | 20 € | ⏳ |
| 15/10 04h30 · MLS | Los Angeles Galaxy et Los Angeles FC marquent chacun au moins 2 buts (respectivement contre Portland Timbers et Austin FC) | 2,4 | 2,499 | -4,0 % | 20 € | ⏳ |
| 15/10 02h45 · Colorado Avalanche - Dallas Stars | Nathan MacKinnon buteur et Colorado Avalanche gagne (hors prol. et TAB) | 3,4 | 5,167 | -34,2 % ≈ | 20 € | ❌ -20,00 € |
| 15/10 02h30 · Chicago Fire - Philadelphia Union | Robert Lewandowski marque au moins un but en 1ère mi-temps | 3,9 | – | – | 20 € | ❌ -20,00 € |
| 15/10 02h00 · Los Angeles Dodgers - Milwaukee Brewers | Los Angeles Dodgers gagne et moins de 8,5 runs dans le match | 2,5 | 2,695 | -7,2 % ≈ | 20 € | ❌ -20,00 € |
| 15/10 01h45 · Washington Capitals - Montreal Canadiens | Washington Capitals gagne et plus de 5,5 buts dans le match (hors prol. et TAB) | 3,6 | – | – | 20 € | ✅ +52,00 € |
| 15/10 01h30 · MLS | Au moins un but marqué en première mi-temps lors de chacun des 6 matchs à 1h30 | 3,25 | – | – | 20 € | ✅ +45,00 € |
| 15/10 01h30 · Toronto FC - Orlando City | Antoine Griezmann marque au moins un but ou fait au moins une passe décisive et Orlando City gagne | 3,0 | – | – | 20 € | ❌ -20,00 € |
| 15/10 01h30 · Inter Miami - New York City FC | Lionel Messi marque 2 buts ou plus | 3,5 | – | – | 20 € | ❌ -20,00 € |
| 14/10 21h00 · Man. City - Paris SG | Le Trio E.Haaland+O.Dembele+D.Doué marque au moins 2 buts en cumulé ? (Remboursé si non titulaire(s)) | 2,2 | – | – | 25 € | ✅ +30,00 € |

≈ : calcul approché (conditions liées sur un même match).
