# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (293 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 166 / 293 | 3495 € | **-241,25 €** | **-6,9 %** | -16,5 % (65 paris) |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | +5,5 % (1 paris) |
| **D — hypothèse (cotes 1,60–3,50)** | 120 / 214 | 1200 € | **-103,50 €** | **-8,6 %** | -16,2 % (45 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (293 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 144 / 293 | 2937 € | +75,67 € | +2,6 % |
| **I — cotes modérées, un boost/match** | 93 / 175 | 930 € | +30,00 € | +3,2 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 21/10 21h44 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 293 / 475 | 6002 € | **-235,78 €** | **-3,9 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 7 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 293 / 475 | 2925 € | **-96,95 €** | **-3,3 %** | -337,50 € |
| **D — cote 1,60–3,50** | 209 / 341 | 2090 € | **-4,50 €** | **-0,2 %** | -238,00 € |
| **E — dans les 48 h** | 291 / 414 | 2905 € | **-76,95 €** | **-2,6 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 1 / 1 | 5 € | **-4,96 €** | **-100,0 %** | -4,96 € |
| **H — un boost/match** | 261 / 371 | 2605 € | **-112,95 €** | **-4,3 %** | -326,45 € |
| **I — cotes modérées, un boost/match** | 182 / 265 | 1820 € | **-70,50 €** | **-3,9 %** | -274,50 € |
| **B — valeur ≥ +5 %** | 2 / 2 | 40 € | **-40,00 €** | **-100,0 %** | -40,00 € |
| **B0 — valeur ≥ 0 %** | 3 / 3 | 50 € | **-50,00 €** | **-100,0 %** | -50,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 44 / 51 | 424 € | **+19,39 €** | **+4,6 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 62 / 74 | 605 € | **+136,73 €** | **+22,6 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 65 / 77 | 430 € | **+60,82 €** | **+14,1 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 46 / 54 | 879 € | **+381,38 €** | **+43,4 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 93 gagnés, 196 perdus, 4 remboursés, 182 en attente · cote moyenne 3,32 · pire série perdante 22

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
| non évaluable | 196 / 370 | 4070 € | -212,33 € | -5,2 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 7 / 17 | 140 € | +26,00 € | +18,6 % | 43 % |
| Genybet | 3 / 7 | 30 € | -10,00 € | -33,3 % | 33 % |
| NetBet | 3 / 7 | 30 € | -2,50 € | -8,3 % | 33 % |
| OlyBet | 7 / 17 | 82 € | +106,47 € | +129,8 % | 71 % |
| Unibet | 52 / 122 | 1300 € | +31,25 € | +2,4 % | 39 % |
| Winamax | 221 / 305 | 4420 € | -387,00 € | -8,8 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 52 | 0 € | +0,00 € | – | – |
| match | 293 / 423 | 6002 € | -235,78 € | -3,9 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 7 / 19 | 70 € | +12,50 € | +17,9 % | 43 % |
| 11.11 € | 1 / 1 | 11 € | -11,11 € | -100,0 % | 0 % |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 13.88 € | 1 / 2 | 14 € | +24,98 € | +180,0 % | 100 % |
| 14.7 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 20 € | 228 / 322 | 4560 € | -361,00 € | -7,9 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 52 / 122 | 1300 € | +31,25 € | +2,4 % | 39 % |
| 3.12 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 5.74 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 6.25 € | 1 / 2 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |
| 9.25 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 3 / 6 | 60 € | -60,00 € | -100,0 % | 0 % |
| 2 – 3 | 124 / 206 | 2650 € | +191,98 € | +7,2 % | 43 % |
| 3 – 5 | 151 / 218 | 3012 € | -387,76 € | -12,9 % | 25 % |
| 5 – 10 | 13 / 30 | 260 € | +40,00 € | +15,4 % | 23 % |
| < 2 | 2 / 15 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 9 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 13 / 63 | 265 € | -68,00 € | -25,7 % | 25 % |
| Football | 159 / 256 | 3212 € | -35,03 € | -1,1 % | 33 % |
| Football Américain | 6 / 11 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 32 / 41 | 640 € | -233,00 € | -36,4 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| MMA | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 6 / 8 | 150 € | -87,50 € | -58,3 % | 17 % |
| Rugby à XIII | 4 / 4 | 95 € | -40,00 € | -42,1 % | 25 % |
| Rugby à XV | 9 / 9 | 180 € | +84,00 € | +46,7 % | 56 % |
| Tennis | 40 / 57 | 855 € | +559,75 € | +65,5 % | 55 % |
| Tennis de table | 6 / 6 | 120 € | -25,00 € | -20,8 % | 17 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 293 / 475 | 6002 € | -235,78 € | -3,9 % | 32 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 24/10 18h30 · Chelsea - Tottenham | Cold Palmer Buteur! | 2,6 | – | – | 20 € | ⏳ |
| 22/10 18h45 · SK Sturm Graz - Marseille | Amine Gouiri Buteur | 2,5 | – | – | 20 € | ⏳ |
| 22/10 05h00 · Liga MX | Cruz Azul et Santos Laguna gagnent chacun leur match (respectivement contre Pachuca et UNAM) | 5,5 | – | – | 20 € | ⏳ |
| 22/10 04h30 · Ann Li - Zeynep Sonmez | Zeynep Sonmez gagne le premier set | 2,4 | – | – | 20 € | ⏳ |
| 22/10 04h30 · Los Angeles Clippers - Sacramento Kings | Darius Garland et Rui Hachimura marquent au moins 20 points chacun | 3,0 | – | – | 20 € | ⏳ |
| 22/10 04h00 · LA Lakers - GS Warriors | NBA - Luka Doncic et Stephen Curry marquent 25pts ou + chacun | 2,3 | – | – | 25 € | ⏳ |
| 22/10 04h00 · Los Angeles Lakers - Golden State Warriors | Luka Doncic et Stephen Curry marquent chacun au moins 4 paniers à 3 points | 2,75 | – | – | 20 € | ⏳ |
| 22/10 04h00 · NBA | Plus de 231,5 points lors de chacun des matchs suivants : Los Angeles Lakers - Golden State Warriors et Portland Trail Blazers - Phoenix Suns | 3,25 | – | – | 20 € | ⏳ |
| 22/10 02h40 · Houston Rockets - Dallas Mavericks | Kevin Durant marque au moins 30 points | 3,25 | – | – | 20 € | ⏳ |
| 22/10 02h10 · New Orleans Pelicans - Indiana Pacers | T. Haliburton marque au moins 20 points et Indiana Pacers gagne | 2,9 | – | – | 20 € | ⏳ |
| 22/10 02h00 · Atlanta Dream - Golden State Valkyries | Gabby Williams + Angel Reese marquent 40 points ou plus | 2,85 | – | – | 20 € | ⏳ |
| 22/10 01h45 · Buffalo Sabres - Philadelphia Flyers | Tage Thompson marque au moins 2 points (avec Garantie Golden Goal) | 3,1 | – | – | 20 € | ⏳ |
| 22/10 01h45 · Ottawa Senators - Florida Panthers | Brady Tkachuk buteur et Florida Panthers gagne (hors prol. et TAB) | 4,5 | – | – | 20 € | ⏳ |
| 22/10 01h40 · Buffalo Sabres - Philadelphia Flyers | Tage Thompson buteur et Buffalo Sabres gagne (hors prol. et TAB) | 3,5 | – | – | 20 € | ⏳ |
| 22/10 01h40 · Miami Heat - Minnesota Timberwolves | A. Edwards + G. Antetokounmpo marquent 65 points ou plus | 2,9 | – | – | 20 € | ⏳ |
| 22/10 01h30 · MIA Heat - MIN TWolves | NBA - Anthony Edwards termine meilleur marqueur du match | 2,45 | – | – | 25 € | ⏳ |
| 22/10 01h00 · Cincinnati FC - DC United | Evander marque au moins un but en 1ère mi-temps | 3,5 | – | – | 20 € | ⏳ |
| 21/10 21h00 · Ligue des Champions - 21/10 | Le trio L.Suarez / M.Thuram / N.Jackson marque plus de 2,5 buts (Remboursé si non titulaire(s)) | 2,25 | – | – | 25 € | ⏳ |
| 21/10 21h00 · Real Madrid - RB Leipzig | Kylian Mbappé buteur et son équipe gagne de 3 buts ou plus (remboursé si non titulaire) | 2,6 | – | – | 25 € | ⏳ |
| 21/10 21h00 · Club Bruges - Lens | F.Thauvin décisif et son équipe ne perd pas (remboursé si non titulaire) | 2,85 | – | – | 25 € | ⏳ |
| 21/10 21h00 · Bayern Munich - Arsenal | Le trio H.Kane / K.Havertz / L.Diaz marque plus de 1,5 buts (remboursé si non titulaires) | 2,4 | – | – | 25 € | ⏳ |
| 21/10 21h00 · Betis Séville - Feyenoord | Betis Séville gagne le match 1-0, 2-0 ou 3-0 | 4,75 | – | – | 20 € | ⏳ |
| 21/10 21h00 · Ligue des Champions | Chaque équipe marque lors des matchs suivants : Sporting Portugal - LASK Linz et Aston Villa - Viking | 3,3 | – | – | 20 € | ⏳ |
| 21/10 21h00 · Inter Milan - Shakhtar Donetsk | Inter Milan marque au moins 4 buts | 2,85 | – | – | 20 € | ⏳ |
| 21/10 21h00 · Bayern Munich - Arsenal | H. Kane premier buteur du match | 4,75 | – | – | 20 € | ⏳ |
| 21/10 21h00 · Club Bruges - Lens | Lens marque dans les deux mi-temps | 3,25 | – | – | 20 € | ⏳ |
| 21/10 21h00 · Real Madrid - Leipzig | Kylian Mbappé marque 2 buts ou plus | 2,5 | – | – | 20 € | ⏳ |
| 21/10 21h00 · Lens marque dans les 2 mi-temps ? - Bruges | Lens marque dans les 2 mi-temps ? (vs Bruges) | 3,0 | – | – | 10 € | ⏳ |
| 21/10 21h00 · Bayern Munich / Arsenal : Plus de 2,5 buts (mise max 10 €) | Bayern Munich / Arsenal : Plus de 2,5 buts (mise max 10 €) | 1,6 | – | – | 10 € | ⏳ |
| 21/10 19h00 · M.Kouame - L.Musetti | Les 2 joueurs gagnent un set ? | 2,7 | – | – | 25 € | ⏳ |
| 21/10 19h00 · Moïse Kouame - Lorenzo Musetti | Moïse Kouamé gagne le premier set et le match | 4,75 | – | – | 20 € | ⏳ |
| 21/10 18h45 · Lille - Galatasaray | Le trio V.Osimhen / O.Giroud / H.Haraldsson marque plus de 1,5 buts (remboursé si non titulaires) | 2,5 | – | – | 25 € | ⏳ |
| 21/10 18h45 · Ligue des Champions - 21/10 | Plus de 1,5 buts dans chacun des 9 matchs du jour | 2,85 | – | – | 25 € | ⏳ |
| 21/10 18h45 · Lille - Galatasaray | Lille gagne et plus de 1,5 buts dans le match | 2,8 | – | – | 25 € | ⏳ |
| 21/10 18h45 · Come - Manchester United | Manchester United gagne la première mi-temps | 3,2 | – | – | 20 € | ⏳ |
| 21/10 18h45 · Lille - Galatasaray | Lille gagne le match 2-1, 3,-1 ou 4-1 | 5,5 | – | – | 20 € | ⏳ |
| 21/10 18h45 · Côme - Manchester United | Nico Paz Buteur | 3,2 | – | – | 20 € | ⏳ |
| 21/10 18h45 · Lille - Galatasaray | Rafael Leao Buteur | 3,6 | – | – | 20 € | ⏳ |
| 21/10 17h30 · Liiga | Plus de 5,5 buts lors de chacun des matchs suivants : Tappara Tampere - Porin Ässät et Kiekko-Espoo - Kookoo | 4,0 | – | – | 20 € | ⏳ |
| 21/10 14h10 · Ekaterina Alexandrova - Marta Kostyuk | Marta Kostyuk gagne et plus de 21,5 jeux dans le match | 3,25 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
