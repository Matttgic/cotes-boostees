# Bilan des cotes boostées (stratégies et risques)

Mis à jour le 10/10 18h39 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 42 / 93 | 865 € | **+118,00 €** | **+13,6 %** | -205,00 € |
| **B-exacte (EV ≥ 5 %)** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **B-approx (EV ≥ 5 %)** | 0 / 2 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **C — 10 € maximum** | 42 / 93 | 420 € | **+48,00 €** | **+11,4 %** | -100,00 € |
| **D — cote 1,60–3,50** | 29 / 63 | 290 € | **+94,50 €** | **+32,6 %** | -40,00 € |
| **E — dans les 48 h** | 42 / 68 | 420 € | **+48,00 €** | **+11,4 %** | -100,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 40 / 63 | 400 € | **+45,00 €** | **+11,2 %** | -100,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 17 gagnés, 25 perdus, 0 remboursés, 51 en attente · cote moyenne 3,16 · pire série perdante 10

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 0 / 1 | 0 € | +0,00 € | – | – |
| EV 10 % et + (approx) | 0 / 1 | 0 € | +0,00 € | – | – |
| EV 5 à 10 % (approx) | 0 / 1 | 0 € | +0,00 € | – | – |
| EV < 0 (approx) | 5 / 6 | 100 € | +8,00 € | +8,0 % | 40 % |
| EV < 0 (exacte) | 4 / 7 | 80 € | +26,00 € | +32,5 % | 50 % |
| non évaluable | 33 / 77 | 685 € | +84,00 € | +12,3 % | 39 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 5 / 34 | 125 € | +110,00 € | +88,0 % | 80 % |
| Winamax | 37 / 59 | 740 € | +8,00 € | +1,1 % | 35 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 25 | 0 € | +0,00 € | – | – |
| match | 42 / 68 | 865 € | +118,00 € | +13,6 % | 40 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 37 / 59 | 740 € | +8,00 € | +1,1 % | 35 % |
| 25 € | 5 / 34 | 125 € | +110,00 € | +88,0 % | 80 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 21 / 40 | 445 € | +191,00 € | +42,9 % | 57 % |
| 3 – 5 | 20 / 38 | 400 € | -53,00 € | -13,2 % | 25 % |
| 5 – 10 | 1 / 6 | 20 € | -20,00 € | -100,0 % | 0 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 1 / 1 | 20 € | +28,00 € | +140,0 % | 100 % |
| Basketball | 4 / 27 | 80 € | -80,00 € | -100,0 % | 0 % |
| Football | 16 / 38 | 330 € | +79,00 € | +23,9 % | 44 % |
| Football Américain | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Formule 1 | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 4 / 5 | 80 € | -20,00 € | -25,0 % | 25 % |
| Judo | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby | 1 / 2 | 25 € | +37,50 € | +150,0 % | 100 % |
| Rugby à XV | 2 / 4 | 40 € | +57,00 € | +142,5 % | 100 % |
| Tennis | 7 / 8 | 150 € | +61,50 € | +41,0 % | 57 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 42 / 93 | 865 € | +118,00 € | +13,6 % | 40 % |

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
| 10/10 18h30 · Man. United - Tottenham | B.Fernandes décisif et son équipe gagne (remboursé si non titulaire) | 2,3 | – | – | 25 € | ⏳ |
| 10/10 18h30 · Manchester United - Tottenham | Manchester United gagne et plus de 3,5 buts dans le match | 3,6 | 4,268 | -15,7 % ≈ | 20 € | ⏳ |
| 10/10 18h30 · FC Barcelone - Getafe | Lamine Yamal premier buteur du match | 4,0 | – | – | 20 € | ⏳ |
| 10/10 18h00 · 1re division professionnelle | Plus de 159,5 points lors de chacun des matchs suivants : Cholet - Pau-Lacq-Orthez et Chalon-sur-Saône - Nancy | 2,1 | – | – | 20 € | ⏳ |
| 10/10 18h00 · Inter Milan - Parme | Inter Milan gagne et les deux équipes marquent | 2,8 | 2,673 | +4,7 % ≈ | 20 € | ⏳ |
| 10/10 17h15 · Ligue 1 McDonald's® | Plus de 1,5 buts dans chacun des 5 matchs du jour | 2,4 | – | – | 20 € | ⏳ |
| 10/10 16h35 · Top 14 | Chaque équipe à domicile gagne (4 matchs à 16h35) | 2,3 | – | – | 20 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
