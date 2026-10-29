# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (564 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 564 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 409 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (640 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 640 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 375 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 29/10 22h41 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 822 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 822 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 571 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 745 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 662 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 465 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
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

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 529 en attente · cote moyenne 3,43 · pire série perdante 22

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
| non évaluable | 196 / 717 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 36 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 15 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 11 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 62 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 176 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 522 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 62 | 0 € | +0,00 € | – | – |
| match | 293 / 760 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 1.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 1.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 10 € | 7 / 32 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 2 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 12.5 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.15 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 13.88 € | 1 / 2 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 16.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.08 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.5 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.63 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.77 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 559 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 23.8 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 52 / 177 | 1300 € | +31,25 € | +2,4 % | 39 % |
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
| 2 – 3 | 124 / 341 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 389 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 57 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 22 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 8 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 14 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 116 | 265 € | -68,00 € | -25,7 % | 25 % |
| Foot américain | 0 / 1 | 0 € | +0,00 € | – | – |
| Football | 159 / 423 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 17 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 5 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 5 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 61 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 3 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 12 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 6 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 14 | 180 € | +84,00 € | +46,7 % | 56 % |
| Ski Alpin | 0 / 1 | 0 € | +0,00 € | – | – |
| Tennis | 40 / 124 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 9 | 120 € | -25,00 € | -20,8 % | 17 % |
| UFC/MMA | 0 / 1 | 0 € | +0,00 € | – | – |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 820 | 6002 € | -235,78 € | -3,9 % | 32 % |
| 2026-11 | 0 / 2 | 0 € | +0,00 € | – | – |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 01/11 17h30 · Liverpool - Arsenal | Bradley Barcola Buteur | 4,1 | – | – | 20 € | ⏳ |
| 01/11 17h15 · Lyon - Angers | Ernest Nuamah Buteur! | 2,7 | – | – | 20 € | ⏳ |
| 31/10 16h00 · Manchester City - Brighton | Rayan Cherki Buteur! | 3,0 | – | – | 20 € | ⏳ |
| 31/10 13h30 · Chelsea - Manchester United | Bryan Mbeumo buteur! | 3,5 | – | – | 20 € | ⏳ |
| 30/10 19h00 · Nice - Rennes | Mousa Al-Taamari Décisif | 2,4 | – | – | 20 € | ⏳ |
| 30/10 19h00 · Le Havre - Paris SG | Maghnes Akliouche Buteur | 2,4 | – | – | 20 € | ⏳ |
| 30/10 18h00 · Novak Djokovic - Jan-Lennard Struff | Novak Djokovic gagne et plus de 22,5 jeux dans le match | 2,5 | – | – | 20 € | ⏳ |
| 30/10 03h10 · Portland Trail Blazers - Memphis Grizzlies | Damian Lillard marque au moins 25 points | 3,25 | – | – | 20 € | ⏳ |
| 30/10 03h10 · NHL | Ottawa Senators et San Jose Sharks gagnent chacun leur match (respectivement contre Los Angeles Kings et Vancouver Canucks) (prol. et TAB inclus) | 3,0 | – | – | 20 € | ⏳ |
| 30/10 01h15 · Green Bay Packers - Carolina Panthers | Josh Jacobs marque au moins un touchdown et Green Bay Packers gagne | 2,2 | – | – | 20 € | ⏳ |
| 30/10 01h10 · Dallas Stars - Montreal Canadiens | Jason Robertson buteur et Dallas Stars gagne (hors TAB) | 3,4 | – | – | 20 € | ⏳ |
| 30/10 01h00 · ATL Hawks - CLE Cavaliers | NBA - Jalen Johnson ou Donovan Mitchell marque 30pts ou + | 2,4 | – | – | 25 € | ⏳ |
| 30/10 01h00 · Atlanta Hawks - Cleveland Cavaliers | Donovan Mitchell et Nickeil Alexander-Walker marquent au moins 20 points chacun | 3,0 | – | – | 20 € | ⏳ |
| 29/10 23h30 · Serie A - Brésil | Chaque équipe marque lors des matchs suivants : Atlético Mineiro - Cruzeiro et Vasco da Gama - Flamengo | 2,6 | – | – | 20 € | ⏳ |
| 29/10 21h45 · Benfica - Gil Vicente | Benfica gagne le match 1-0, 2-0 ou 3-0 (hors prol. et TAB) | 3,1 | – | – | 20 € | ⏳ |
| 29/10 21h00 · Coupe du Roi | Athletic Bilbao et FC Séville gagnent chacun par au moins 4 buts d'écart (respectivement contre AE Prat et AD Sporting Hortaleza) (hors prol. et TAB) | 2,4 | – | – | 20 € | ⏳ |
| 29/10 20h45 · Fiorentina - Atalanta | N.Krstovic décisif et les deux équipes marquent (remboursé si non titulaire) | 2,4 | – | – | 25 € | ⏳ |
| 29/10 20h45 · Fiorentina - Atalanta | Fiorentina gagne par au moins 2 buts d'écart | 4,25 | – | – | 20 € | ⏳ |
| 29/10 20h45 · Fiorentina - Atalanta | Les 2 équipes marquent et plus de 3.5 buts | 2,5 | – | – | 16.66 € | ⏳ |
| 29/10 20h45 · Everton / Newcastle : Les 2 équipes marquent (mise max 10 €) | Everton / Newcastle : Les 2 équipes marquent (mise max 10 €) | 1,7 | – | – | 10 € | ⏳ |
| 29/10 20h05 · Maccabi Tel-Aviv - Paris Basketball | Nadir Hifi marque au moins 20 points et Paris Basketball gagne | 4,0 | – | – | 20 € | ⏳ |
| 29/10 20h00 · Flavio Cobolli - Matteo Berrettini | Flavio Cobolli gagne 2-1 | 4,2 | – | – | 20 € | ⏳ |
| 29/10 19h00 · Al-Nassr - Al-Kholood | Cristiano Ronaldo marque au moins un but en 1ère mi-temps (remboursé si non titulaire) | 2,5 | – | – | 20 € | ⏳ |
| 29/10 19h00 · Al Nassr Club - Al-Kholood | Joao Felix Buteur | 2,05 | – | – | 20 € | ⏳ |
| 29/10 18h45 · Paris FC - Hacken Gothenburg | Paris FC gagne 1-0 | 9,5 | – | – | 20 € | ⏳ |
| 29/10 18h30 · CB - Serie A (29/10) | Plus de 2,5 buts dans chacun des 2 matchs du jour | 2,35 | – | – | 25 € | ⏳ |
| 29/10 18h30 · Frosinone - Lecce | Frosinone gagne le match 1-0, 2-0 ou 3-0 | 4,75 | – | – | 20 € | ⏳ |
| 29/10 18h00 · N. Djokovic - J-L. Struff | Djokovic gagne et moins de 21.5 jeux | 2,9 | – | – | 13.15 € | ⏳ |
| 29/10 17h40 · Atlanta Dream - Golden State Valkyries | Gabby Williams réalise une performance points + rebonds + passes décisives d'au moins 30 | 2,75 | – | – | 20 € | ⏳ |
| 29/10 17h30 · Alexander Zverev - Tallon Griekspoor | Alexander Zverev gagne 2-1 | 3,5 | – | – | 20 € | ⏳ |
| 29/10 17h00 · Arthur Fery - Lorenzo Musetti | Moins de 20,5 jeux lors du match | 2,35 | – | – | 20 € | ⏳ |
| 29/10 17h00 · KHL | Plus de 4,5 buts lors de chacun des matchs suivants : Cherepovets - Spartak Moscou, Lokomotiv Yaroslavl - Sochi et Neftekhimik Niznekamsk - Vladivostok (prol. et TAB inclus) | 3,5 | – | – | 20 € | ⏳ |
| 29/10 15h35 · Al Khaleej Club - Al Hazem | Al Khaleej Club gagne et les deux équipes marquent | 4,0 | – | – | 20 € | ⏳ |
| 29/10 14h00 · A.Michelsen - A.Fils | A.Fils remporte le 1er set 6-3 ou 6-4 ? | 2,75 | – | – | 25 € | ⏳ |
| 29/10 14h00 · ATP Vienne | A. Fils et C. Alcaraz gagnent chacun leur match 2-0 (respectivement contre A. Michelsen et N. Basilashvili) | 3,15 | – | – | 20 € | ⏳ |
| 29/10 14h00 · A. Michelsen - A. Fils | Fils gagne et au moins 18 aces dans le match | 2,9 | – | – | 13.15 € | ⏳ |
| 29/10 12h00 · Valentin Vacherot - Rafael Jodar | Rafael Jodar gagne le premier set 7-5 ou 7-6 | 5,0 | – | – | 20 € | ⏳ |
| 29/10 10h00 · Brisbane Bullets - Cairns Taipans | Cairns Taipans gagne par au moins 6 points d'écart | 2,7 | – | – | 20 € | ⏳ |
| 29/10 06h30 · WTA Tokyo | Naomi Osaka et Elena Rybakina gagnent chacune leur match 2-0 (respectivement contre Mia Pohankova et Yulia Putintseva) | 2,35 | – | – | 20 € | ⏳ |
| 29/10 04h30 · Leylah Fernandez - Elise Mertens | Elise Mertens gagne 2-0 | 2,65 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
