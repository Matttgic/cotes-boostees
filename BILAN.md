# Bilan des cotes boostées (stratégies et risques)

Mis à jour le 10/10 21h52 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 49 / 100 | 1005 € | **+108,00 €** | **+10,7 %** | -212,50 € |
| **B-exacte (EV ≥ 5 %)** | 0 / 1 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **B-approx (EV ≥ 5 %)** | 1 / 2 | 20 € | **+55,00 €** | **+275,0 %** | +0,00 € |
| **C — 10 € maximum** | 49 / 100 | 490 € | **+43,00 €** | **+8,8 %** | -107,50 € |
| **D — cote 1,60–3,50** | 33 / 66 | 330 € | **+82,00 €** | **+24,8 %** | -37,50 € |
| **E — dans les 48 h** | 49 / 75 | 490 € | **+43,00 €** | **+8,8 %** | -107,50 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 47 / 70 | 470 € | **+40,00 €** | **+8,5 %** | -107,50 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 19 gagnés, 30 perdus, 0 remboursés, 51 en attente · cote moyenne 3,23 · pire série perdante 6

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 0 / 1 | 0 € | +0,00 € | – | – |
| EV 10 % et + (approx) | 0 / 1 | 0 € | +0,00 € | – | – |
| EV 10 % et + (exacte) | 0 / 1 | 0 € | +0,00 € | – | – |
| EV 5 à 10 % (approx) | 1 / 1 | 20 € | +55,00 € | +275,0 % | 100 % |
| EV < 0 (approx) | 5 / 7 | 100 € | +8,00 € | +8,0 % | 40 % |
| EV < 0 (exacte) | 5 / 8 | 100 € | +6,00 € | +6,0 % | 40 % |
| non évaluable | 38 / 81 | 785 € | +39,00 € | +5,0 % | 37 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 5 / 34 | 125 € | +110,00 € | +88,0 % | 80 % |
| Winamax | 44 / 66 | 880 € | -2,00 € | -0,2 % | 34 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 25 | 0 € | +0,00 € | – | – |
| match | 49 / 75 | 1005 € | +108,00 € | +10,7 % | 39 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 44 / 66 | 880 € | -2,00 € | -0,2 % | 34 % |
| 25 € | 5 / 34 | 125 € | +110,00 € | +88,0 % | 80 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 24 / 41 | 505 € | +186,00 € | +36,8 % | 54 % |
| 3 – 5 | 23 / 42 | 460 € | -38,00 € | -8,3 % | 26 % |
| 5 – 10 | 2 / 8 | 40 € | -40,00 € | -100,0 % | 0 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 1 / 1 | 20 € | +28,00 € | +140,0 % | 100 % |
| Basketball | 4 / 27 | 80 € | -80,00 € | -100,0 % | 0 % |
| Football | 20 / 41 | 410 € | +74,00 € | +18,0 % | 40 % |
| Football Américain | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Formule 1 | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 4 / 7 | 80 € | -20,00 € | -25,0 % | 25 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 1 / 2 | 25 € | +37,50 € | +150,0 % | 100 % |
| Rugby à XV | 3 / 4 | 60 € | +37,00 € | +61,7 % | 67 % |
| Tennis | 8 / 10 | 170 € | +96,50 € | +56,8 % | 62 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 49 / 100 | 1005 € | +108,00 € | +10,7 % | 39 % |

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
| 20/10 19h00 · Paris Trashtalk 26/27 | TOR Raptors - Scottie Barnes meilleur passeur des Raptors (total de passes) | 2,0 | – | – | 25 € | ⏳ |
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
| 11/10 13h30 · Qinwen Zheng - Mirra Andreeva | Mirra Andreeva gagne 2-1 | 4,25 | – | – | 20 € | ⏳ |
| 11/10 06h00 · Ben Shelton - Arthur Gea | Arthur Gea gagne 2-1 | 6,5 | – | – | 20 € | ⏳ |
| 11/10 04h15 · Vegas Golden Knights - Los Angeles Kings | Vegas Golden Knights marque au moins 5 buts (hors prol. et TAB) | 3,75 | 4,41 | -15,0 % | 20 € | ⏳ |
| 11/10 03h00 · Atlas - Guadalajara | Guadalajara marque dans les deux mi-temps | 3,1 | – | – | 20 € | ⏳ |
| 11/10 02h00 · Sao Paulo FC - Vitoria | Sao Paulo gagne à la mi-temps et à la fin du match | 2,55 | 3,997 | -36,2 % ≈ | 20 € | ⏳ |
| 11/10 01h30 · Inter Miami - DC United | L. Messi et L. Suarez marquent chacun au moins un but et Inter Miami gagne | 3,4 | – | – | 20 € | ⏳ |
| 11/10 01h10 · NHL | Nathan MacKinnon et Cole Caufield marquent chacun au moins un but (respectivement contre Toronto Maple Leafs et Detroit Red Wings) (avec Garantie Golden Goal) | 5,25 | 4,733 | +10,9 % | 20 € | ⏳ |
| 10/10 21h30 · NHL | Edmonton Oilers et New Jersey Devils gagnent chacun leur match (respectivement contre San Jose Sharks et Vancouver Canucks) (hors prol. et TAB) | 3,25 | 3,501 | -7,2 % | 20 € | ⏳ |
| 10/10 21h00 · Clermont - Bordeaux | Clermont gagne et le duo B.Delguy/B.Massa marque au moins 1 essai | 2,4 | – | – | 25 € | ⏳ |
| 10/10 21h00 · Real Madrid - Villarreal | K.Mbappé buteur, son équipe mène à la mi-temps et gagne le match ? (remboursé si non titulaire) | 2,35 | – | – | 25 € | ⏳ |
| 10/10 21h00 · ASM Clermont - Bordeaux-Bègles | L. Bielle-Biarrey et A. Raka marquent chacun au moins un essai | 5,0 | – | – | 20 € | ⏳ |
| 10/10 21h00 · Real Madrid - Villarreal | Kylian Mbappé marque 2 buts ou plus | 3,25 | – | – | 20 € | ⏳ |
| 10/10 20h45 · Paris SG - Le Mans | Paris SG gagne 1-0, 2-0 ou 3-0 | 3,3 | – | – | 25 € | ⏳ |
| 10/10 20h45 · Ligue 1 - 10/10 | Plus de 0,5 buts à la mi-temps de chacun des 4 matchs de 20h45 ? | 2,45 | – | – | 25 € | ⏳ |
| 10/10 20h45 · Naples - Frosinone | Kevin De Bruyne buteur et Naples gagne | 3,5 | – | – | 20 € | ⏳ |
| 10/10 20h45 · Paris SG - Le Mans | Paris SG gagne le match 4-0 ou 5-0 ou 6-0 | 4,5 | – | – | 20 € | ⏳ |
| 10/10 20h30 · Chicago Fire - New York City FC | Chicago Fire gagne et les deux équipes marquent | 3,5 | 3,103 | +12,8 % ≈ | 20 € | ⏳ |
| 10/10 20h00 · Saint-Etienne - Rodez | Saint-Etienne gagne par au moins 3 buts d'écart | 3,5 | 3,854 | -9,2 % | 20 € | ⏳ |
| 10/10 18h30 · FC Barcelone - Getafe | L.Yamal décisif au moins 2 fois ? (remboursé si non titulaire) | 2,6 | – | – | 25 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
