# Recherche de stratégies — replay chronologique

Source initiale : branche donnees, commit `fb09dbd70b7d302838c1a107cc47e77db2a3bcdb` ; dernière observation du 2026-10-16T17:18:07+00:00.
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
| temoin_10 | 89 / 100 | 823.95 € | -72.56 € | -8.8 % | -167.12 € |
| temoin_20 | 53 / 62 | 892.57 € | +15.96 € | +1.8 % | -162.12 € |
| value_0 | 1 / 2 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| value_5 | 1 / 1 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| J_adaptative | 43 / 44 | 414.14 € | +29.68 € | +7.2 % | -122.83 € |
| K_modele | 54 / 57 | 524.90 € | +130.73 € | +24.9 % | -74.75 € |
| L_kelly_dynamique | 57 / 60 | 364.02 € | +75.53 € | +20.7 % | -59.37 € |
| M_modele_20 | 39 / 41 | 744.70 € | +367.77 € | +49.4 % | -85.88 € |

Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.
M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.

## Stabilité et calibration

Sur 190 prévisions réglées : score de Brier du modèle 0.2113, prior bookmaker 0.2113 (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.

| Simulation | Dispersion ROI à 90 % par bootstrap de rencontres |
|---|---|
| J_adaptative | [-31.4, 47.2] |
| K_modele | [-10.6, 61.9] |
| L_kelly_dynamique | [-16.4, 57.3] |
| M_modele_20 | [3.1, 94.2] |
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

| Sport | Réglés | Gain net |
|---|---|---|
| Football | 19 | -119.44 € |
| Football Américain | 1 | -9.05 € |
| Formule 1 | 1 | -10.00 € |
| Hockey sur glace | 1 | -9.52 € |
| Rugby | 2 | +5.00 € |
| Tennis | 19 | +172.69 € |

### K_modele par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -32.25 € |
| 2026-10-11 | 14 | +23.98 € |
| 2026-10-12 | 3 | +2.50 € |
| 2026-10-13 | 8 | +74.00 € |
| 2026-10-14 | 6 | +18.00 € |
| 2026-10-15 | 4 | -5.00 € |
| 2026-10-16 | 3 | +49.50 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -10.00 € |
| Basketball | 1 | -10.00 € |
| Football | 17 | -18.00 € |
| Football Américain | 1 | -10.00 € |
| Formule 1 | 3 | -30.00 € |
| Hockey sur glace | 1 | -9.00 € |
| Rugby | 3 | -5.00 € |
| Rugby à XV | 1 | +8.48 € |
| Tennis | 26 | +214.25 € |

### L_kelly_dynamique par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -20.08 € |
| 2026-10-11 | 17 | -7.25 € |
| 2026-10-12 | 3 | +2.09 € |
| 2026-10-13 | 8 | +53.84 € |
| 2026-10-14 | 6 | +16.18 € |
| 2026-10-15 | 4 | +5.56 € |
| 2026-10-16 | 3 | +25.19 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -3.94 € |
| Basketball | 1 | -3.65 € |
| Football | 17 | -61.76 € |
| Football Américain | 2 | -11.83 € |
| Formule 1 | 3 | -11.09 € |
| Hockey sur glace | 3 | -5.08 € |
| Rugby | 2 | +11.14 € |
| Rugby à XV | 1 | +8.14 € |
| Tennis | 27 | +153.60 € |

### M_modele_20 par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 8 | -11.60 € |
| 2026-10-11 | 9 | +110.97 € |
| 2026-10-12 | 2 | +23.15 € |
| 2026-10-13 | 8 | +148.00 € |
| 2026-10-14 | 5 | +8.25 € |
| 2026-10-15 | 4 | -10.00 € |
| 2026-10-16 | 3 | +99.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Basketball | 1 | -20.00 € |
| Football | 14 | -16.05 € |
| Formule 1 | 1 | -19.76 € |
| Hockey sur glace | 1 | -17.82 € |
| Tennis | 22 | +441.40 € |

## Sensibilité du modèle : les 9 variantes explorées

| EV estimée minimale | Mise maximale | Réglés | Gain net | ROI | Baisse maximale |
|---|---|---|---|---|---|
| 0 % | 5 € | 89 | +15.98 € | +3.6 % | -54.52 € |
| 0 % | 10 € | 66 | +42.54 € | +6.7 % | -92.44 € |
| 0 % | 20 € | 42 | +241.11 € | +31.8 % | -143.22 € |
| 5 % | 5 € | 68 | +45.00 € | +13.3 % | -52.25 € |
| 5 % | 10 € | 54 | +130.73 € | +24.9 % | -74.75 € |
| 5 % | 20 € | 39 | +367.77 € | +49.4 % | -85.88 € |
| 10 % | 5 € | 56 | +62.25 € | +22.3 % | -46.75 € |
| 10 % | 10 € | 45 | +140.75 € | +32.0 % | -79.75 € |
| 10 % | 20 € | 32 | +267.92 € | +43.5 % | -76.00 € |

## Classement exploratoire des 56 filtres

Ce classement a été trié après lecture de tous les résultats. Il sert à proposer des hypothèses, pas à valider une stratégie. Le meilleur filtre tennis repose sur très peu de paris.
| Filtre | Réglés | Gain net | ROI |
|---|---|---|---|
| sport:tennis:1.5-5 | 26 | +230.50 € | +88.7 % |
| sport:tennis:2-5 | 26 | +230.50 € | +88.7 % |
| sport:tennis:1.5-8 | 27 | +220.50 € | +81.7 % |
| sport:tennis:3-5 | 14 | +183.00 € | +130.7 % |
| sport:tennis:1.5-3.5 | 16 | +135.00 € | +84.4 % |
| sport:tennis:2-3.5 | 16 | +135.00 € | +84.4 % |
| sport:tennis:1.5-2.5 | 5 | +22.50 € | +45.0 % |
| sport:rugby:1.5-2.5 | 4 | +10.00 € | +25.0 % |
| sport:hockey sur glace:1.5-2.5 | 2 | +5.00 € | +25.0 % |
| bookmaker:Unibet:1.5-3.5 | 29 | +3.00 € | +1.0 % |
| bookmaker:Unibet:1.5-5 | 29 | +3.00 € | +1.0 % |
| bookmaker:Unibet:1.5-8 | 29 | +3.00 € | +1.0 % |
| bookmaker:Unibet:2-3.5 | 29 | +3.00 € | +1.0 % |
| bookmaker:Unibet:2-5 | 29 | +3.00 € | +1.0 % |
| sport:basketball:1.5-2.5 | 2 | +1.00 € | +5.0 % |
| bookmaker:Winamax:1.5-2.5 | 24 | -1.50 € | -0.6 % |
| sport:hockey sur glace:1.5-3.5 | 9 | -1.50 € | -1.7 % |
| sport:hockey sur glace:2-3.5 | 9 | -1.50 € | -1.7 % |
| sport:rugby:1.5-3.5 | 8 | -2.50 € | -3.1 % |
| sport:rugby:2-3.5 | 8 | -2.50 € | -3.1 % |
| tous:tous:1.5-2.5 | 36 | -4.50 € | -1.2 % |
| bookmaker:Unibet:1.5-2.5 | 11 | -12.50 € | -11.4 % |
| sport:rugby:1.5-5 | 9 | -12.50 € | -13.9 % |
| sport:rugby:1.5-8 | 9 | -12.50 € | -13.9 % |
| sport:rugby:2-5 | 9 | -12.50 € | -13.9 % |
| sport:football:1.5-2.5 | 18 | -16.00 € | -8.9 % |
| sport:rugby:3-5 | 2 | -20.00 € | -100.0 % |
| bookmaker:Winamax:3-5 | 74 | -27.15 € | -3.8 % |
| sport:basketball:1.5-3.5 | 6 | -29.00 € | -48.3 % |
| sport:basketball:2-3.5 | 6 | -29.00 € | -48.3 % |
| sport:football:3-5 | 56 | -32.88 € | -6.0 % |
| sport:football:1.5-5 | 60 | -34.23 € | -5.9 % |
| sport:football:1.5-8 | 60 | -34.23 € | -5.9 % |
| sport:football:2-5 | 60 | -34.23 € | -5.9 % |
| sport:basketball:1.5-5 | 8 | -49.00 € | -61.3 % |
| sport:basketball:1.5-8 | 8 | -49.00 € | -61.3 % |
| sport:basketball:2-5 | 8 | -49.00 € | -61.3 % |
| bookmaker:Unibet:3-5 | 8 | -49.50 € | -61.9 % |
| sport:basketball:3-5 | 5 | -50.00 € | -100.0 % |
| sport:hockey sur glace:3-5 | 16 | -60.50 € | -37.8 % |
| tous:tous:3-5 | 71 | -62.33 € | -9.0 % |
| sport:hockey sur glace:1.5-5 | 19 | -65.50 € | -34.5 % |
| sport:hockey sur glace:2-5 | 19 | -65.50 € | -34.5 % |
| sport:football:1.5-3.5 | 52 | -69.88 € | -14.0 % |
| sport:football:2-3.5 | 52 | -69.88 € | -14.0 % |
| sport:hockey sur glace:1.5-8 | 20 | -75.50 € | -37.8 % |
| tous:tous:1.5-5 | 89 | -80.88 € | -9.8 % |
| tous:tous:2-5 | 89 | -80.88 € | -9.8 % |
| tous:tous:1.5-8 | 86 | -98.48 € | -12.1 % |
| bookmaker:Winamax:1.5-5 | 84 | -120.21 € | -14.8 % |
| bookmaker:Winamax:2-5 | 84 | -120.21 € | -14.8 % |
| bookmaker:Winamax:1.5-8 | 86 | -128.45 € | -15.6 % |
| tous:tous:1.5-3.5 | 77 | -160.89 € | -22.4 % |
| tous:tous:2-3.5 | 77 | -160.89 € | -22.4 % |
| bookmaker:Winamax:1.5-3.5 | 71 | -235.75 € | -34.7 % |
| bookmaker:Winamax:2-3.5 | 71 | -235.75 € | -34.7 % |

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

Producteurs des 232 événements de règlement : {'gpt-6-luna': 232}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.
La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.

Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.
