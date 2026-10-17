# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (146 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 131 / 146 | 2750 € | **-264,50 €** | **-9,6 %** | -17,5 % (49 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 94 / 103 | 940 € | **-117,00 €** | **-12,4 %** | -17,1 % (35 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (120 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 103 / 120 | 2111 € | +78,53 € | +3,7 % |
| **I — cotes modérées, un boost/match** | 64 / 71 | 640 € | -8,50 € | -1,3 % |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 17/10 07h40 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 252 / 302 | 5176 € | **-232,92 €** | **-4,5 %** | -706,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 5 / 5 | 100 € | **+125,00 €** | **+125,0 %** | -20,00 € |
| **C — 10 € maximum** | 252 / 302 | 2515 € | **-97,95 €** | **-3,9 %** | -337,50 € |
| **D — cote 1,60–3,50** | 178 / 212 | 1780 € | **-23,00 €** | **-1,3 %** | -238,00 € |
| **E — dans les 48 h** | 252 / 259 | 2515 € | **-97,95 €** | **-3,9 %** | -337,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 222 / 232 | 2215 € | **-133,95 €** | **-6,0 %** | -301,00 € |
| **I — cotes modérées, un boost/match** | 153 / 161 | 1530 € | **-109,00 €** | **-7,1 %** | -244,00 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 2 / 2 | 30 € | **-30,00 €** | **-100,0 %** | -30,00 € |
| **J — filtre quotidien choisi avec les résultats passés** | 43 / 44 | 414 € | **+29,68 €** | **+7,2 %** | -122,83 € |
| **K — modèle progressif, 10 € maximum** | 56 / 57 | 545 € | **+150,73 €** | **+27,7 %** | -74,75 € |
| **L — modèle et Kelly amorti sur bankroll** | 59 / 60 | 369 € | **+76,74 €** | **+20,8 %** | -59,37 € |
| **M — modèle progressif, 20 € maximum** | 40 / 41 | 759 € | **+409,38 €** | **+54,0 %** | -85,88 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.
J/K/L/M utilisent un replay chronologique après 30 règlements d'apprentissage, avec une bankroll et des mises immobilisées. Leur période diffère de A–I. Leur modèle utilise des probabilités estimées ; le rapport RECHERCHE.md présente les témoins comparables et la recherche complète, y compris les variantes perdantes.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 79 gagnés, 169 perdus, 4 remboursés, 50 en attente · cote moyenne 3,36 · pire série perdante 22

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 4 / 4 | 85 € | +51,25 € | +60,3 % | 50 % |
| EV 0 à 5 % (exacte) | 1 / 1 | 10 € | -10,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 3 / 3 | 60 € | +10,00 € | +16,7 % | 33 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 38 / 40 | 762 € | -346,70 € | -45,5 % | 21 % |
| EV < 0 (exacte) | 35 / 36 | 700 € | +204,50 € | +29,2 % | 38 % |
| non évaluable | 168 / 215 | 3499 € | -236,97 € | -6,8 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 5 / 9 | 100 € | +66,00 € | +66,0 % | 60 % |
| Genybet | 2 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| NetBet | 2 / 2 | 20 € | +7,50 € | +37,5 % | 50 % |
| OlyBet | 5 / 9 | 61 € | +92,58 € | +152,0 % | 80 % |
| Unibet | 43 / 81 | 1075 € | -25,00 € | -2,3 % | 38 % |
| Winamax | 195 / 199 | 3900 € | -354,00 € | -9,1 % | 29 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 39 | 0 € | +0,00 € | – | – |
| match | 252 / 263 | 5176 € | -232,92 € | -4,5 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 4 / 7 | 40 € | -12,50 € | -31,2 % | 25 % |
| 11.11 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 11.62 € | 1 / 1 | 12 € | +29,05 € | +250,0 % | 100 % |
| 13.88 € | 1 / 1 | 14 € | +24,98 € | +180,0 % | 100 % |
| 20 € | 200 / 208 | 4000 € | -288,00 € | -7,2 % | 29 % |
| 20.83 € | 1 / 1 | 21 € | +25,00 € | +120,0 % | 100 % |
| 25 € | 43 / 81 | 1075 € | -25,00 € | -2,3 % | 38 % |
| 6.25 € | 1 / 1 | 6 € | +21,88 € | +350,1 % | 100 % |
| 8.33 € | 1 / 1 | 8 € | -8,33 € | -100,0 % | 0 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 2 / 5 | 40 € | -40,00 € | -100,0 % | 0 % |
| 2 – 3 | 102 / 121 | 2190 € | +181,23 € | +8,3 % | 43 % |
| 3 – 5 | 135 / 149 | 2706 € | -434,15 € | -16,0 % | 25 % |
| 5 – 10 | 11 / 17 | 220 € | +80,00 € | +36,4 % | 27 % |
| < 2 | 2 / 10 | 20 € | -20,00 € | -100,0 % | 0 % |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Baseball | 7 / 8 | 140 € | -92,00 € | -65,7 % | 14 % |
| Basketball | 11 / 40 | 220 € | -158,00 € | -71,8 % | 10 % |
| Football | 138 / 155 | 2816 € | -125,67 € | -4,5 % | 32 % |
| Football Américain | 6 / 6 | 120 € | -120,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 3 / 3 | 60 € | -14,00 € | -23,3 % | 33 % |
| Hockey sur glace | 27 / 28 | 540 € | -179,00 € | -33,1 % | 22 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 4 / 4 | 100 € | -37,50 € | -37,5 % | 25 % |
| Rugby à XIII | 3 / 3 | 70 € | -15,00 € | -21,4 % | 33 % |
| Rugby à XV | 7 / 8 | 140 € | +72,00 € | +51,4 % | 57 % |
| Tennis | 35 / 36 | 745 € | +566,25 € | +76,0 % | 58 % |
| Tennis de table | 4 / 4 | 80 € | +15,00 € | +18,8 % | 25 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 252 / 302 | 5176 € | -232,92 € | -4,5 % | 32 % |

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
| 17/10 18h30 · Nottingham Forest - Arsenal | Arsenal marque au moins 3 buts | 3,5 | 3,861 | -9,4 % | 10 € | ⏳ |
| 17/10 18h30 · Bayern Munich - Leipzig | Le Bayern gagne 3-0 | 12,5 | – | – | 20 € | ⏳ |
| 17/10 17h15 · Strasbourg - Paris SG | Paris SG gagne par au moins 3 buts | 3,25 | – | – | 11.11 € | ⏳ |
| 17/10 17h15 · Strasbourg - Paris SG | Kvara Buteur! | 2,3 | – | – | 20 € | ⏳ |
| 17/10 13h22 · Manchester City - Ipswitch | Manchester City gagne et E. Haaland marque 2 buts ou plus | 3,5 | – | – | 10 € | ⏳ |
| 17/10 07h00 · Australie - Nouvelle Zélande | Nouvelle Zélande gagne et plus de 59,5 points dans le match | 2,6 | – | – | 20 € | ⏳ |
| 17/10 04h00 · Anaheim Ducks - Boston Bruins | Anaheim Ducks gagne et plus de 5,5 buts dans le match (hors prol. et TAB) | 4,0 | – | – | 20 € | ⏳ |
| 17/10 03h00 · Colorado Avalanche - Pittsburgh Penguins | Nathan MacKinnon buteur et Colorado Avalanche gagne (hors prol. et TAB) | 2,6 | 3,832 | -32,1 % ≈ | 20 € | ✅ +32,00 € |
| 17/10 02h30 · Boca Juniors - Talleres | Boca Juniors gagne le match 1-0, 2-0 ou 3-0 | 2,7 | – | – | 20 € | ❌ -20,00 € |
| 17/10 02h00 · Cleveland Guardians - Tampa Bay Rays | Les deux équipes marquent chacune au moins 3 runs | 2,75 | 2,821 | -2,5 % ≈ | 20 € | ⏳ |
| 16/10 21h00 · Gloucester - Bordeaux | Bordeaux gagne et Tom Willis marque au moins 1 essai ? | 3,0 | – | – | 25 € | ❌ -25,00 € |

≈ : calcul approché (conditions liées sur un même match).
