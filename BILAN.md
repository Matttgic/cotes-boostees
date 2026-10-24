# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (412 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 412 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 302 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (439 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 439 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 256 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 24/10 22h32 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 621 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 621 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 436 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 553 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 493 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 346 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
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

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 328 en attente · cote moyenne 3,39 · pire série perdante 22

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
| non évaluable | 196 / 516 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 23 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 9 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 9 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 34 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 150 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 396 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 56 | 0 € | +0,00 € | – | – |
| match | 293 / 565 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 1.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 10 € | 7 / 23 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 1 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 13.88 € | 1 / 2 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.5 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 2.77 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 419 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 23.8 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 25 € | 52 / 150 | 1300 € | +31,25 € | +2,4 % | 39 % |
| 3.12 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 3.84 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 4.16 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 5 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 5.55 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 5.74 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 6.25 € | 1 / 2 | 6 € | +21,88 € | +350,1 % | 100 % |
| 6.66 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 7.69 € | 0 / 2 | 0 € | +0,00 € | – | – |
| 8.33 € | 1 / 2 | 8 € | -8,33 € | -100,0 % | 0 % |
| 9.09 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 10 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 264 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 288 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 42 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 17 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 7 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 10 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 83 | 265 € | -68,00 € | -25,7 % | 25 % |
| Football | 159 / 325 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 13 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 4 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 49 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 3 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 11 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 6 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 13 | 180 € | +84,00 € | +46,7 % | 56 % |
| Tennis | 40 / 85 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 6 | 120 € | -25,00 € | -20,8 % | 17 % |
| UFC/MMA | 0 / 1 | 0 € | +0,00 € | – | – |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 621 | 6002 € | -235,78 € | -3,9 % | 32 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 26/10 20h30 · Paris SG - Lyon | Maghnes Akliouche Buteur! | 2,85 | – | – | 20 € | ⏳ |
| 25/10 17h15 · Marseille - Le Havre | Amine Harit PASSEUR DECISIF | 3,75 | – | – | 20 € | ⏳ |
| 25/10 15h00 · Monaco - Lille | Monaco gagne 2-0 | 10,0 | – | – | 20 € | ⏳ |
| 25/10 03h30 · MLS | Chaque équipe marque lors des matchs suivants : San Diego FC - Seattle Sounders et Portland Timbers - Charlotte FC | 2,0 | – | – | 20 € | ⏳ |
| 25/10 02h00 · DAL Mavericks - SA Spurs | NBA - Victor Wembanyama : 25 points ou +, 7 rebonds ou +, 3 passes ou + | 2,9 | – | – | 25 € | ⏳ |
| 25/10 02h30 · MLS | FC Dallas et Vancouver Whitecaps gagnent chacun leur match (respectivement contre San Jose Earthquakes et Colorado Rapids) | 4,0 | – | – | 20 € | ⏳ |
| 25/10 02h10 · Dallas Mavericks - San Antonio Spurs | Victor Wembanyama marque au moins 30 points et San Antonio Spurs gagne | 2,75 | – | – | 20 € | ⏳ |
| 25/10 02h00 · NBA | Anthony Davis et Nikola Jokic marquent au moins 25 points chacun (respectivement contre Chicago Bulls et New Orleans Pelicans) | 3,5 | – | – | 20 € | ⏳ |
| 25/10 01h30 · DC United - Cincinnati FC | Les deux équipes marquent en première mi-temps | 3,0 | – | – | 20 € | ⏳ |
| 25/10 01h30 · NBA | Cleveland Cavaliers et Philadelphia 76ers gagnent chacun par au moins 12 points d'écart (respectivement contre Brooklyn Nets et Milwaukee Bucks) | 3,6 | – | – | 20 € | ⏳ |
| 25/10 01h10 · Edmonton Oilers - Toronto Maple Leafs | Leon Draisaitl buteur et Edmonton Oilers gagne (hors prol. et TAB) | 3,0 | – | – | 20 € | ⏳ |
| 25/10 00h10 · Charlotte Hornets - Miami Heat | Giannis Antetokounmpo réalise une performance points + rebonds + passes décisives d'au moins 50 | 2,55 | – | – | 20 € | ⏳ |
| 25/10 00h00 · CHA Hornets - MIA Heat | NBA - G.Antetokounmpo marque 29pts ou + et N.Reid marque 16pts ou + | 2,4 | – | – | 25 € | ⏳ |
| 24/10 23h30 · New York City FC - Inter Miami | Lionel Messi marque 2 buts ou plus | 4,3 | – | – | 20 € | ⏳ |
| 24/10 22h15 · Alex Volkanovski - Movsar Evloev | Alex Volkanovski gagne par KO, KO technique ou disqualification | 5,75 | – | – | 20 € | ⏳ |
| 24/10 21h45 · New Jersey Devils - Los Angeles Kings | N. Hischier buteur et New Jersey Devils gagne (hors prol. et TAB) | 4,25 | – | – | 20 € | ⏳ |
| 24/10 21h45 · Petr Yan - Merab Dvalishvili | Merab Dvalishvili gagne par décision | 3,3 | – | – | 20 € | ⏳ |
| 24/10 21h20 · A.Volkov - M.Elvoev | A.Volkanovski gagne aux points | 2,95 | – | – | 25 € | ⏳ |
| 24/10 21h00 · Toulon - Pau | Toulon gagne et le duo R.Marta / T.Attissogbé marque au moins 1 essai ? | 2,75 | – | – | 25 € | ⏳ |
| 24/10 21h00 · RC Toulon - Section Paloise | Plus de 8,5 essais lors du match | 2,75 | – | – | 20 € | ⏳ |
| 24/10 21h00 · Atletico Madrid - Deportivo La Corogne | Atletico Madrid marque au moins 4 buts contre Deportivo La Corogne | 4,0 | – | – | 20 € | ⏳ |
| 24/10 21h00 · Atletico Madrid - Deportivo La Corogne | Atletico Madrid gagne par 3+ buts d'écart et Julian Alvarez buteur | 4,0 | – | – | 8.33 € | ⏳ |
| 24/10 20h45 · Lens - Paris FC | Le duo F.Thauvin / L.Sinayoko cumule plus de 1,5 buts et/ou passes décisives (remboursé si non titulaires) | 2,45 | – | – | 25 € | ⏳ |
| 24/10 20h45 · Lens - Paris FC | Florian Thauvin marque au moins un but ou fait au moins une passe décisive et Lens gagne ou fait match nul | 2,5 | – | – | 20 € | ⏳ |
| 24/10 20h45 · Lazio Rome - Parme | Tijjani Noslin marque au moins un but en 1ère mi-temps | 4,5 | – | – | 20 € | ⏳ |
| 24/10 20h45 · Saint-Etienne - Nantes | Irvin Cardona buteur et Saint-Etienne gagne | 3,6 | – | – | 20 € | ⏳ |
| 24/10 20h45 · Lens - Paris FC | Florian Thauvin marque au moins 1+ buts et fait au moins 1+ passes décisives | 11,0 | – | – | 2.5 € | ⏳ |
| 24/10 20h45 · LES DEUX JOUEURS MARQUENT | Franjo Ivanovic et Lassine Sinayoko marquent chacun au moins 1+ but | 7,0 | – | – | 4.16 € | ⏳ |
| 24/10 20h45 · Lens/Paris FC - Thauvin ou Sinayoko premier buteur | Lens/Paris FC - Thauvin ou Sinayoko premier buteur | 4,0 | – | – | 10 € | ⏳ |
| 24/10 19h00 · Atlanta Dream - Golden State Valkyries | Angel Reese marque au moins 20 points et Atlanta Dream gagne | 4,0 | – | – | 20 € | ⏳ |
| 24/10 19h00 · Nantes - Chambéry | Nantes marque au moins 37 buts | 2,4 | – | – | 20 € | ⏳ |
| 24/10 18h30 · A.Fils - JL.Struff | A.Fils remporte le 1er set et plus de 9,5 jeux dans le set ? | 2,55 | – | – | 25 € | ⏳ |
| 24/10 18h30 · Chelsea - Tottenham | Joao Pedro décisif et son équipe gagne (remboursé si non titulaire) | 2,55 | – | – | 25 € | ⏳ |
| 24/10 18h30 · Arthur Fils - Jan-Lennard Struff | Au moins un Tie-break lors du match | 2,15 | – | – | 20 € | ⏳ |
| 24/10 18h30 · Borussia Dortmund - Eintracht Francfort | Serhou Guirassy premier buteur du match | 4,0 | – | – | 20 € | ⏳ |
| 24/10 18h30 · Chelsea - Tottenham | Chelsea gagne le match 2-1, 3-1 ou 4-1 | 5,0 | – | – | 20 € | ⏳ |
| 24/10 18h30 · Dortmund - Eintracht Francfort | Serhou Guirassy marque dans chaque mi-temps | 7,0 | – | – | 4.16 € | ⏳ |
| 24/10 18h30 · Chelsea - Tottenham | Chelsea gagne par 2+ buts d'écart et Joao Pedro buteur | 4,25 | – | – | 7.69 € | ⏳ |
| 24/10 18h30 · Chelsea / Tottenham : Les 2 équipes marquent (mise max 10 €) | Chelsea / Tottenham : Les 2 équipes marquent (mise max 10 €) | 1,6 | – | – | 10 € | ⏳ |
| 24/10 18h30 · Chelsea - Tottenham | Cold Palmer Buteur! | 2,6 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
