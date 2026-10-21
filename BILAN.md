# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (257 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 257 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 186 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (255 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 255 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 151 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 21/10 02h21 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 437 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 437 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 311 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 379 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 341 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 241 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
| **B — valeur ≥ +5 %** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B0 — valeur ≥ 0 %** | 3 / 3 | 50 € | **-50,00 €** | **-100,0 %** | -50,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 44 / 48 | 424 € | **+19,39 €** | **+4,6 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 62 / 74 | 605 € | **+136,73 €** | **+22,6 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 65 / 77 | 430 € | **+60,82 €** | **+14,1 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 46 / 54 | 879 € | **+381,38 €** | **+43,4 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 144 en attente · cote moyenne 3,32 · pire série perdante 22

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
| non évaluable | 196 / 332 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 17 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 6 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 6 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 17 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 112 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 279 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 49 | 0 € | +0,00 € | – | – |
| match | 293 / 388 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 7 / 17 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 1 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 13.88 € | 1 / 2 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 296 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 52 / 112 | 1300 € | +31,25 € | +2,4 % | 39 % |
| 3.12 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5.74 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 6.25 € | 1 / 2 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 6 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 189 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 201 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 27 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 14 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 9 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 54 | 265 € | -68,00 € | -25,7 % | 25 % |
| Football | 159 / 236 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 11 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 37 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 8 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 4 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 9 | 180 € | +84,00 € | +46,7 % | 56 % |
| Tennis | 40 / 52 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 6 | 120 € | -25,00 € | -20,8 % | 17 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 437 | 6002 € | -235,78 € | -3,9 % | 32 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 24/10 18h30 · Chelsea - Tottenham | Cold Palmer Buteur! | 2,6 | – | – | 20 € | ⏳ |
| 22/10 18h45 · SK Sturm Graz - Marseille | Amine Gouiri Buteur | 2,5 | – | – | 20 € | ⏳ |
| 21/10 18h45 · Côme - Manchester United | Nico Paz Buteur | 3,2 | – | – | 20 € | ⏳ |
| 21/10 18h45 · Lille - Galatasaray | Rafael Leao Buteur | 3,6 | – | – | 20 € | ⏳ |
| 21/10 04h45 · Vegas Golden Knights - Tampa Bay Lightning | Mark Stone marque au moins un point et Vegas Golden Knights gagne (hors prol. et TAB) | 2,75 | – | – | 20 € | ⏳ |
| 21/10 04h30 · Lanlana Tararudee - Ashlyn Krueger | Ashlyn Krueger gagne 2-1 | 4,25 | – | – | 20 € | ⏳ |
| 21/10 03h45 · San Antonio Spurs - Oklahoma City Thunder | Victor Wembanyama marque au moins 30 points et San Antonio Spurs gagne | 4,5 | – | – | 20 € | ⏳ |
| 21/10 03h45 · NBA 2026 - 2027 | San Antonio Spurs gagne le titre NBA | 4,5 | – | – | 20 € | ⏳ |
| 21/10 03h15 · Edmonton Oilers - Minnesota Wild | Leon Draisaitl et Connor McDavid marquent chacun au moins un but (avec Garantie Golden Goal) | 5,25 | – | – | 20 € | ⏳ |
| 21/10 02h30 · San Antonio Spurs - Oklahoma City Thunder | Spurs gagne et Wembanyama marque au moins 30 points et 13 rebonds | 5,35 | – | – | 5.74 € | ⏳ |
| 21/10 02h07 · Guadalajara - Necaxa | Guadalajara gagne et les deux équipes marquent | 2,75 | – | – | 20 € | ⏳ |
| 21/10 01h15 · New York Knicks - Philadelphia 76ers | Philadelphia 76ers gagne et plus de 225,5 points dans le match | 3,5 | – | – | 20 € | ⏳ |
| 21/10 01h10 · Montreal Canadiens - San Jose Sharks | Cole Caufield buteur et Montreal Canadiens gagne (hors prol. et TAB) | 2,75 | – | – | 20 € | ⏳ |
| 20/10 21h10 · Detroit Pistons - Boston Celtics | Jayson Tatum marque au moins 25 points et Boston Celtics gagne | 2,75 | – | – | 20 € | ⏳ |
| 20/10 21h00 · DET Pistons - BOS Celtics | NBA - Jayson Tatum marque 30pts ou + | 2,45 | – | – | 25 € | ⏳ |
| 20/10 21h00 · Stuttgart - Atl. Madrid | J.Alvarez décisif et son équipe gagne (remboursé si non titulaire) | 3,0 | – | – | 25 € | ⏳ |
| 20/10 21h00 · Paris SG - FC Barcelone | Au moins 2 des 3 joueurs marquent : O.Dembele / L.Yamal / D.Doué (remboursé si non titulaires) | 2,65 | – | – | 25 € | ⏳ |
| 20/10 21h00 · Paris SG - FC Barcelone | Paris SG gagne et les deux équipes marquent | 2,95 | – | – | 25 € | ⏳ |
| 20/10 21h00 · Liverpool - Villarreal | Le duo A.Isak / B.Barcola marque plus de 1,5 buts (remboursé si non titulaire) | 3,0 | – | – | 25 € | ⏳ |
| 20/10 21h00 · Ligue des Champions - 20/10 | Le trio R.Cherki / D.Malen / S.Aghehowa marque plus de 2,5 buts (Remboursé si non titulaires) | 2,65 | – | – | 25 € | ⏳ |
| 20/10 21h00 · Naples - Bodø/Glimt | Naples gagne à la mi-temps et à la fin du match | 2,65 | – | – | 20 € | ⏳ |
| 20/10 21h00 · Stuttgart - Atletico Madrid | Atletico Madrid marque dans les deux mi-temps | 2,5 | – | – | 20 € | ⏳ |
| 20/10 21h00 · AS Rome - Slovan Bratislava | Donyell Malen marque au moins un but en 1ère mi-temps | 2,2 | – | – | 20 € | ⏳ |
| 20/10 21h00 · Liverpool - Villarreal | Liverpool gagne les deux mi-temps | 3,5 | – | – | 20 € | ⏳ |
| 20/10 21h00 · Manchester City - AEK Athènes | Manchester City gagne et plus de 4,5 buts dans le match | 2,65 | – | – | 20 € | ⏳ |
| 20/10 21h00 · Paris SG - FC Barcelone | Paris SG gagne et les deux équipes marquent | 3,1 | – | – | 20 € | ⏳ |
| 20/10 21h00 · Cote Boostée Wiloo : CB Wiloo Paris SG - FC Barcelone | D. Doué marque au moins un but ou fait au moins une passe décisive | 2,0 | – | – | 20 € | ⏳ |
| 20/10 21h00 · O.Dembélé ou D.Doué buteur et le PSG - Barcelone | O.Dembélé ou D.Doué buteur et le PSG (vs Barcelone) ne perd pas ? | 2,3 | – | – | 10 € | ⏳ |
| 20/10 21h00 · O.Dembélé ou D.Doué buteur et le PSG - Barcelone | O.Dembélé ou D.Doué buteur et le PSG (vs Barcelone) ne perd pas ? | 2,1 | – | – | 10 € | ⏳ |
| 20/10 21h00 · Ousmane Dembélé - FC Barcelone | Ousmane Dembélé (vs FC Barcelone) buteur ou passeur décisif | 1,8 | – | – | 10 € | ⏳ |
| 20/10 21h00 · Paris SG - FC Barcelone | Le PSG mène à la mi-temps et gagne le match | 3,35 | – | – | 20 € | ⏳ |
| 20/10 20h00 · Boston Celtics - Detroit Pistons | J. Tatum marque plus de 24.5 points, plus de 4.5 assists et 9.5 rebonds — Ըես | 3,5 | – | – | 10 € | ⏳ |
| 20/10 20h00 · Trio buteur | S. Aghehowa, D. Malen et J. Alvares marquent au total plus de 2.5 goals | 2,7 | – | – | 14.7 € | ⏳ |
| 20/10 20h00 · Ligue des Champions | Plus de 2.5 buts dans chacun des 7 matchs de 21h | 9,0 | – | – | 3.12 € | ⏳ |
| 20/10 20h00 · Paris SG - Barcelone | Paris SG gagne et O. Dembélé buteur | 3,7 | – | – | 9.25 € | ⏳ |
| 20/10 19h55 · M.Berrettini - K.Jacquet | K.Jacquet remporte le 1er set et le match ? | 2,7 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | IND Pacers - Les Pacers remportent la Division Centrale | 4,25 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MEM Grizzlies - Cameron Boozer prend 8 rebonds ou + (moyenne) | 1,8 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | LA Clippers - Darius Garland fait 7 passes ou + (moyenne) | 1,6 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | HOU Rockets - Fred VanVleet fait 6 passes ou + (moyenne) | 2,1 | – | – | 25 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
