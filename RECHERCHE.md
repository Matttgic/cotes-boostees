# Recherche de stratégies — replay chronologique

Source initiale : branche donnees, commit `fb09dbd70b7d302838c1a107cc47e77db2a3bcdb` ; dernière observation du 2026-10-15T17:06:16+00:00.
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
| temoin_10 | 75 / 82 | 703.18 € | -92.24 € | -13.1 % | -143.88 € |
| temoin_20 | 44 / 49 | 755.68 € | -2.58 € | -0.3 % | -161.00 € |
| value_0 | 1 / 1 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| value_5 | 1 / 1 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| J_adaptative | 38 / 40 | 365.87 € | -32.50 € | -8.9 % | -122.83 € |
| K_modele | 48 / 51 | 464.90 € | +76.23 € | +16.4 % | -74.75 € |
| L_kelly_dynamique | 51 / 54 | 313.16 € | +37.56 € | +12.0 % | -59.37 € |
| M_modele_20 | 33 / 36 | 624.70 € | +258.77 € | +41.4 % | -85.88 € |

Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.
M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.

## Stabilité et calibration

Sur 152 prévisions réglées : score de Brier du modèle 0.2143, prior bookmaker 0.2106 (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.

| Simulation | Dispersion ROI à 90 % par bootstrap de rencontres |
|---|---|
| J_adaptative | [-45.1, 30.7] |
| K_modele | [-23.3, 55.9] |
| L_kelly_dynamique | [-25.1, 49.1] |
| M_modele_20 | [-3.5, 92.0] |
Ces intervalles décrivent la dispersion des paris déjà sélectionnés ; ils ne corrigent pas la sélection a posteriori des méthodes et ne simulent pas un nouvel apprentissage complet.

### J_adaptative par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 14 | -28.27 € |
| 2026-10-11 | 12 | -82.06 € |
| 2026-10-13 | 5 | +70.16 € |
| 2026-10-14 | 6 | +17.26 € |
| 2026-10-15 | 1 | -9.59 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Football | 19 | -119.44 € |
| Football Américain | 1 | -9.05 € |
| Formule 1 | 1 | -10.00 € |
| Hockey sur glace | 1 | -9.52 € |
| Rugby | 2 | +5.00 € |
| Tennis | 14 | +110.51 € |

### K_modele par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -32.25 € |
| 2026-10-11 | 14 | +23.98 € |
| 2026-10-12 | 3 | +2.50 € |
| 2026-10-13 | 8 | +74.00 € |
| 2026-10-14 | 6 | +18.00 € |
| 2026-10-15 | 1 | -10.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -10.00 € |
| Basketball | 1 | -10.00 € |
| Football | 16 | -8.00 € |
| Football Américain | 1 | -10.00 € |
| Formule 1 | 3 | -30.00 € |
| Hockey sur glace | 1 | -9.00 € |
| Rugby | 3 | -5.00 € |
| Rugby à XV | 1 | +8.48 € |
| Tennis | 21 | +149.75 € |

### L_kelly_dynamique par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -20.08 € |
| 2026-10-11 | 17 | -7.25 € |
| 2026-10-12 | 3 | +2.09 € |
| 2026-10-13 | 8 | +53.84 € |
| 2026-10-14 | 6 | +16.18 € |
| 2026-10-15 | 1 | -7.22 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -3.94 € |
| Basketball | 1 | -3.65 € |
| Football | 16 | -58.97 € |
| Football Américain | 2 | -11.83 € |
| Formule 1 | 3 | -11.09 € |
| Hockey sur glace | 3 | -5.08 € |
| Rugby | 2 | +11.14 € |
| Rugby à XV | 1 | +8.14 € |
| Tennis | 22 | +112.84 € |

### M_modele_20 par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 8 | -11.60 € |
| 2026-10-11 | 9 | +110.97 € |
| 2026-10-12 | 2 | +23.15 € |
| 2026-10-13 | 8 | +148.00 € |
| 2026-10-14 | 5 | +8.25 € |
| 2026-10-15 | 1 | -20.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Basketball | 1 | -20.00 € |
| Football | 13 | +3.95 € |
| Formule 1 | 1 | -19.76 € |
| Hockey sur glace | 1 | -17.82 € |
| Tennis | 17 | +312.40 € |

## Sensibilité du modèle : les 9 variantes explorées

| EV estimée minimale | Mise maximale | Réglés | Gain net | ROI | Baisse maximale |
|---|---|---|---|---|---|
| 0 % | 5 € | 79 | -13.27 € | -3.4 % | -54.52 € |
| 0 % | 10 € | 56 | -15.96 € | -3.0 % | -92.44 € |
| 0 % | 20 € | 35 | +91.03 € | +14.3 % | -143.22 € |
| 5 % | 5 € | 62 | +17.75 € | +5.7 % | -52.25 € |
| 5 % | 10 € | 48 | +76.23 € | +16.4 % | -74.75 € |
| 5 % | 20 € | 33 | +258.77 € | +41.4 % | -85.88 € |
| 10 % | 5 € | 51 | +30.00 € | +11.8 % | -46.75 € |
| 10 % | 10 € | 40 | +76.25 € | +19.5 % | -79.75 € |
| 10 % | 20 € | 27 | +138.92 € | +26.9 % | -76.00 € |

## Classement exploratoire des 56 filtres

Ce classement a été trié après lecture de tous les résultats. Il sert à proposer des hypothèses, pas à valider une stratégie. Le meilleur filtre tennis repose sur très peu de paris.
| Filtre | Réglés | Gain net | ROI |
|---|---|---|---|
| sport:tennis:1.5-5 | 21 | +166.00 € | +79.0 % |
| sport:tennis:2-5 | 21 | +166.00 € | +79.0 % |
| sport:tennis:1.5-8 | 22 | +156.00 € | +70.9 % |
| sport:tennis:3-5 | 12 | +118.00 € | +98.3 % |
| sport:tennis:1.5-3.5 | 12 | +110.50 € | +92.1 % |
| sport:tennis:2-3.5 | 12 | +110.50 € | +92.1 % |
| sport:tennis:1.5-2.5 | 5 | +22.50 € | +45.0 % |
| sport:rugby:1.5-2.5 | 4 | +10.00 € | +25.0 % |
| sport:rugby:1.5-3.5 | 7 | +7.50 € | +10.7 % |
| sport:rugby:2-3.5 | 7 | +7.50 € | +10.7 % |
| sport:hockey sur glace:1.5-2.5 | 2 | +5.00 € | +25.0 % |
| sport:basketball:1.5-2.5 | 2 | +1.00 € | +5.0 % |
| bookmaker:Winamax:1.5-2.5 | 19 | +0.50 € | +0.3 % |
| sport:rugby:1.5-5 | 8 | -2.50 € | -3.1 % |
| sport:rugby:1.5-8 | 8 | -2.50 € | -3.1 % |
| sport:rugby:2-5 | 8 | -2.50 € | -3.1 % |
| sport:hockey sur glace:1.5-3.5 | 7 | -12.50 € | -17.9 % |
| sport:hockey sur glace:2-3.5 | 7 | -12.50 € | -17.9 % |
| tous:tous:1.5-2.5 | 30 | -12.50 € | -4.2 % |
| bookmaker:Unibet:1.5-3.5 | 23 | -17.50 € | -7.6 % |
| bookmaker:Unibet:1.5-5 | 23 | -17.50 € | -7.6 % |
| bookmaker:Unibet:1.5-8 | 23 | -17.50 € | -7.6 % |
| bookmaker:Unibet:2-3.5 | 23 | -17.50 € | -7.6 % |
| bookmaker:Unibet:2-5 | 23 | -17.50 € | -7.6 % |
| sport:basketball:1.5-3.5 | 5 | -19.00 € | -38.0 % |
| sport:basketball:2-3.5 | 5 | -19.00 € | -38.0 % |
| bookmaker:Unibet:3-5 | 5 | -19.50 € | -39.0 % |
| sport:rugby:3-5 | 2 | -20.00 € | -100.0 % |
| sport:football:1.5-2.5 | 12 | -24.00 € | -20.0 % |
| sport:football:3-5 | 47 | -24.38 € | -5.4 % |
| bookmaker:Unibet:1.5-2.5 | 10 | -25.00 € | -25.0 % |
| sport:football:1.5-3.5 | 44 | -34.88 € | -8.3 % |
| sport:football:2-3.5 | 44 | -34.88 € | -8.3 % |
| sport:basketball:1.5-5 | 7 | -39.00 € | -55.7 % |
| sport:basketball:1.5-8 | 7 | -39.00 € | -55.7 % |
| sport:basketball:2-5 | 7 | -39.00 € | -55.7 % |
| sport:football:1.5-5 | 50 | -39.23 € | -8.1 % |
| sport:football:1.5-8 | 50 | -39.23 € | -8.1 % |
| sport:football:2-5 | 50 | -39.23 € | -8.1 % |
| sport:basketball:3-5 | 4 | -40.00 € | -100.0 % |
| sport:hockey sur glace:3-5 | 11 | -41.50 € | -37.7 % |
| sport:hockey sur glace:1.5-5 | 14 | -46.50 € | -33.2 % |
| sport:hockey sur glace:2-5 | 14 | -46.50 € | -33.2 % |
| sport:hockey sur glace:1.5-8 | 15 | -56.50 € | -37.7 % |
| bookmaker:Winamax:3-5 | 62 | -77.39 € | -13.0 % |
| tous:tous:1.5-5 | 76 | -93.76 € | -13.4 % |
| tous:tous:2-5 | 76 | -93.76 € | -13.4 % |
| tous:tous:3-5 | 60 | -111.34 € | -19.0 % |
| tous:tous:1.5-8 | 74 | -114.75 € | -16.5 % |
| bookmaker:Winamax:1.5-5 | 72 | -118.29 € | -17.0 % |
| bookmaker:Winamax:2-5 | 72 | -118.29 € | -17.0 % |
| bookmaker:Winamax:1.5-8 | 74 | -127.45 € | -18.0 % |
| tous:tous:1.5-3.5 | 63 | -133.67 € | -22.2 % |
| tous:tous:2-3.5 | 63 | -133.67 € | -22.2 % |
| bookmaker:Winamax:1.5-3.5 | 60 | -156.12 € | -27.1 % |
| bookmaker:Winamax:2-3.5 | 60 | -156.12 € | -27.1 % |

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

Producteurs des 194 événements de règlement : {'gpt-6-luna': 194}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.
La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.

Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.
