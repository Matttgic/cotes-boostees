# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (15 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 2 / 15 | 40 € | **+60,00 €** | **+150,0 %** | -26,2 % (5 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 0 / 9 | 0 € | **+0,00 €** | **–** | -37,8 % (3 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 12/10 15h03 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 109 / 149 | 2265 € | **-54,50 €** | **-2,4 %** | -471,00 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 3 / 3 | 60 € | **+85,00 €** | **+141,7 %** | -20,00 € |
| **C — 10 € maximum** | 109 / 149 | 1090 € | **-27,50 €** | **-2,5 %** | -226,00 € |
| **D — cote 1,60–3,50** | 75 / 102 | 750 € | **-11,50 €** | **-1,5 %** | -131,00 € |
| **E — dans les 48 h** | 109 / 120 | 1090 € | **-27,50 €** | **-2,5 %** | -226,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 101 / 112 | 1010 € | **-4,00 €** | **-0,4 %** | -199,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 35 gagnés, 74 perdus, 0 remboursés, 40 en attente · cote moyenne 3,26 · pire série perdante 9

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 2 / 2 | 40 € | +30,00 € | +75,0 % | 50 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 1 / 1 | 20 € | +55,00 € | +275,0 % | 100 % |
| EV < 0 (approx) | 15 / 18 | 300 € | -192,00 € | -64,0 % | 13 % |
| EV < 0 (exacte) | 13 / 14 | 260 € | +149,00 € | +57,3 % | 46 % |
| non évaluable | 76 / 112 | 1605 € | -56,50 € | -3,5 % | 33 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 17 / 46 | 425 € | +2,50 € | +0,6 % | 41 % |
| Winamax | 92 / 103 | 1840 € | -57,00 € | -3,1 % | 30 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 29 | 0 € | +0,00 € | – | – |
| match | 109 / 120 | 2265 € | -54,50 € | -2,4 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 92 / 103 | 1840 € | -57,00 € | -3,1 % | 30 % |
| 25 € | 17 / 46 | 425 € | +2,50 € | +0,6 % | 41 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 43 / 56 | 930 € | +45,50 € | +4,9 % | 42 % |
| 3 – 5 | 60 / 74 | 1215 € | -80,00 € | -6,6 % | 27 % |
| 5 – 10 | 6 / 10 | 120 € | -20,00 € | -16,7 % | 17 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 2 / 2 | 40 € | +8,00 € | +20,0 % | 50 % |
| Basketball | 5 / 30 | 100 € | -58,00 € | -58,0 % | 20 % |
| Football | 57 / 67 | 1190 € | +1,00 € | +0,1 % | 32 % |
| Football Américain | 5 / 5 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 11 / 12 | 220 € | -95,00 € | -43,2 % | 18 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 13 / 17 | 275 € | +225,00 € | +81,8 % | 62 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 109 / 149 | 2265 € | -54,50 € | -2,4 % | 32 % |

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
| 12/10 21h00 · Levante - FC Séville | FC Séville gagne le match 1-0, 2-0 ou 3-0 | 4,75 | – | – | 20 € | ⏳ |
| 12/10 21h00 · Coventry - Newcastle | Newcastle gagne à la mi-temps et à la fin du match | 3,5 | 6,682 | -47,6 % ≈ | 20 € | ⏳ |
| 12/10 20h45 · Top Football Européen (12/10) | Au moins 2 joueurs marquent dans le Quatuor : Y.Wissa/G.Simeone/Pape Moussa Fall/R.Ure ? (Remboursé si non titulaire(s)) | 2,3 | – | – | 25 € | ⏳ |
| 12/10 20h45 · Torino - Udinese | Torino gagne ou fait match nul et les deux équipes marquent | 2,5 | 4,943 | -49,4 % ≈ | 20 € | ⏳ |
| 12/10 19h10 · Buffalo Sabres - Florida Panthers | Matthew Tkachuk + Tage Thompson marquent 2 buts ou plus (avec Garantie Golden Goal) | 4,0 | – | – | 20 € | ⏳ |
| 12/10 18h30 · Atalanta - Venise | Atalanta gagne et les deux équipes marquent | 2,8 | – | – | 20 € | ⏳ |
| 12/10 18h00 · Galatasaray - Bursaspor Durmazlar | Galatasaray gagne et plus de 166,5 points dans le match | 3,15 | – | – | 20 € | ⏳ |
| 12/10 15h30 · Alexandra Eala - Han Shi | Alexandra Eala gagne 2-1 | 4,25 | 4,384 | -3,1 % | 20 € | ⏳ |
| 12/10 14h00 · LaLiga 2 | Plus de 1,5 buts dans chacun des 4 matchs du jour | 3,25 | – | – | 20 € | ⏳ |
| 12/10 13h00 · A.Fils - Van De Zandsch | A.Fils remporte le 1er set et moins de 9,5 jeux dans le set ? | 2,5 | – | – | 25 € | ⏳ |
| 12/10 12h00 · Zizou Bergs - Carlos Alcaraz | Au moins un Tie-break lors du match | 3,25 | – | – | 20 € | ⏳ |
| 12/10 09h30 · Arthur Fils - Botic van de Zandschulp | Arthur Fils gagne et moins de 21,5 jeux dans le match | 2,25 | 2,695 | -16,5 % ≈ | 20 € | ⏳ |
| 12/10 07h10 · Jiri Lehecka - Rafael Jodar | Rafael Jodar gagne 2-1 | 5,0 | 5,843 | -14,4 % | 20 € | ✅ +80,00 € |
| 12/10 06h00 · Pablo Carreno-Busta - Felix Auger-Aliassime | Felix Auger-Aliassime gagne 2-1 | 3,55 | 4,412 | -19,5 % | 20 € | ✅ +51,00 € |
| 12/10 03h15 · U.N.A.M. - Cruz Azul | Cruz Azul gagne à la mi-temps et à la fin du match | 3,25 | 5,757 | -43,5 % ≈ | 20 € | ❌ -20,00 € |
| 12/10 02h20 · Atlanta Falcons - Baltimore Ravens | Plus de 53,5 points lors du match | 3,75 | – | – | 20 € | ❌ -20,00 € |
| 12/10 02h00 · Milwaukee Brewers - Los Angeles Dodgers | Les deux équipes marquent chacune au moins 3 runs | 3,2 | 3,254 | -1,7 % ≈ | 20 € | ❌ -20,00 € |

≈ : calcul approché (conditions liées sur un même match).
