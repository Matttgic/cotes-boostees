# Bilan des cotes boostées (stratégies et risques)

Mis à jour le 10/10 01h06 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 30 / 60 | 615 € | **+245,50 €** | **+39,9 %** | -80,00 € |
| **B-exacte (EV ≥ 5 %)** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **B-approx (EV ≥ 5 %)** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **C — 10 € maximum** | 30 / 60 | 300 € | **+113,00 €** | **+37,7 %** | -40,00 € |
| **D — cote 1,60–3,50** | 23 / 40 | 230 € | **+99,50 €** | **+43,3 %** | -30,00 € |
| **E — dans les 48 h** | 30 / 39 | 300 € | **+113,00 €** | **+37,7 %** | -40,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 28 / 37 | 280 € | **+110,00 €** | **+39,3 %** | -40,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 15 gagnés, 15 perdus, 0 remboursés, 30 en attente · cote moyenne 3,14 · pire série perdante 4

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV < 0 (approx) | 3 / 4 | 60 € | +48,00 € | +80,0 % | 67 % |
| EV < 0 (exacte) | 3 / 4 | 60 € | +46,00 € | +76,7 % | 67 % |
| non évaluable | 24 / 52 | 495 € | +151,50 € | +30,6 % | 46 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 3 / 25 | 75 € | +97,50 € | +130,0 % | 100 % |
| Winamax | 27 / 35 | 540 € | +148,00 € | +27,4 % | 44 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 21 | 0 € | +0,00 € | – | – |
| match | 30 / 39 | 615 € | +245,50 € | +39,9 % | 50 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 27 / 35 | 540 € | +148,00 € | +27,4 % | 44 % |
| 25 € | 3 / 25 | 75 € | +97,50 € | +130,0 % | 100 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 19 / 25 | 395 € | +178,50 € | +45,2 % | 58 % |
| 3 – 5 | 11 / 22 | 220 € | +67,00 € | +30,5 % | 36 % |
| 5 – 10 | 0 / 4 | 0 € | +0,00 € | – | – |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 1 / 1 | 20 € | +28,00 € | +140,0 % | 100 % |
| Basketball | 1 / 24 | 20 € | -20,00 € | -100,0 % | 0 % |
| Football | 11 / 15 | 230 € | +119,00 € | +51,7 % | 54 % |
| Football Américain | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 3 / 4 | 60 € | +0,00 € | +0,0 % | 33 % |
| Judo | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby à XV | 2 / 2 | 40 € | +57,00 € | +142,5 % | 100 % |
| Tennis | 6 / 7 | 125 € | +86,50 € | +69,2 % | 67 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 30 / 60 | 615 € | +245,50 € | +39,9 % | 50 % |

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
| 10/10 13h00 · S.Baez - V.Vacherot | V.Vacherot gagne le 1er set et moins de 9,5 jeux dans le set ? | 2,5 | – | – | 25 € | ⏳ |
| 10/10 09h30 · Ch. du Monde +78 kg (F) | Léa Fontaine remporte la médaille d'or | 5,0 | – | – | 20 € | ⏳ |
| 10/10 03h30 · Las Vegas Aces - Golden State Valkyries | A'ja Wilson marque au moins 30 points et Las Vegas Aces gagne | 3,0 | – | – | 20 € | ⏳ |
| 10/10 03h00 · Puebla - Leon | Leon marque dans les deux mi-temps | 3,75 | – | – | 20 € | ⏳ |
| 10/10 02h45 · Union De Santa Fe - Defensa Y Justicia | Union De Santa Fe gagne à la mi-temps et à la fin du match | 3,75 | 7,172 | -47,7 % ≈ | 20 € | ⏳ |
| 10/10 01h30 · WNBA | Plus de 164,5 points lors de chacun des matchs suivants : New York Liberty - Atlanta Dream et Las Vegas Aces - Golden State Valkyries | 4,0 | – | – | 20 € | ⏳ |
| 10/10 01h15 · NHL | Plus de 5,5 buts lors de chacun des matchs suivants : Washington Capitals - New York Rangers et Detroit Red Wings - Seattle Kraken | 3,0 | 3,44 | -12,8 % | 20 € | ⏳ |
| 09/10 21h15 · Braga - Sporting Portugal | Braga ou Sporting Portugal gagne et les deux équipes marquent | 3,0 | – | – | 20 € | ⏳ |
| 09/10 21h00 · Malaga - Espanyol Barcelone | Malaga gagne ou fait match nul et les deux équipes marquent | 2,6 | – | – | 20 € | ✅ +32,00 € |
| 09/10 20h45 · Lens - Lyon | Le duo F.Thauvin / L.Openda cumule plus de 1,5 buts et/ou passes décisives (remboursé si non titulaires) | 2,3 | – | – | 25 € | ✅ +32,50 € |
| 09/10 20h45 · Lens - Lyon | Le duo F.Thauvin / L.Openda cumule plus de 1,5 buts et passes décisives (remboursé si non titulaires) | 2,3 | – | – | 25 € | ✅ +32,50 € |
| 09/10 20h30 · Borussia Dortmund - Werder Brême | Serhou Guirassy marque au moins un but en 1ère mi-temps | 2,85 | – | – | 20 € | ❌ -20,00 € |
| 09/10 20h00 · Ligue 2 - 09/10 | Plus de 1,5 buts dans chacun des 5 matchs de 20:00 | 3,65 | – | – | 25 € | ⏳ |
| 09/10 20h00 · Al Nassr - Diriyah Club | Cristiano Ronaldo marque 2 buts ou plus | 4,0 | – | – | 20 € | ❌ -20,00 € |
| 09/10 20h00 · Synerglace Ligue Magnus | Plus de 4,5 buts dans chacun des 5 matchs du jour | 4,0 | – | – | 20 € | ❌ -20,00 € |
| 09/10 20h00 · Ligue 2 BKT® | Plus de 1,5 buts dans chacun des 5 matchs du jour | 3,75 | – | – | 20 € | ❌ -20,00 € |
| 09/10 19h30 · Pro D2 | Agen, Oyonnax et Stade Niçois gagnent chacun leur match (respectivement contre Dax, Narbonne et Nevers) | 2,6 | – | – | 20 € | ✅ +32,00 € |
| 09/10 19h00 · NBA 2026 - 2027 | New York Knicks gagne le titre NBA | 11,0 | – | – | 20 € | ⏳ |
| 09/10 19h00 · Galatasaray - Kasimpasa | Galatasaray gagne les deux mi-temps | 2,6 | – | – | 20 € | ✅ +32,00 € |
| 09/10 16h10 · Ch. du Monde -78 kg (F) | Kaïla Issoufi remporte la médaille d'or | 2,75 | – | – | 20 € | ❌ -20,00 € |

≈ : calcul approché (conditions liées sur un même match).
