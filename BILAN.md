# Bilan des cotes boostées (stratégies et risques)

Mis à jour le 10/10 09h59 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 34 / 76 | 695 € | **+225,50 €** | **+32,4 %** | -80,00 € |
| **B-exacte (EV ≥ 5 %)** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **B-approx (EV ≥ 5 %)** | 0 / 1 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **C — 10 € maximum** | 34 / 76 | 340 € | **+103,00 €** | **+30,3 %** | -40,00 € |
| **D — cote 1,60–3,50** | 25 / 52 | 250 € | **+109,50 €** | **+43,8 %** | -30,00 € |
| **E — dans les 48 h** | 34 / 52 | 340 € | **+103,00 €** | **+30,3 %** | -40,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 32 / 49 | 320 € | **+100,00 €** | **+31,2 %** | -40,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 16 gagnés, 18 perdus, 0 remboursés, 42 en attente · cote moyenne 3,11 · pire série perdante 4

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 5 à 10 % (approx) | 0 / 1 | 0 € | +0,00 € | – | – |
| EV < 0 (approx) | 4 / 5 | 80 € | +28,00 € | +35,0 % | 50 % |
| EV < 0 (exacte) | 4 / 5 | 80 € | +26,00 € | +32,5 % | 50 % |
| non évaluable | 26 / 65 | 535 € | +171,50 € | +32,1 % | 46 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 3 / 33 | 75 € | +97,50 € | +130,0 % | 100 % |
| Winamax | 31 / 43 | 620 € | +128,00 € | +20,6 % | 42 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 24 | 0 € | +0,00 € | – | – |
| match | 34 / 52 | 695 € | +225,50 € | +32,4 % | 47 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 31 / 43 | 620 € | +128,00 € | +20,6 % | 42 % |
| 25 € | 3 / 33 | 75 € | +97,50 € | +130,0 % | 100 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 19 / 34 | 395 € | +178,50 € | +45,2 % | 58 % |
| 3 – 5 | 15 / 29 | 300 € | +47,00 € | +15,7 % | 33 % |
| 5 – 10 | 0 / 4 | 0 € | +0,00 € | – | – |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 1 / 1 | 20 € | +28,00 € | +140,0 % | 100 % |
| Basketball | 1 / 25 | 20 € | -20,00 € | -100,0 % | 0 % |
| Football | 14 / 26 | 290 € | +119,00 € | +41,0 % | 50 % |
| Football Américain | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Formule 1 | 0 / 1 | 0 € | +0,00 € | – | – |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 4 / 4 | 80 € | -20,00 € | -25,0 % | 25 % |
| Judo | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 0 / 2 | 0 € | +0,00 € | – | – |
| Rugby à XV | 2 / 2 | 40 € | +57,00 € | +142,5 % | 100 % |
| Tennis | 6 / 8 | 125 € | +86,50 € | +69,2 % | 67 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 34 / 76 | 695 € | +225,50 € | +32,4 % | 47 % |

### Derniers paris

