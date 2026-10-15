# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (120 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 90 / 120 | 1885 € | **+39,75 €** | **+2,1 %** | -17,5 % (41 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 65 / 85 | 650 € | **+30,00 €** | **+4,6 %** | -17,9 % (29 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (88 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 56 / 88 | 1171 € | +308,75 € | +26,4 % |
| **I — cotes modérées, un boost/match** | 35 / 51 | 350 € | +75,50 € | +21,6 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 15/10 23h12 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 205 / 270 | 4235 € | **-2,70 €** | **-0,1 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 5 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 205 / 270 | 2045 € | **+1,05 €** | **+0,1 %** | -337,50 € |
| **D — cote 1,60–3,50** | 144 / 188 | 1440 € | **+76,00 €** | **+5,3 %** | -238,00 € |
| **E — dans les 48 h** | 205 / 228 | 2045 € | **+1,05 €** | **+0,1 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 182 / 205 | 1815 € | **-69,95 €** | **-3,9 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 124 / 141 | 1240 € | **-25,00 €** | **-2,0 %** | -221,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 38 / 41 | 366 € | **-32,50 €** | **-8,9 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 48 / 52 | 465 € | **+76,23 €** | **+16,4 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 51 / 55 | 313 € | **+37,56 €** | **+12,0 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 33 / 37 | 625 € | **+258,77 €** | **+41,4 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 68 gagnés, 133 perdus, 4 remboursés, 65 en attente · cote moyenne 3,37 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 4 / 4 | 85 € | +51,25 € | +60,3 % | 50 % |
| EV 10 % et + (approx) | 3 / 3 | 60 € | +10,00 € | +16,7 % | 33 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 28 / 34 | 565 € | -242,75 € | -43,0 % | 21 % |
| EV < 0 (exacte) | 26 / 32 | 530 € | +204,50 € | +38,6 % | 44 % |
| non évaluable | 141 / 194 | 2935 € | -120,70 € | -4,1 % | 33 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 4 / 9 | 80 € | +16,00 € | +20,0 % | 50 % |
| Genybet | 0 / 1 | 0 € | +0,00 € | – | – |
| NetBet | 1 / 2 | 10 € | +17,50 € | +175,0 % | 100 % |
| OlyBet | 3 / 4 | 35 € | +38,55 € | +108,9 % | 67 % |
| Unibet | 34 / 74 | 850 € | +126,25 € | +14,9 % | 46 % |
| Winamax | 163 / 180 | 3260 € | -201,00 € | -6,2 % | 30 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 38 | 0 € | +0,00 € | – | – |
| match | 205 / 232 | 4235 € | -2,70 € | -0,1 % | 34 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 1 / 4 | 10 € | +17,50 € | +175,0 % | 100 % |
| 20 € | 167 / 189 | 3340 € | -185,00 € | -5,5 % | 30 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 34 / 74 | 850 € | +126,25 € | +14,9 % | 46 % |
| 6.25 € | 1 / 1 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 2 / 5 | 40 € | -40,00 € | -100,0 % | 0 % |
| 2 – 3 | 87 / 110 | 1871 € | +287,50 € | +15,4 % | 46 % |
| 3 – 5 | 106 / 131 | 2125 € | -250,20 € | -11,8 % | 26 % |
| 5 – 10 | 10 / 15 | 200 € | +0,00 € | +0,0 % | 20 % |
| < 2 | 0 / 9 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 6 / 7 | 120 € | -72,00 € | -60,0 % | 17 % |
| Basketball | 10 / 38 | 200 € | -138,00 € | -69,0 % | 11 % |
| Football | 112 / 139 | 2310 € | +92,30 € | +4,0 % | 35 % |
| Football Américain | 5 / 6 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 19 / 24 | 380 € | -133,00 € | -35,0 % | 21 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XIII | 2 / 2 | 45 € | +10,00 € | +22,2 % | 50 % |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 30 / 33 | 640 € | +427,50 € | +66,8 % | 57 % |
| Tennis de table | 3 / 3 | 60 € | +35,00 € | +58,3 % | 33 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 205 / 270 | 4235 € | -2,70 € | -0,1 % | 34 % |

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
| 20/10 19h00 · Paris Trashtalk 26/27 | PHI 76ers - Les 76ers finissent champions NBA | 9,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MIA Heat - Le Heat remporte la Division Sud-Est | 3,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CLE Cavaliers - Les Cavaliers remportent la Division Centrale | 3,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | SAC Kings - Maxime Raynaud meilleur rebondeur des Kings (total de rebonds) | 2,5 | – | – | 25 € | ⏳ |
| 18/10 17h30 · Nottingham Forest - Arsenal | Arsenal mène à la mi-temps et gagne le match | 2,1 | 3,854 | -45,5 % ≈ | 20 € | ⏳ |
| 18/10 15h00 · Angers - Marseille | Amine Gouiri Buteur! | 2,55 | – | – | 20 € | ⏳ |
| 17/10 18h30 · Bayern Munich - Leipzig | Le Bayern gagne 3-0 | 12,5 | – | – | 20 € | ⏳ |
| 17/10 17h15 · Strasbourg - Paris SG | Kvara Buteur! | 2,3 | – | – | 20 € | ⏳ |
| 16/10 12h00 · Medvedev, Daniil - Paul, Tommy | Daniil Medvedev gagne 2-1 | 3,5 | 3,736 | -6,3 % | 20 € | ⏳ |
| 16/10 08h30 · Rafael Jodar - Casper Ruud | Rafael Jodar gagne 2-0 | 2,85 | 3,036 | -6,1 % | 20 € | ⏳ |
| 16/10 04h15 · Vegas Golden Knights - Calgary Flames | Vegas Golden Knights gagne et plus de 5,5 buts dans le match (hors prol. et TAB) | 2,4 | – | – | 20 € | ⏳ |
| 16/10 03h15 · Edmonton Oilers - Utah Mammoth | Leon Draisaitl buteur et Edmonton Oilers gagne (hors prol. et TAB) | 4,0 | 5,859 | -31,7 % ≈ | 20 € | ⏳ |
| 16/10 02h30 · Estudiantes - Flamengo | Flamengo gagne le match 1-0, 2-0 ou 3-0 | 3,25 | – | – | 20 € | ⏳ |
| 16/10 02h15 · Chicago Blackhawks - Winnipeg Jets | Kyle Connor buteur et Winnipeg Jets gagne (hors prol. et TAB) | 3,75 | 5,645 | -33,6 % ≈ | 20 € | ⏳ |
| 16/10 02h15 · Denver Broncos - Seattle Seahawks | Jaxon Smith-Njigba marque au moins un touchdown et Seattle Seahawks gagne | 2,8 | 3,835 | -27,0 % ≈ | 20 € | ⏳ |
| 16/10 02h00 · Los Angeles Dodgers - Milwaukee Brewers | Los Angeles Dodgers réalise au moins 6 runs | 2,9 | 3,208 | -9,6 % | 20 € | ⏳ |
| 16/10 01h15 · NHL | Tampa Bay Lightning et Florida Panthers marquent chacun au moins 4 buts (respectivement contre Seattle Kraken et Vancouver Canucks) (hors prol. et TAB) | 3,2 | 3,6 | -11,1 % | 20 € | ⏳ |
| 15/10 21h00 · Marseille - Olympiakos | I.Paixao décisif et son équipe gagne (remboursé si non titulaire) | 3,4 | – | – | 25 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
