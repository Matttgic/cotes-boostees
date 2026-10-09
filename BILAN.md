# Bilan des cotes boostées (stratégies et risques)

Mis à jour le 09/10 22h09 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 21 / 59 | 425 € | **+164,50 €** | **+38,7 %** | -60,00 € |
| **B-exacte (EV ≥ 5 %)** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **B-approx (EV ≥ 5 %)** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **C — 10 € maximum** | 21 / 59 | 210 € | **+79,00 €** | **+37,6 %** | -30,00 € |
| **D — cote 1,60–3,50** | 17 / 39 | 170 € | **+35,50 €** | **+20,9 %** | -30,00 € |
| **E — dans les 48 h** | 21 / 38 | 210 € | **+79,00 €** | **+37,6 %** | -30,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 20 / 36 | 200 € | **+89,00 €** | **+44,5 %** | -30,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 10 gagnés, 11 perdus, 0 remboursés, 38 en attente · cote moyenne 3,15 · pire série perdante 3

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV < 0 (approx) | 3 / 4 | 60 € | +48,00 € | +80,0 % | 67 % |
| EV < 0 (exacte) | 3 / 4 | 60 € | +46,00 € | +76,7 % | 67 % |
| non évaluable | 15 / 51 | 305 € | +70,50 € | +23,1 % | 40 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 1 / 24 | 25 € | +32,50 € | +130,0 % | 100 % |
| Winamax | 20 / 35 | 400 € | +132,00 € | +33,0 % | 45 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 21 | 0 € | +0,00 € | – | – |
| match | 21 / 38 | 425 € | +164,50 € | +38,7 % | 48 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 20 / 35 | 400 € | +132,00 € | +33,0 % | 45 % |
| 25 € | 1 / 24 | 25 € | +32,50 € | +130,0 % | 100 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 13 / 24 | 265 € | +37,50 € | +14,2 % | 46 % |
| 3 – 5 | 8 / 22 | 160 € | +127,00 € | +79,4 % | 50 % |
| 5 – 10 | 0 / 4 | 0 € | +0,00 € | – | – |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 1 / 1 | 20 € | +28,00 € | +140,0 % | 100 % |
| Basketball | 1 / 24 | 20 € | -20,00 € | -100,0 % | 0 % |
| Football | 4 / 15 | 80 € | +50,00 € | +62,5 % | 50 % |
| Football Américain | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 2 / 4 | 40 € | +20,00 € | +50,0 % | 50 % |
| Judo | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| Rugby à XV | 1 / 2 | 20 € | +25,00 € | +125,0 % | 100 % |
| Tennis | 6 / 6 | 125 € | +86,50 € | +69,2 % | 67 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 21 / 59 | 425 € | +164,50 € | +38,7 % | 48 % |

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
| 10/10 09h30 · Ch. du Monde +78 kg (F) | Léa Fontaine remporte la médaille d'or | 5,0 | – | – | 20 € | ⏳ |
| 10/10 03h30 · Las Vegas Aces - Golden State Valkyries | A'ja Wilson marque au moins 30 points et Las Vegas Aces gagne | 3,0 | – | – | 20 € | ⏳ |
| 10/10 03h00 · Puebla - Leon | Leon marque dans les deux mi-temps | 3,75 | – | – | 20 € | ⏳ |
| 10/10 02h45 · Union De Santa Fe - Defensa Y Justicia | Union De Santa Fe gagne à la mi-temps et à la fin du match | 3,75 | 7,172 | -47,7 % ≈ | 20 € | ⏳ |
| 10/10 01h30 · WNBA | Plus de 164,5 points lors de chacun des matchs suivants : New York Liberty - Atlanta Dream et Las Vegas Aces - Golden State Valkyries | 4,0 | – | – | 20 € | ⏳ |
| 10/10 01h15 · NHL | Plus de 5,5 buts lors de chacun des matchs suivants : Washington Capitals - New York Rangers et Detroit Red Wings - Seattle Kraken | 3,0 | 3,44 | -12,8 % | 20 € | ⏳ |
| 09/10 21h15 · Braga - Sporting Portugal | Braga ou Sporting Portugal gagne et les deux équipes marquent | 3,0 | – | – | 20 € | ⏳ |
| 09/10 21h00 · Malaga - Espanyol Barcelone | Malaga gagne ou fait match nul et les deux équipes marquent | 2,6 | – | – | 20 € | ⏳ |
| 09/10 20h45 · Lens - Lyon | Le duo F.Thauvin / L.Openda cumule plus de 1,5 buts et/ou passes décisives (remboursé si non titulaires) | 2,3 | – | – | 25 € | ⏳ |
| 09/10 20h45 · Lens - Lyon | Le duo F.Thauvin / L.Openda cumule plus de 1,5 buts et passes décisives (remboursé si non titulaires) | 2,3 | – | – | 25 € | ⏳ |
| 09/10 20h30 · Borussia Dortmund - Werder Brême | Serhou Guirassy marque au moins un but en 1ère mi-temps | 2,85 | – | – | 20 € | ⏳ |
| 09/10 20h00 · Ligue 2 - 09/10 | Plus de 1,5 buts dans chacun des 5 matchs de 20:00 | 3,65 | – | – | 25 € | ⏳ |
| 09/10 20h00 · Al Nassr - Diriyah Club | Cristiano Ronaldo marque 2 buts ou plus | 4,0 | – | – | 20 € | ⏳ |
| 09/10 20h00 · Synerglace Ligue Magnus | Plus de 4,5 buts dans chacun des 5 matchs du jour | 4,0 | – | – | 20 € | ⏳ |
| 09/10 20h00 · Ligue 2 BKT® | Plus de 1,5 buts dans chacun des 5 matchs du jour | 3,75 | – | – | 20 € | ⏳ |
| 09/10 19h30 · Pro D2 | Agen, Oyonnax et Stade Niçois gagnent chacun leur match (respectivement contre Dax, Narbonne et Nevers) | 2,6 | – | – | 20 € | ⏳ |
| 09/10 19h00 · NBA 2026 - 2027 | New York Knicks gagne le titre NBA | 11,0 | – | – | 20 € | ⏳ |
| 09/10 19h00 · Galatasaray - Kasimpasa | Galatasaray gagne les deux mi-temps | 2,6 | – | – | 20 € | ⏳ |
| 09/10 16h10 · Ch. du Monde -78 kg (F) | Kaïla Issoufi remporte la médaille d'or | 2,75 | – | – | 20 € | ❌ -20,00 € |
| 09/10 13h35 · Chine Super League | Plus de 2,5 buts dans chacun des 3 matchs à partir de 13h35 | 2,9 | – | – | 20 € | ✅ +38,00 € |

≈ : calcul approché (conditions liées sur un même match).
