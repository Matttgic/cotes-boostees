# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (138 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 110 / 138 | 2305 € | **-190,25 €** | **-8,3 %** | -17,5 % (47 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 79 / 97 | 790 € | **-55,00 €** | **-7,0 %** | -17,1 % (33 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (106 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 78 / 106 | 1611 € | +58,75 € | +3,6 % |
| **I — cotes modérées, un boost/match** | 48 / 62 | 480 € | +0,50 € | +0,1 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 16/10 13h15 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 227 / 288 | 4675 € | **-252,70 €** | **-5,4 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 5 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 227 / 288 | 2265 € | **-123,95 €** | **-5,5 %** | -337,50 € |
| **D — cote 1,60–3,50** | 159 / 200 | 1590 € | **-19,00 €** | **-1,2 %** | -238,00 € |
| **E — dans les 48 h** | 227 / 245 | 2265 € | **-123,95 €** | **-5,5 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 200 / 221 | 1995 € | **-154,95 €** | **-7,8 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 137 / 152 | 1370 € | **-100,00 €** | **-7,3 %** | -221,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 39 / 44 | 376 € | **-42,17 €** | **-11,2 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 50 / 57 | 485 € | **+56,23 €** | **+11,6 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 53 / 60 | 326 € | **+24,42 €** | **+7,5 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 35 / 41 | 665 € | **+218,77 €** | **+32,9 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 71 gagnés, 152 perdus, 4 remboursés, 61 en attente · cote moyenne 3,38 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 4 / 4 | 85 € | +51,25 € | +60,3 % | 50 % |
| EV 10 % et + (approx) | 3 / 3 | 60 € | +10,00 € | +16,7 % | 33 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 33 / 37 | 670 € | -347,75 € | -51,9 % | 18 % |
| EV < 0 (exacte) | 31 / 35 | 620 € | +114,50 € | +18,5 % | 37 % |
| non évaluable | 153 / 206 | 3180 € | -175,70 € | -5,5 % | 33 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 4 / 9 | 80 € | +16,00 € | +20,0 % | 50 % |
| Genybet | 1 / 1 | 10 € | -10,00 € | -100,0 % | 0 % |
| NetBet | 2 / 2 | 20 € | +7,50 € | +37,5 % | 50 % |
| OlyBet | 3 / 4 | 35 € | +38,55 € | +108,9 % | 67 % |
| Unibet | 38 / 80 | 950 € | +26,25 € | +2,8 % | 40 % |
| Winamax | 179 / 192 | 3580 € | -331,00 € | -9,2 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 39 | 0 € | +0,00 € | – | – |
| match | 227 / 249 | 4675 € | -252,70 € | -5,4 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 3 / 4 | 30 € | -2,50 € | -8,3 % | 33 % |
| 20 € | 183 / 201 | 3660 € | -315,00 € | -8,6 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 38 / 80 | 950 € | +26,25 € | +2,8 % | 40 % |
| 6.25 € | 1 / 1 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 2 / 5 | 40 € | -40,00 € | -100,0 % | 0 % |
| 2 – 3 | 94 / 115 | 2021 € | +185,50 € | +9,2 % | 44 % |
| 3 – 5 | 120 / 142 | 2405 € | -388,20 € | -16,1 % | 24 % |
| 5 – 10 | 10 / 17 | 200 € | +0,00 € | +0,0 % | 20 % |
| < 2 | 1 / 9 | 10 € | -10,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 7 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 10 / 40 | 200 € | -138,00 € | -69,0 % | 11 % |
| Football | 125 / 147 | 2565 € | -34,70 € | -1,4 % | 33 % |
| Football Américain | 6 / 6 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 24 / 26 | 480 € | -171,00 € | -35,6 % | 21 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 4 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XIII | 3 / 3 | 70 € | -15,00 € | -21,4 % | 33 % |
| Rugby à XV | 5 / 6 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 31 / 36 | 660 € | +407,50 € | +61,7 % | 55 % |
| Tennis de table | 3 / 3 | 60 € | +35,00 € | +58,3 % | 33 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 227 / 288 | 4675 € | -252,70 € | -5,4 % | 32 % |

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
| 18/10 17h30 · Nottingham Forest - Arsenal | Arsenal mène à la mi-temps et gagne le match | 2,1 | 3,854 | -45,5 % ≈ | 20 € | ⏳ |
| 18/10 15h00 · Angers - Marseille | Amine Gouiri Buteur! | 2,55 | – | – | 20 € | ⏳ |
| 17/10 18h30 · Bayern Munich - Leipzig | Le Bayern gagne 3-0 | 12,5 | – | – | 20 € | ⏳ |
| 17/10 17h15 · Strasbourg - Paris SG | Kvara Buteur! | 2,3 | – | – | 20 € | ⏳ |
| 16/10 21h00 · Gloucester - Bordeaux | Bordeaux gagne et Tom Willis marque au moins 1 essai ? | 3,0 | – | – | 25 € | ⏳ |
| 16/10 21h00 · Deportivo La Corogne - Levante | Deportivo La Corogne gagne le match 1-0, 2-0 ou 3-0 | 4,0 | – | – | 20 € | ⏳ |
| 16/10 20h45 · Le Mans - Toulouse | L.Mafouta ou C.Tengstedt buteur et les deux équipes marquent (remboursé si non titulaire(s)) | 2,4 | – | – | 25 € | ⏳ |
| 16/10 20h45 · Frosinone - Sassuolo | Sassuolo gagne à la mi-temps et à la fin du match | 4,5 | 9,851 | -54,3 % ≈ | 20 € | ⏳ |
| 16/10 20h45 · Le Mans - Toulouse | C. Tengstedt ou L. Mafouta marque au moins un but en 1ère mi-temps | 2,8 | – | – | 20 € | ⏳ |
| 16/10 20h30 · Eintracht Francfort - Cologne | Eintracht Francfort gagne et plus de 3,5 buts dans le match | 3,15 | 3,64 | -13,5 % ≈ | 20 € | ⏳ |
| 16/10 20h15 · Synerglace Ligue Magnus | Bordeaux, Angers et Grenoble gagnent chacun leur match (respectivement contre Gap, Chamonix et Nice) (hors prol. et TAB) | 3,0 | 3,399 | -11,7 % | 20 € | ⏳ |
| 16/10 20h00 · Ligue 2 BKT | Les 5 équipes à domicile ne perdent pas leur match respectif | 4,3 | – | – | 25 € | ⏳ |
| 16/10 20h00 · Ligue 2 BKT® | Plus de 1,5 buts dans chacun des 5 matchs du jour | 4,0 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
