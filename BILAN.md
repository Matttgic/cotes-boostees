# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (692 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 692 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 510 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (786 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 786 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 472 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 02/11 20h11 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 968 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 968 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 689 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 884 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 785 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 562 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
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

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 675 en attente · cote moyenne 3,37 · pire série perdante 22

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
| non évaluable | 196 / 863 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 40 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 19 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 15 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 68 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 204 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 622 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 68 | 0 € | +0,00 € | – | – |
| match | 293 / 900 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 1.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 1.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 10 € | 7 / 40 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 3 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 12.5 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.15 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.88 € | 1 / 3 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 3 | 0 € | +0,00 € | – | – |
| 16.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 17.24 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.5 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.63 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.77 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 663 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 23.8 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 52 / 205 | 1300 € | +31,25 € | +2,4 % | 39 % |
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
| 8.92 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 9.09 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 9.61 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 13 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 409 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 463 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 59 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 24 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 9 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 14 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 140 | 265 € | -68,00 € | -25,7 % | 25 % |
| Foot américain | 0 / 1 | 0 € | +0,00 € | – | – |
| Football | 159 / 498 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 20 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 7 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 5 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 74 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 3 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 14 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 7 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 14 | 180 € | +84,00 € | +46,7 % | 56 % |
| Ski Alpin | 0 / 1 | 0 € | +0,00 € | – | – |
| Tennis | 40 / 148 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 10 | 120 € | -25,00 € | -20,8 % | 17 % |
| UFC/MMA | 0 / 1 | 0 € | +0,00 € | – | – |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 886 | 6002 € | -235,78 € | -3,9 % | 32 % |
| 2026-11 | 0 / 82 | 0 € | +0,00 € | – | – |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 04/11 11h00 · ATP Paris | Carlos Alcaraz remporte le tournoi | 3,5 | – | – | 20 € | ⏳ |
| 03/11 21h00 · Villarreal - Paris SG | Désiré Doué Buteur | 2,35 | – | – | 20 € | ⏳ |
| 03/11 18h45 · Galatasaray - Stuttgart | Rafael Leao Décisif | 2,1 | – | – | 20 € | ⏳ |
| 03/11 04h00 · LA Lakers - MIA Heat | Luka Doncic termine meilleur marqueur du match et son équipe gagne | 2,45 | – | – | 25 € | ⏳ |
| 03/11 02h40 · Houston Rockets - Boston Celtics | Jayson Tatum marque au moins 25 points et Boston Celtics gagne | 3,5 | – | – | 20 € | ⏳ |
| 03/11 02h35 · San Antonio Spurs - Utah Jazz | Victor Wenbanyama marque au moins 20 points, prend au moins 10 rebonds et réalise au moins 3 contres | 2,85 | – | – | 20 € | ⏳ |
| 03/11 02h30 · HOU Rockets - BOS Celtics | NBA - Jayson Tatum termine meilleur marqueur du match | 2,3 | – | – | 25 € | ⏳ |
| 03/11 02h15 · Bucaramanga - Atletico Nacional | Atletico Nacional marque dans les deux mi-temps | 3,5 | – | – | 20 € | ⏳ |
| 03/11 02h10 · Boston Bruins - Vegas Golden Knights | N. MacKinnon buteur et Colorado Avalanche gagne (hors prol. et TAB) | 3,0 | – | – | 20 € | ⏳ |
| 03/11 02h10 · Seattle Seahawks - Chicago Bears | Jaxon Smith-Njigba marque au moins un touchdown et Seattle Seahawks gagne | 2,5 | – | – | 20 € | ⏳ |
| 03/11 01h40 · New York Knicks - Brooklyn Nets | Jalen Brunson marque au moins 25 points et distribue au moins 5 passes décisives | 2,3 | – | – | 20 € | ⏳ |
| 03/11 01h15 · Independiente Rivadavia - Banfield | Independiente Rivadavia gagne le match 1-0, 2-0 ou 3-0 | 2,85 | – | – | 20 € | ⏳ |
| 03/11 01h10 · Boston Bruins - Vegas Golden Knights | M. Stone, J. Eichel et M. Marner marquent chacun au moins 1 point (avec Garantie Golden Goal) | 2,3 | – | – | 20 € | ⏳ |
| 03/11 01h10 · Cleveland Cavaliers - Oklahoma City Thunder | Do. Mitchell + S. Gilgeous-Alexander marquent 60 points ou plus | 3,25 | – | – | 20 € | ⏳ |
| 03/11 00h00 · Bragantino SP - Santos | Gabriel Barbosa marque au moins un but en 1ère mi-temps | 4,75 | – | – | 20 € | ⏳ |
| 02/11 21h15 · Liga Portugal | Chaque équipe marque lors des matchs suivants : Gil Vicente - Vitoria Guimaraes et Benfica - Alverca FC | 3,65 | – | – | 20 € | ⏳ |
| 02/11 21h00 · Newcastle - Everton | Newcastle gagne et les deux équipes marquent | 3,75 | – | – | 20 € | ⏳ |
| 02/11 20h45 · Lorient - Brest | Ib.Baldé ou L.Ajorque buteur et les 2 équipes marquent ? (Remboursé si non titulaire(s)) | 2,55 | – | – | 25 € | ⏳ |
| 02/11 20h45 · Ligue 2 BKT® | Plus de 2,5 buts dans chacun des 2 matchs du jour | 3,25 | – | – | 20 € | ⏳ |
| 02/11 20h45 · Lorient - Brest | Ludovic Ajorque marque au moins un but ou fait au moins une passe décisive | 2,75 | – | – | 20 € | ⏳ |
| 02/11 20h45 · Lorient - Brest | Les 2 équipes marquent et plus de 2.5 buts | 2,7 | – | – | 14.7 € | ⏳ |
| 02/11 20h45 · Lorient / Brest : Plus de 2,5 buts (mise max 10 €) | Lorient / Brest : Plus de 2,5 buts (mise max 10 €) | 2,2 | – | – | 10 € | ⏳ |
| 02/11 20h30 · U.Humbert - Van De Zandsch | U.Humbert gagne le 1er set 6-3 ou 6-4 ? | 3,1 | – | – | 25 € | ⏳ |
| 02/11 20h30 · Ugo Humbert - Botic van de Zandschulp | Ugo Humbert gagne et plus de 22,5 jeux dans le match | 3,0 | – | – | 20 € | ⏳ |
| 02/11 20h30 · U. Humbert - B. Van De Zandschulp | Humbert gagne 2 sets 0 | 2,45 | – | – | 17.24 € | ⏳ |
| 02/11 19h00 · D.Shapovalov - K.Khachanov | K.Khachanov gagne et plus de 22,5 jeux dans le match ? | 3,1 | – | – | 25 € | ⏳ |
| 02/11 19h00 · Denis Shapovalov - Karen Khachanov | Karen Khachanov gagne 2-0 | 2,35 | – | – | 20 € | ⏳ |
| 02/11 18h30 · Sassuolo - Fiorentina | Franco Mastantuono Décisif | 2,4 | – | – | 20 € | ⏳ |
| 02/11 16h40 · Alex Molcan - Titouan Droguet | Titouan Droguet gagne 2-1 | 4,5 | – | – | 20 € | ⏳ |
| 02/11 16h20 · Kyrian Jacquet - Tomas Machac | Kyrian Jacquet gagne le premier set et le match | 3,25 | – | – | 20 € | ⏳ |
| 02/11 16h15 · Real Oviedo - UD Las Palmas | Real Oviedo ou UD Las Palmas gagne et les deux équipes marquent | 2,75 | – | – | 20 € | ⏳ |
| 02/11 14h30 · Mattia Bellucci - Lorenzo Sonego | Mattia Bellucci gagne 2-0 | 3,5 | – | – | 20 € | ⏳ |
| 02/11 14h30 · Norrie, Cameron - Arnaldi, Matteo | Cameron Norrie gagne 2 sets à 0 | 2,1 | – | – | 20 € | ⏳ |
| 02/11 12h10 · Luca Van Assche - Mariano Navone | Luca Van Assche gagne 2-0 | 2,5 | – | – | 20 € | ⏳ |
| 02/11 11h00 · Lorenzo Musetti - Hubert Hurkacz | Plus de 2,5 sets lors du match | 2,25 | – | – | 20 € | ⏳ |
| 02/11 09h30 · Melbourne United - New Zealand Breakers | Plus de 199,5 points lors du match | 3,0 | – | – | 20 € | ⏳ |
| 02/11 07h00 · Viktorija Golubic - Katie Boulter | Katie Boulter gagne 2-0 | 2,6 | – | – | 20 € | ⏳ |
| 02/11 03h10 · Los Angeles Lakers - Toronto Raptors | Luka Doncic réalise une performance points + rebonds + passes décisives d'au moins 55 | 3,25 | – | – | 20 € | ⏳ |
| 02/11 03h00 · LA Lakers - TOR Raptors | NBA - Luka Doncic et Scottie Barnes marquent 25pts ou + chacun | 2,45 | – | – | 25 € | ⏳ |
| 02/11 02h20 · Washington Commanders - Philadelphia Eagles | Rachaad White marque au moins un touchdown et Washington Commanders gagne | 2,5 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