| Match | Pari | Cote | Juste | EV | Mise | Résultat |
|---|---|---|---|---|---|---|
| 20/10 19h00 · Paris Trashtalk 26/27 | IND Pacers - Les Pacers remportent la Division Centrale | 4,25 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MEM Grizzlies - Cameron Boozer prend 8 rebonds ou + (moyenne) | 1,8 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | LA Clippers - Darius Garland fait 7 passes ou + (moyenne) | 1,6 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | HOU Rockets - Fred VanVleet fait 6 passes ou + (moyenne) | 2,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | POR TBlazers - Les Blazers ne se qualifient pas pour les Playoffs | 2,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | PHX Suns - Les Suns se qualifient pour les Playoffs | 1,66 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | GS Warriors - Les Warriors se qualifient pour les Playoffs | 1,58 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | DAL Mavericks - Les Mavericks se qualifient pour le PlayIn | 2,15 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | ATL Hawks - Dyson Daniels meilleur intercepteur NBA en saison régulière (moyenne interceptions/match, perdant si moins de 58 matchs joués) | 6,4 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | WAS Wizards - Trae Young meilleur passeur NBA en saison régulière (moyenne passes/match, perdant si moins de 58 matchs joués) | 3,3 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | BKN Nets - Mikel Brown Jr meilleur passeur des Nets (total de passes) | 3,3 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CHA Hornets - Moussa Diabate meilleur rebondeur des Hornets (total de rebonds) | 1,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | UTA Jazz - Darryn Peterson meilleur marqueur du Jazz (total de points) | 7,0 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | ORL Magic - Paolo Banchero meilleur marqueur du Magic (total de points) | 1,6 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | NO Pelicans - Zion Williamson meilleur marqueur des Pelicans (total de points) | 2,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | MIL Bucks - Tyler Herro meilleur marqueur des Bucks (total de points) | 1,35 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | LA Lakers - Luka Doncic meilleur marqueur NBA en saison régulière (moyenne points/match, perdant si moins de 58 matchs joués) | 1,87 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CHI Bulls - Caleb Wilson meilleur marqueur des Bulls (total de points) | 5,5 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | CLE Cavaliers - Les Cavaliers remportent la Division Centrale | 3,1 | – | – | 25 € | ⏳ |
| 20/10 19h00 · Paris Trashtalk 26/27 | SAC Kings - Maxime Raynaud meilleur rebondeur des Kings (total de rebonds) | 2,5 | – | – | 25 € | ⏳ |
| 10/10 21h00 · Clermont - Bordeaux | Clermont gagne et le duo B.Delguy/B.Massa marque au moins 1 essai | 2,4 | – | – | 25 € | ⏳ |
| 10/10 21h00 · Real Madrid - Villarreal | K.Mbappé buteur, son équipe mène à la mi-temps et gagne le match ? (remboursé si non titulaire) | 2,35 | – | – | 25 € | ⏳ |
| 10/10 20h45 · Paris SG - Le Mans | Paris SG gagne 1-0, 2-0 ou 3-0 | 3,3 | – | – | 25 € | ⏳ |
| 10/10 20h45 · Ligue 1 - 10/10 | Plus de 0,5 buts à la mi-temps de chacun des 4 matchs de 20h45 ? | 2,45 | – | – | 25 € | ⏳ |
| 10/10 18h30 · FC Barcelone - Getafe | L.Yamal décisif au moins 2 fois ? (remboursé si non titulaire) | 2,6 | – | – | 25 € | ⏳ |
| 10/10 18h30 · Man. United - Tottenham | B.Fernandes décisif et son équipe gagne (remboursé si non titulaire) | 2,3 | – | – | 25 € | ⏳ |
| 10/10 18h30 · FC Barcelone - Getafe | Lamine Yamal premier buteur du match | 4,0 | – | – | 20 € | ⏳ |
| 10/10 18h00 · Inter Milan - Parme | Inter Milan gagne et les deux équipes marquent | 2,8 | – | – | 20 € | ⏳ |
| 10/10 16h15 · Alaves - Atletico Madrid | Atletico Madrid gagne et les deux équipes marquent | 3,75 | 3,492 | +7,4 % ≈ | 20 € | ⏳ |
| 10/10 15h30 · Augsbourg - Bayern Munich | Bayern Munich marque plus de 4,5 buts lors du match | 3,15 | 3,748 | -16,0 % | 20 € | ⏳ |
| 10/10 14h30 · Stade Français - Montpellier | Le Stade Français gagne et le duo J.Ward/L.Barré marque au moins 1 essai | 2,5 | – | – | 25 € | ⏳ |
| 10/10 13h30 · Top Football Européen - 10/10 | Le trio V.Gyokeres / H.Kane / C.Palmer marque plus de 2,5 buts en cumulé ? (Remboursé si non titulaires) | 2,75 | – | – | 25 € | ⏳ |
| 10/10 13h30 · Arsenal - Leeds | Arsenal gagne et plus de 3,5 buts dans le match | 3,6 | 4,843 | -25,7 % ≈ | 20 € | ⏳ |
| 10/10 13h00 · S.Baez - V.Vacherot | V.Vacherot gagne le 1er set et moins de 9,5 jeux dans le set ? | 2,5 | – | – | 25 € | ⏳ |
| 10/10 11h00 · Grand Prix de Singapour - Sprint | George Russell remporte la course | 3,5 | – | – | 20 € | ⏳ |
| 10/10 10h30 · SE Melbourne Phoenix - Melbourne United | N. Sobey + C. Anthony marquent 55 points ou plus | 3,6 | – | – | 20 € | ⏳ |
| 10/10 09h30 · Ch. du Monde +78 kg (F) | Léa Fontaine remporte la médaille d'or | 5,0 | – | – | 20 € | ⏳ |
| 10/10 08h40 · ATP Shanghai | Arthur Fils et Learner Tien gagnent chacun leur match 2-0 (respectivement contre Pavel Kotov et Zachary Svajda) | 2,75 | – | – | 20 € | ⏳ |
| 10/10 03h30 · Las Vegas Aces - Golden State Valkyries | A'ja Wilson marque au moins 30 points et Las Vegas Aces gagne | 3,0 | – | – | 20 € | ⏳ |
| 10/10 03h00 · Puebla - Leon | Leon marque dans les deux mi-temps | 3,75 | – | – | 20 € | ❌ -20,00 € |

≈ : calcul approché (conditions liées sur un même match).
