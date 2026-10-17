# Recherche de stratégies — replay chronologique

Source initiale : branche donnees, commit `fb09dbd70b7d302838c1a107cc47e77db2a3bcdb` ; dernière observation du 2026-10-17T17:21:34+00:00.
Les observations initiales, premières valeurs et heures de publication des règlements proviennent de 141 instantanés Git.
Une offre retirée du fichier courant reste dans l'historique, sans être transformée en perte.

## Méthode

Les 30 premiers résultats disponibles servent d'amorçage. Chaque nouvelle offre est ensuite décidée avec les seuls résultats déjà publiés, strictement avant cet instant.
Le prix, la mise maximale et les catégories sont pris dans le premier instantané disponible avant match. Une value tardive ne remonte jamais à la découverte de l'offre.
Les mises restent immobilisées jusqu'à la publication du règlement, y compris lorsque plusieurs matchs ont lieu simultanément. Banque initiale : 1 000 €. Plafonds : 10 % de mises ouvertes, 2 % par libellé de rencontre.
J choisit quotidiennement parmi 56 filtres, avec au moins 12 anciens résultats et un score pénalisant les faibles échantillons et la dispersion. Il mise 1 % de la bankroll, maximum 20 €.
K calibre une régression logistique régularisée sur le prix normal bookmaker, la cote, le sport et le bookmaker. Les multiples boosts d'un match se partagent un poids total de 1 pendant l'apprentissage. EV estimée ≥ 5 %, maximum 10 €.
L utilise la même probabilité avec l'edge réduit de moitié puis Kelly 1/8, calculé sur la bankroll disponible et plafonné à 20 €. M utilise le même modèle que K, avec 20 € maximum.
Le prix normal contient la marge du bookmaker : ce prior et l'EV du modèle ne sont pas des références de cote juste.

## Comparaison sur la période après amorçage

| Simulation | Réglés / paris | Mises réglées | Gain net | ROI | Baisse maximale |
|---|---|---|---|---|---|
| temoin_10 | 99 / 109 | 907.25 € | -67.40 € | -7.4 % | -167.12 € |
| temoin_20 | 60 / 67 | 970.30 € | +73.43 € | +7.6 % | -162.12 € |
| value_0 | 3 / 3 | 30.00 € | -30.00 € | -100.0 % | -30.00 € |
| value_5 | 2 / 2 | 20.00 € | -20.00 € | -100.0 % | -20.00 € |
| J_adaptative | 44 / 45 | 424.43 € | +19.39 € | +4.6 % | -122.83 € |
| K_modele | 59 / 63 | 574.90 € | +120.73 € | +21.0 % | -74.75 € |
| L_kelly_dynamique | 62 / 65 | 406.85 € | +39.06 € | +9.6 % | -59.37 € |
| M_modele_20 | 43 / 47 | 818.57 € | +349.38 € | +42.7 % | -85.88 € |

Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.
M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.

## Stabilité et calibration

