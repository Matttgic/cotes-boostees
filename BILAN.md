# Bilan des cotes boostées (stratégies et risques)

Mis à jour le 11/10 09h17 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 73 / 110 | 1510 € | **-2,00 €** | **-0,1 %** | -300,50 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 2 / 2 | 40 € | **+105,00 €** | **+262,5 %** | +0,00 € |
| **C — 10 € maximum** | 73 / 110 | 730 € | **+0,50 €** | **+0,1 %** | -139,00 € |
| **D — cote 1,60–3,50** | 50 / 76 | 500 € | **+69,50 €** | **+13,9 %** | -86,50 € |
| **E — dans les 48 h** | 73 / 84 | 730 € | **+0,50 €** | **+0,1 %** | -139,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 68 / 78 | 680 € | **+27,50 €** | **+4,0 %** | -119,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 25 gagnés, 48 perdus, 0 remboursés, 37 en attente · cote moyenne 3,19 · pire série perdante 6

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 1 / 1 | 20 € | +50,00 € | +250,0 % | 100 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 1 / 1 | 20 € | +55,00 € | +275,0 % | 100 % |
| EV < 0 (approx) | 7 / 8 | 140 € | -32,00 € | -22,9 % | 29 % |
| EV < 0 (exacte) | 8 / 9 | 160 € | +11,00 € | +6,9 % | 38 % |
| non évaluable | 54 / 89 | 1130 € | -46,00 € | -4,1 % | 33 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 10 / 40 | 250 € | -15,00 € | -6,0 % | 40 % |
| Winamax | 63 / 70 | 1260 € | +13,00 € | +1,0 % | 33 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 26 | 0 € | +0,00 € | – | – |
| match | 73 / 84 | 1510 € | -2,00 € | -0,1 % | 34 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 63 / 70 | 1260 € | +13,00 € | +1,0 % | 33 % |
| 25 € | 10 / 40 | 250 € | -15,00 € | -6,0 % | 40 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 33 / 46 | 705 € | +28,00 € | +4,0 % | 42 % |
| 3 – 5 | 36 / 47 | 725 € | +50,00 € | +6,9 % | 31 % |
| 5 – 10 | 4 / 8 | 80 € | -80,00 € | -100,0 % | 0 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 1 / 1 | 20 € | +28,00 € | +140,0 % | 100 % |
| Basketball | 5 / 27 | 100 € | -58,00 € | -58,0 % | 20 % |
| Football | 38 / 50 | 790 € | -18,00 € | -2,3 % | 32 % |
| Football Américain | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Formule 1 | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 7 / 7 | 140 € | -15,00 € | -10,7 % | 29 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 2 / 2 | 50 € | +12,50 € | +25,0 % | 50 % |
| Rugby à XV | 4 / 4 | 80 € | +17,00 € | +21,2 % | 50 % |
| Tennis | 8 / 11 | 170 € | +96,50 € | +56,8 % | 62 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 73 / 110 | 1510 € | -2,00 € | -0,1 % | 34 % |

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
| 11/10 20h45 · Top Football Européen (11/10) | Au moins 2 joueurs marquent dans le trio : A.Gouiri/R.Kolo Muani/H.Duro ? (Remboursé si non titulaire(s)) | 3,15 | – | – | 25 € | ⏳ |
| 11/10 20h45 · Troyes - Marseille | I.Paixao décisif et son équipe gagne (remboursé si non titulaire) | 2,65 | – | – | 25 € | ⏳ |
| 11/10 20h45 · Troyes - Marseille | Marseille gagne à la mi-temps et à la fin du match | 3,0 | 5,122 | -41,4 % ≈ | 20 € | ⏳ |
| 11/10 17h30 · Liverpool - Man. City | B.Barcola ou R.Cherki buteur(s) et les deux équipes marquent ? (Remboursé si non titulaire(s)) | 3,05 | – | – | 25 € | ⏳ |
| 11/10 17h30 · Liverpool - Manchester City | Liverpool ou Manchester City gagne et plus de 3,5 buts dans le match | 3,15 | – | – | 20 € | ⏳ |
| 11/10 17h15 · Rennes - Auxerre | E.Lepaul buteur, Rennes ouvre le score et gagne le match ? (Remboursé si non titulaire(s)) | 2,65 | – | – | 25 € | ⏳ |
| 11/10 15h00 · Nice - Strasbourg | Nice ou Strasbourg gagne par exactement 1 but d'écart ? | 2,55 | – | – | 25 € | ⏳ |
| 11/10 13h30 · 2. Bundesliga | Plus de 2,5 buts dans chacun des 3 matchs à 13h30 | 3,25 | – | – | 20 € | ⏳ |
| 11/10 13h30 · Qinwen Zheng - Mirra Andreeva | Mirra Andreeva gagne 2-1 | 4,25 | – | – | 20 € | ⏳ |
| 11/10 12h30 · Come - AS Rome | Plus de 1,5 buts lors de la première mi-temps du match | 2,4 | 2,634 | -8,9 % | 20 € | ⏳ |
| 11/10 12h00 · A.Zverev - Q.Halys | Q.Halys remporte au moins un set ? | 2,5 | – | – | 25 € | ⏳ |
| 11/10 06h00 · Ben Shelton - Arthur Gea | Arthur Gea gagne 2-1 | 6,5 | – | – | 20 € | ⏳ |
| 11/10 04h15 · Vegas Golden Knights - Los Angeles Kings | Vegas Golden Knights marque au moins 5 buts (hors prol. et TAB) | 3,75 | 4,41 | -15,0 % | 20 € | ❌ -20,00 € |
| 11/10 03h00 · Atlas - Guadalajara | Guadalajara marque dans les deux mi-temps | 3,1 | – | – | 20 € | ❌ -20,00 € |
| 11/10 02h00 · Sao Paulo FC - Vitoria | Sao Paulo gagne à la mi-temps et à la fin du match | 2,55 | 3,997 | -36,2 % ≈ | 20 € | ❌ -20,00 € |
| 11/10 01h30 · Inter Miami - DC United | L. Messi et L. Suarez marquent chacun au moins un but et Inter Miami gagne | 3,4 | – | – | 20 € | ✅ +48,00 € |
| 11/10 01h10 · NHL | Nathan MacKinnon et Cole Caufield marquent chacun au moins un but (respectivement contre Toronto Maple Leafs et Detroit Red Wings) (avec Garantie Golden Goal) | 5,25 | 4,733 | +10,9 % | 20 € | ❌ -20,00 € |
| 10/10 21h30 · NHL | Edmonton Oilers et New Jersey Devils gagnent chacun leur match (respectivement contre San Jose Sharks et Vancouver Canucks) (hors prol. et TAB) | 3,25 | 3,501 | -7,2 % | 20 € | ✅ +45,00 € |
| 10/10 21h00 · Clermont - Bordeaux | Clermont gagne et le duo B.Delguy/B.Massa marque au moins 1 essai | 2,4 | – | – | 25 € | ❌ -25,00 € |

≈ : calcul approché (conditions liées sur un même match).
