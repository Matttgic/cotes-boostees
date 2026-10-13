# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (47 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 22 / 47 | 455 € | **+63,50 €** | **+14,0 %** | -16,7 % (15 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 15 / 31 | 150 € | **+13,00 €** | **+8,7 %** | -20,7 % (10 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Hypothèse I — essai prospectif

Règle figée le 13/10 22h20 ; comparaison A/I sur les boosts découverts depuis (6 pour l'instant).

| Stratégie | Paris réglés | Misé | Gain net | ROI |
|---|---|---|---|---|
| **A — tout miser** | 0 / 6 | 0 € | +0,00 € | – |
| **I — cotes modérées, un boost/match** | 0 / 5 | 0 € | +0,00 € | – |
Le bouton I conserve aussi l'exploration historique complète ; ces chiffres ne valident pas la stratégie.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 13/10 23h19 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres historiques. I combine D et H après lecture de l'historique ; son test prospectif séparé commence à la date documentée. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 129 / 188 | 2680 € | **-51,00 €** | **-1,9 %** | -471,00 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 4 / 4 | 80 € | **+145,00 €** | **+181,2 %** | -20,00 € |
| **C — 10 € maximum** | 129 / 188 | 1290 € | **-24,50 €** | **-1,9 %** | -226,00 € |
| **D — cote 1,60–3,50** | 90 / 127 | 900 € | **+1,50 €** | **+0,2 %** | -148,50 € |
| **E — dans les 48 h** | 129 / 156 | 1290 € | **-24,50 €** | **-1,9 %** | -226,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 121 / 147 | 1210 € | **-1,00 €** | **-0,1 %** | -199,50 € |
| **I — cotes modérées, un boost/match** | 84 / 99 | 840 € | **+5,00 €** | **+0,6 %** | -142,00 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match ; I combine D et H. I a été choisie après lecture des résultats historiques : son score passé est rétrospectif et ne valide pas la règle. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 42 gagnés, 87 perdus, 0 remboursés, 59 en attente · cote moyenne 3,4 · pire série perdante 9

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 2 / 2 | 40 € | +30,00 € | +75,0 % | 50 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 20 / 21 | 400 € | -182,00 € | -45,5 % | 20 % |
| EV < 0 (exacte) | 16 / 19 | 325 € | +191,50 € | +58,9 % | 50 % |
| non évaluable | 87 / 141 | 1835 € | -165,50 € | -9,0 % | 31 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Betsson | 0 / 4 | 0 € | +0,00 € | – | – |
| OlyBet | 0 / 3 | 0 € | +0,00 € | – | – |
| Unibet | 20 / 53 | 500 € | -10,00 € | -2,0 % | 40 % |
| Winamax | 109 / 128 | 2180 € | -41,00 € | -1,9 % | 31 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 32 | 0 € | +0,00 € | – | – |
| match | 129 / 156 | 2680 € | -51,00 € | -1,9 % | 33 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 20 € | 109 / 132 | 2180 € | -41,00 € | -1,9 % | 31 % |
| 25 € | 20 / 53 | 500 € | -10,00 € | -2,0 % | 40 % |
| 7.14 € | 0 / 1 | 0 € | +0,00 € | – | – |
| 8.33 € | 0 / 1 | 0 € | +0,00 € | – | – |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 4 | 0 € | +0,00 € | – | – |
| 2 – 3 | 51 / 70 | 1100 € | +89,00 € | +8,1 % | 43 % |
| 3 – 5 | 71 / 95 | 1440 € | -100,00 € | -6,9 % | 27 % |
| 5 – 10 | 7 / 11 | 140 € | -40,00 € | -28,6 % | 14 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Badminton | 0 / 1 | 0 € | +0,00 € | – | – |
| Baseball | 3 / 4 | 60 € | -12,00 € | -20,0 % | 33 % |
| Basketball | 6 / 33 | 120 € | -78,00 € | -65,0 % | 17 % |
| Football | 66 / 93 | 1375 € | +2,00 € | +0,1 % | 32 % |
| Football Américain | 5 / 5 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 13 / 14 | 260 € | -135,00 € | -51,9 % | 15 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 20 / 22 | 425 € | +307,50 € | +72,4 % | 60 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 129 / 188 | 2680 € | -51,00 € | -1,9 % | 33 % |

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
| 20/10 19h00 · Paris Trashtalk 26/27 | MIA Heat - Le Heat remporte la Division Sud-Est | 3,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CLE Cavaliers - Les Cavaliers remportent la Division Centrale | 3,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | SAC Kings - Maxime Raynaud meilleur rebondeur des Kings (total de rebonds) | 2,5 | – | – | 25 € | ⏳ |
| 15/10 18h45 · CSKA Sofia - Monaco | Monaco gagne 3-0 | 10,5 | – | – | 20 € | ⏳ |
| 15/10 18h45 · Lyon - Crystal Palace | Pavel Sulc Décisif | 2,15 | – | – | 20 € | ⏳ |
| 14/10 21h00 · Manchester City - Paris SG | Le PSG gagne 1-0 | 15,0 | – | – | 20 € | ⏳ |
| 14/10 20h45 · Manchester City - Paris SG | Paris SG gagne et les 2 équipes marquent | 4,5 | – | – | 7.14 € | ⏳ |
| 14/10 20h45 · AS Rome - Real Madrid | Real Madrid to win and Vinicius to score | 4,0 | – | – | 8.33 € | ⏳ |
| 14/10 18h45 · LASK Linz - Liverpool | Barcola Buteur | 2,65 | – | – | 20 € | ⏳ |
| 14/10 07h15 · C. Ruud - F. Auger-Aliassime | Auger-Aliassime gagne et plus de 20,5 aces dans le match | 3,5 | – | – | 10 € | ⏳ |
| 14/10 05h00 · WTA Wuhan | Iga Swiatek, Iva Jovic et Karolina Muchova gagnent chacun leur match 2-0 (respectivement contre Magdalena Frech, Dayana Yastremska et Caty McNally) | 3,75 | 4,462 | -16,0 % | 20 € | ⏳ |
| 14/10 02h45 · NHL | Plus de 5,5 buts lors de chacun des matchs suivants : Nashville Predators - Vegas Golden Knights et Utah Mammoth - Toronto Maple Leafs | 2,5 | 2,776 | -9,9 % | 20 € | ⏳ |
| 14/10 02h30 · Boca Juniors - Vasco da Gama | Boca Juniors gagne le match 1-0, 2-0 ou 3-0 | 2,8 | – | – | 20 € | ⏳ |
| 14/10 02h00 · Tampa Bay Rays - Cleveland Guardians | Tampa Bay Rays réalise au moins 5 runs | 2,8 | 2,995 | -6,5 % | 20 € | ⏳ |
| 14/10 01h30 · Bucaramanga - Aguilas Doradas | Bucaramanga gagne à la mi-temps et à la fin du match | 3,25 | – | – | 20 € | ⏳ |
| 14/10 00h40 · Montreal Canadiens - Buffalo Sabres | Cole Caufield buteur et Montreal Canadiens gagne (hors prol. et TAB) | 3,25 | – | – | 20 € | ⏳ |
| 13/10 21h00 · CB - ChampionsLeague (13/10) | Au moins 5 équipes marquent chacune 3 buts ou plus lors des 7 matchs de 21h ? | 2,5 | – | – | 25 € | ⏳ |
| 13/10 21h00 · CB - ChampionsLeague (13/10) | Au moins 2 joueurs marquent dans le Trio M.Olise/M.Thuram/C.Nkunku ? (Remboursé si non titulaire(s)) | 2,3 | – | – | 25 € | ⏳ |
| 13/10 21h00 · Atl. Madrid - Man. United | Le Duo J.Alvarez+B.Fernandes sera décisif au moins 2 fois en cumulé ? (Remboursé si non titulaire(s)) | 2,3 | – | – | 25 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