Sur 218 prévisions réglées : score de Brier du modèle 0.2124, prior bookmaker 0.2133 (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.

| Simulation | Dispersion ROI à 90 % par bootstrap de rencontres |
|---|---|
| J_adaptative | [-32.7, 46.3] |
| K_modele | [-14.0, 58.9] |
| L_kelly_dynamique | [-23.9, 43.5] |
| M_modele_20 | [1.2, 87.4] |
Ces intervalles décrivent la dispersion des paris déjà sélectionnés ; ils ne corrigent pas la sélection a posteriori des méthodes et ne simulent pas un nouvel apprentissage complet.

### J_adaptative par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 14 | -28.27 € |
| 2026-10-11 | 12 | -82.06 € |
| 2026-10-13 | 5 | +70.16 € |
| 2026-10-14 | 6 | +17.26 € |
| 2026-10-15 | 3 | +4.72 € |
| 2026-10-16 | 3 | +47.87 € |
| 2026-10-17 | 1 | -10.29 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Football | 19 | -119.44 € |
| Football Américain | 1 | -9.05 € |
| Formule 1 | 1 | -10.00 € |
| Hockey sur glace | 1 | -9.52 € |
| Rugby | 2 | +5.00 € |
| Tennis | 20 | +162.40 € |

### K_modele par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -32.25 € |
| 2026-10-11 | 14 | +23.98 € |
| 2026-10-12 | 3 | +2.50 € |
| 2026-10-13 | 8 | +74.00 € |
| 2026-10-14 | 6 | +18.00 € |
| 2026-10-15 | 4 | -5.00 € |
| 2026-10-16 | 5 | +69.50 € |
| 2026-10-17 | 3 | -30.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -10.00 € |
| Basketball | 1 | -10.00 € |
| Football | 18 | +12.00 € |
| Football Américain | 1 | -10.00 € |
| Formule 1 | 3 | -30.00 € |
| Hockey sur glace | 1 | -9.00 € |
| Rugby | 3 | -5.00 € |
| Rugby à XV | 2 | -1.52 € |
| Tennis | 29 | +184.25 € |

### L_kelly_dynamique par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -20.08 € |
| 2026-10-11 | 17 | -7.25 € |
| 2026-10-12 | 3 | +2.09 € |
| 2026-10-13 | 8 | +53.84 € |
| 2026-10-14 | 6 | +16.18 € |
| 2026-10-15 | 4 | +5.56 € |
| 2026-10-16 | 5 | +26.40 € |
| 2026-10-17 | 3 | -37.68 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -3.94 € |
| Basketball | 1 | -3.65 € |
| Football | 18 | -56.99 € |
| Football Américain | 2 | -11.83 € |
| Formule 1 | 3 | -11.09 € |
| Hockey sur glace | 3 | -5.08 € |
| Rugby | 2 | +11.14 € |
| Rugby à XV | 2 | +4.58 € |
| Tennis | 30 | +115.92 € |

### M_modele_20 par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 8 | -11.60 € |
| 2026-10-11 | 9 | +110.97 € |
| 2026-10-12 | 2 | +23.15 € |
| 2026-10-13 | 8 | +148.00 € |
| 2026-10-14 | 5 | +8.25 € |
| 2026-10-15 | 4 | -10.00 € |
| 2026-10-16 | 4 | +140.61 € |
| 2026-10-17 | 3 | -60.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Basketball | 1 | -20.00 € |
| Football | 15 | +25.56 € |
| Formule 1 | 1 | -19.76 € |
| Hockey sur glace | 1 | -17.82 € |
| Rugby | 0 | +0.00 € |
| Tennis | 25 | +381.40 € |

## Sensibilité du modèle : les 9 variantes explorées

| EV estimée minimale | Mise maximale | Réglés | Gain net | ROI | Baisse maximale |
|---|---|---|---|---|---|
| 0 % | 5 € | 96 | +0.98 € | +0.2 % | -54.52 € |
| 0 % | 10 € | 73 | +19.59 € | +2.8 % | -92.44 € |
| 0 % | 20 € | 46 | +161.11 € | +19.2 % | -143.22 € |
| 5 % | 5 € | 73 | +40.00 € | +11.0 % | -52.25 € |
| 5 % | 10 € | 59 | +120.73 € | +21.0 % | -74.75 € |
| 5 % | 20 € | 43 | +349.38 € | +42.7 % | -85.88 € |
| 10 % | 5 € | 60 | +42.25 € | +14.1 % | -46.75 € |
| 10 % | 10 € | 49 | +100.75 € | +21.0 % | -79.75 € |
| 10 % | 20 € | 36 | +204.03 € | +30.0 % | -76.00 € |

## Classement exploratoire des 56 filtres

Ce classement a été trié après lecture de tous les résultats. Il sert à proposer des hypothèses, pas à valider une stratégie. Le meilleur filtre tennis repose sur très peu de paris.
| Filtre | Réglés | Gain net | ROI |
|---|---|---|---|
| sport:tennis:1.5-5 | 29 | +200.50 € | +69.1 % |
| sport:tennis:2-5 | 29 | +200.50 € | +69.1 % |
| sport:tennis:1.5-8 | 30 | +190.50 € | +63.5 % |
| sport:tennis:3-5 | 15 | +173.00 € | +115.3 % |
| sport:tennis:1.5-3.5 | 18 | +115.00 € | +63.9 % |
| sport:tennis:2-3.5 | 18 | +115.00 € | +63.9 % |
| sport:tennis:1.5-2.5 | 6 | +12.50 € | +20.8 % |
| sport:rugby:1.5-3.5 | 13 | +6.00 € | +4.6 % |
| sport:rugby:2-3.5 | 13 | +6.00 € | +4.6 % |
| sport:hockey sur glace:1.5-2.5 | 2 | +5.00 € | +25.0 % |
| sport:basketball:1.5-2.5 | 2 | +1.00 € | +5.0 % |
| sport:rugby:1.5-2.5 | 5 | +0.00 € | +0.0 % |
| sport:rugby:1.5-5 | 14 | -4.00 € | -2.9 % |
| sport:rugby:1.5-8 | 14 | -4.00 € | -2.9 % |
| sport:rugby:2-5 | 14 | -4.00 € | -2.9 % |
| sport:hockey sur glace:1.5-3.5 | 12 | -5.50 € | -4.6 % |
| sport:hockey sur glace:2-3.5 | 12 | -5.50 € | -4.6 % |
| bookmaker:Winamax:1.5-2.5 | 25 | -11.50 € | -4.6 % |
| sport:football:3-5 | 65 | -12.88 € | -2.0 % |
| sport:rugby:3-5 | 5 | -17.50 € | -35.0 % |
| sport:basketball:1.5-3.5 | 6 | -29.00 € | -48.3 % |
| sport:basketball:2-3.5 | 6 | -29.00 € | -48.3 % |
| bookmaker:Unibet:1.5-2.5 | 13 | -32.50 € | -25.0 % |
| sport:football:1.5-2.5 | 20 | -36.00 € | -18.0 % |
| bookmaker:Unibet:1.5-3.5 | 33 | -37.00 € | -11.2 % |
| bookmaker:Unibet:2-3.5 | 33 | -37.00 € | -11.2 % |
| tous:tous:1.5-2.5 | 40 | -44.50 € | -11.1 % |
| bookmaker:Unibet:1.5-5 | 34 | -47.00 € | -13.8 % |
| bookmaker:Unibet:1.5-8 | 34 | -47.00 € | -13.8 % |
| bookmaker:Unibet:2-5 | 34 | -47.00 € | -13.8 % |
| sport:basketball:1.5-5 | 8 | -49.00 € | -61.3 % |
| sport:basketball:1.5-8 | 8 | -49.00 € | -61.3 % |
| sport:basketball:2-5 | 8 | -49.00 € | -61.3 % |
| sport:basketball:3-5 | 5 | -50.00 € | -100.0 % |
| sport:football:1.5-5 | 69 | -56.23 € | -8.4 % |
| sport:football:1.5-8 | 69 | -56.23 € | -8.4 % |
| sport:football:2-5 | 69 | -56.23 € | -8.4 % |
| sport:football:1.5-3.5 | 59 | -68.03 € | -12.2 % |
| sport:football:2-3.5 | 59 | -68.03 € | -12.2 % |
| bookmaker:Unibet:3-5 | 10 | -69.50 € | -69.5 % |
| bookmaker:Winamax:3-5 | 87 | -71.93 € | -8.7 % |
| tous:tous:2-5 | 99 | -76.17 € | -8.4 % |
| sport:hockey sur glace:1.5-5 | 23 | -79.50 € | -34.6 % |
| sport:hockey sur glace:2-5 | 23 | -79.50 € | -34.6 % |
| tous:tous:1.5-5 | 99 | -81.89 € | -9.1 % |
| sport:hockey sur glace:1.5-8 | 24 | -89.50 € | -37.3 % |
| sport:hockey sur glace:3-5 | 19 | -90.50 € | -47.6 % |
| tous:tous:1.5-8 | 96 | -97.73 € | -10.9 % |
| tous:tous:3-5 | 83 | -101.59 € | -12.6 % |
| bookmaker:Winamax:1.5-5 | 96 | -141.80 € | -15.4 % |
| bookmaker:Winamax:2-5 | 96 | -141.80 € | -15.4 % |
| bookmaker:Winamax:1.5-8 | 98 | -152.50 € | -16.4 % |
| tous:tous:2-3.5 | 85 | -159.20 € | -20.1 % |
| tous:tous:1.5-3.5 | 86 | -183.28 € | -23.2 % |
| bookmaker:Winamax:1.5-3.5 | 79 | -261.75 € | -34.6 % |
| bookmaker:Winamax:2-3.5 | 79 | -261.75 € | -34.6 % |

## Suivi futur gelé

Départ : 2026-10-14T00:00:00+00:00. Chaque simulation repart avec 1 000 € et peut apprendre des anciens règlements, mais ne joue que les nouvelles observations à partir de cette date.
Les décisions, probabilités et mises sont conservées dans un journal par version. Une modification d'une décision existante est refusée ; une évolution du modèle exige une nouvelle version.

## Limites

- Rejeu rétrospectif choisi après consultation de ce même historique.
- Règlements automatiques non vérifiés indépendamment.
- Prix normal bookmaker utilisé comme prior, avec marge ; EV du modèle estimée.
- 56 filtres explorés : leur meilleur score final est choisi après coup.
- 9 variantes de seuil et mise explorées : M est une candidate choisie après cette comparaison.
- Bankroll 1 000 €, exposition ouverte ≤ 10 %, par libellé de rencontre ≤ 2 %.
- Les combinés peuvent partager des rencontres non identifiables par leurs seuls libellés.

Producteurs des 260 événements de règlement : {'gpt-6-luna': 260}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.
La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.

Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.
