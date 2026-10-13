# Bilan des cotes boostées (stratégies et risques)

## Protocole gelé (gel-1) — seuls ces résultats comptent

Règles fixées le 11/10 22h00 avant de connaître leurs résultats ; jugées uniquement sur les boosts découverts après (35 pour l'instant).

| Stratégie suivie | Paris réglés | Misé | Gain net | ROI | Valeur moyenne jouée |
|---|---|---|---|---|---|
| **A — témoin** | 15 / 35 | 305 € | **+46,00 €** | **+15,1 %** | -18,2 % (12 paris) |
| **B — valeur ≥ +5 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **B0 — valeur ≥ 0 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | – |
| **D — hypothèse (cotes 1,60–3,50)** | 9 / 22 | 90 € | **-4,50 €** | **-5,0 %** | -23,9 % (8 paris) |

« Valeur moyenne jouée » : écart moyen entre la cote prise et la cote juste (Pinnacle / Betfair), sur les paris dont la valeur était calculable avant le match. Indicateur peu bruité, lisible en quelques jours ; le ROI, lui, demande des centaines de paris.

## Toutes les stratégies depuis le début (archives, non jugées)

Mis à jour le 13/10 09h34 (heure de Paris). Argent fictif : A/B à la mise max ; C-H avec mises plafonnées et filtres prédéfinis. Les F/G utilisent la cote du premier calcul EV.

| Stratégie | Paris réglés | Misé | Gain net | ROI | Pire baisse |
|---|---|---|---|---|---|
| **A — tout miser** | 122 / 169 | 2530 € | **-68,50 €** | **-2,7 %** | -471,00 € |
| **B-exacte (EV ≥ 5 %)** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B-approx (EV ≥ 5 %)** | 4 / 4 | 80 € | **+145,00 €** | **+181,2 %** | -20,00 € |
| **C — 10 € maximum** | 122 / 169 | 1220 € | **-32,00 €** | **-2,6 %** | -226,00 € |
| **D — cote 1,60–3,50** | 84 / 115 | 840 € | **-16,00 €** | **-1,9 %** | -148,50 € |
| **E — dans les 48 h** | 122 / 138 | 1220 € | **-32,00 €** | **-2,6 %** | -226,00 € |
| **F — EV exacte ≥ 8 %** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **G — quart Kelly** | 0 / 0 | 0 € | **+0,00 €** | **–** | +0,00 € |
| **H — un boost/match** | 114 / 129 | 1140 € | **-8,50 €** | **-0,7 %** | -199,50 € |
| **B — valeur ≥ +5 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |
| **B0 — valeur ≥ 0 %** | 1 / 1 | 20 € | **-20,00 €** | **-100,0 %** | -20,00 € |

**Hypothèses exploratoires** : C plafonne chaque mise à 10 € ; D ajoute la zone de cotes 1,60–3,50 ; E sélectionne les matchs dans les 48 h de leur première observation ; F exige EV exacte ≥ 8 % et cote ≤ 4 ; G utilise un quart Kelly sur une banque fictive constante de 1 000 € avec un plafond de 1 % par pari ; H retient uniquement le premier boost observé par match. Le changement de mise réduit l'exposition absolue, pas nécessairement le ROI. Ces seuils sont fixés à l'avance, pas calibrés sur les gagnants passés.

**Validité** : seulement les paris réglés entrent dans les gains et le ROI. Les futurs, les marchés dépendants, les erreurs de règlement et les offres dont le prix a changé peuvent fausser les comparaisons. Les EV proviennent de prix de marché, non de probabilités garanties. Aucune stratégie n'est validée sur un échantillon réduit.


- **A** : chaque boost publié.
- **B-exacte** : seulement les boosts dont la cote juste Pinnacle (marge retirée) donne au moins +5 % d'EV, calcul exact (un seul pari, ou des matchs différents).
- **B-approx** : idem, mais pour les combinés sur un même match (produit des probabilités, lien entre les conditions ignoré).

A en détail : 39 gagnés, 83 perdus, 0 remboursés, 47 en attente · cote moyenne 3,26 · pire série perdante 9

> Simulation uniquement. Les paris sportifs comportent un risque de perte. Joueurs Info Service : 09 74 75 13 13.

### A par valeur face à Pinnacle (le filtre B marche-t-il ?)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| EV 0 à 5 % (approx) | 1 / 2 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 10 % et + (approx) | 2 / 2 | 40 € | +30,00 € | +75,0 % | 50 % |
| EV 10 % et + (exacte) | 1 / 1 | 20 € | -20,00 € | -100,0 % | 0 % |
| EV 5 à 10 % (approx) | 2 / 2 | 40 € | +115,00 € | +287,5 % | 100 % |
| EV < 0 (approx) | 19 / 21 | 380 € | -222,00 € | -58,4 % | 16 % |
| EV < 0 (exacte) | 14 / 16 | 280 € | +129,00 € | +46,1 % | 43 % |
| non évaluable | 83 / 125 | 1750 € | -80,50 € | -4,6 % | 32 % |

### A par bookmaker

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Unibet | 18 / 52 | 450 € | -22,50 € | -5,0 % | 39 % |
| Winamax | 104 / 117 | 2080 € | -46,00 € | -2,2 % | 31 % |

### A par horizon (paris de saison réglés en fin de saison)

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| long terme (saison) | 0 / 31 | 0 € | +0,00 € | – | – |
| match | 122 / 138 | 2530 € | -68,50 € | -2,7 % | 32 % |

### A par mise max

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 20 € | 104 / 117 | 2080 € | -46,00 € | -2,2 % | 31 % |
| 25 € | 18 / 52 | 450 € | -22,50 € | -5,0 % | 39 % |

### A par tranche de cote

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 10 et + | 0 / 1 | 0 € | +0,00 € | – | – |
| 2 – 3 | 48 / 64 | 1035 € | +46,50 € | +4,5 % | 42 % |
| 3 – 5 | 68 / 85 | 1375 € | -95,00 € | -6,9 % | 26 % |
| 5 – 10 | 6 / 11 | 120 € | -20,00 € | -16,7 % | 17 % |
| < 2 | 0 / 8 | 0 € | +0,00 € | – | – |

### A par sport

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| Baseball | 3 / 3 | 60 € | -12,00 € | -20,0 % | 33 % |
| Basketball | 6 / 30 | 120 € | -78,00 € | -65,0 % | 17 % |
| Football | 63 / 83 | 1310 € | +67,00 € | +5,1 % | 33 % |
| Football Américain | 5 / 5 | 100 € | -100,00 € | -100,0 % | 0 % |
| Formule 1 | 3 / 3 | 65 € | -65,00 € | -100,0 % | 0 % |
| Handball | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Hockey sur glace | 12 / 12 | 240 € | -115,00 € | -47,9 % | 17 % |
| Judo | 2 / 2 | 40 € | -40,00 € | -100,0 % | 0 % |
| Rugby | 3 / 3 | 75 € | -12,50 € | -16,7 % | 33 % |
| Rugby à XV | 5 / 5 | 100 € | +47,00 € | +47,0 % | 60 % |
| Tennis | 17 / 20 | 360 € | +205,00 € | +56,9 % | 53 % |
| Tennis de table | 1 / 1 | 20 € | +75,00 € | +375,0 % | 100 % |

### A par mois

| | Paris réglés | Misé | Gain net | ROI | Réussite |
|---|---|---|---|---|---|
| 2026-10 | 122 / 169 | 2530 € | -68,50 € | -2,7 % | 32 % |

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
| 13/10 21h00 · Atl. Madrid - Man. United | Le Duo J.Alvarez+B.Fernandes sera décisif au moins 2 fois en cumulé ? (Remboursé si non titulaire(s)) | 2,3 | – | – | 25 € | ⏳ |
| 13/10 21h00 · Arsenal - Lille | Arsenal ou Lille gagne et les 2 équipes marquent ? | 2,8 | – | – | 25 € | ⏳ |
| 13/10 21h00 · Leipzig - PSV Eindhoven | Christopher Nkunku marque au moins un but en 1ère mi-temps | 4,25 | – | – | 20 € | ⏳ |
| 13/10 21h00 · Villarreal - Naples | Villarreal ou Naples marque sur penalty | 3,85 | – | – | 20 € | ⏳ |
| 13/10 21h00 · Galatasaray - FC Barcelone | FC Barcelone gagne les deux mi-temps | 2,55 | – | – | 20 € | ⏳ |
| 13/10 21h00 · Viking - Bayern Munich | H. Kane buteur sur une passe décisive de M. Olise | 4,0 | – | – | 20 € | ⏳ |
| 13/10 21h00 · Inter Milan - Club Bruges | Lautaro Martínez et Marcus Thuram marquent chacun au moins un but | 3,5 | – | – | 20 € | ⏳ |
| 13/10 21h00 · Atletico Madrid - Manchester United | Atletico Madrid gagne et plus de 3,5 buts dans le match | 4,2 | 5,134 | -18,2 % ≈ | 20 € | ⏳ |
| 13/10 21h00 · Arsenal - Lille | Arsenal gagne et les deux équipes marquent | 3,1 | 2,981 | +4,0 % ≈ | 20 € | ⏳ |
| 13/10 20h45 · CB - ChampionsLeague (13/10) | Au moins 5 équipes marquent chacune 3 buts ou plus lors des 7 matchs de 21h ? | 2,5 | – | – | 25 € | ⏳ |
| 13/10 20h45 · CB - ChampionsLeague (13/10) | Au moins 2 joueurs marquent dans le Trio M.Olise/M.Thuram/C.Nkunku ? (Remboursé si non titulaire(s)) | 2,3 | – | – | 25 € | ⏳ |
| 13/10 18h45 · Lens - Sporting | F.Thauvin décisif et Lens gagne le match ? (Remboursé si non titulaire(s)) | 3,0 | – | – | 25 € | ⏳ |
| 13/10 18h45 · Sabah - Slavia Prague | Slavia Prague gagne le match 2-1, 3-1 ou 4-1 | 5,25 | – | – | 20 € | ⏳ |
| 13/10 18h45 · Lens - Sporting Portugal | Lens gagne le match et Florian Thauvin marque au moins un but ou fait au moins une passe décisive | 3,0 | – | – | 20 € | ⏳ |
| 13/10 18h45 · Ligue des Champions | Plus de 36,5 buts sur les 9 matchs du jour | 4,25 | – | – | 20 € | ⏳ |
| 13/10 13h10 · Hubert Hurkacz - Alejandro Davidovich Fokina | Plus de 2,5 sets lors du match | 2,25 | 2,363 | -4,8 % | 20 € | ⏳ |
| 13/10 12h00 · A.Zverev - A.Bublik | Les 2 joueurs gagnent un set ? | 2,5 | 2,714 | -7,9 % | 25 € | ⏳ |

≈ : calcul approché (conditions liées sur un même match).
