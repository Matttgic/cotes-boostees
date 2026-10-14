# Recherche de stratégies — replay chronologique

Source initiale : branche donnees, commit `fb09dbd70b7d302838c1a107cc47e77db2a3bcdb` ; dernière observation du 2026-10-14T11:18:57+00:00.
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
| temoin_10 | 56 / 65 | 533.01 € | -65.94 € | -12.4 % | -107.52 € |
| temoin_20 | 32 / 38 | 574.83 € | -11.22 € | -2.0 % | -161.00 € |
| value_0 | 1 / 1 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| value_5 | 1 / 1 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| J_adaptative | 31 / 36 | 299.86 € | -30.86 € | -10.3 % | -122.83 € |
| K_modele | 40 / 46 | 384.90 € | +61.73 € | +16.0 % | -74.75 € |
| L_kelly_dynamique | 43 / 49 | 255.24 € | +32.03 € | +12.5 % | -59.37 € |
| M_modele_20 | 26 / 31 | 496.95 € | +257.52 € | +51.8 % | -85.88 € |

Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.
M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.

## Stabilité et calibration

Sur 111 prévisions réglées : score de Brier du modèle 0.1993, prior bookmaker 0.2018 (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.

| Simulation | Dispersion ROI à 90 % par bootstrap de rencontres |
|---|---|
| J_adaptative | [-49.8, 33.9] |
| K_modele | [-26.4, 61.8] |
| L_kelly_dynamique | [-28.1, 57.0] |
| M_modele_20 | [-6.5, 110.4] |
Ces intervalles décrivent la dispersion des paris déjà sélectionnés ; ils ne corrigent pas la sélection a posteriori des méthodes et ne simulent pas un nouvel apprentissage complet.

### J_adaptative par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 14 | -28.27 € |
| 2026-10-11 | 12 | -82.06 € |
| 2026-10-13 | 4 | +79.47 € |
| 2026-10-14 | 1 | +0.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Football | 19 | -119.44 € |
| Football Américain | 1 | -9.05 € |
| Formule 1 | 1 | -10.00 € |
| Hockey sur glace | 1 | -9.52 € |
| Rugby | 2 | +5.00 € |
| Tennis | 7 | +112.15 € |

### K_modele par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -32.25 € |
| 2026-10-11 | 14 | +23.98 € |
| 2026-10-12 | 3 | +2.50 € |
| 2026-10-13 | 6 | +67.50 € |
| 2026-10-14 | 1 | +0.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -10.00 € |
| Basketball | 1 | -10.00 € |
| Football | 15 | -24.50 € |
| Football Américain | 1 | -10.00 € |
| Formule 1 | 3 | -30.00 € |
| Hockey sur glace | 1 | -9.00 € |
| Rugby | 3 | -5.00 € |
| Rugby à XV | 1 | +8.48 € |
| Tennis | 14 | +151.75 € |

### L_kelly_dynamique par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -20.08 € |
| 2026-10-11 | 17 | -7.25 € |
| 2026-10-12 | 3 | +2.09 € |
| 2026-10-13 | 6 | +57.27 € |
| 2026-10-14 | 1 | +0.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -3.94 € |
| Basketball | 1 | -3.65 € |
| Football | 15 | -64.38 € |
| Football Américain | 2 | -11.83 € |
| Formule 1 | 3 | -11.09 € |
| Hockey sur glace | 3 | -5.08 € |
| Rugby | 2 | +11.14 € |
| Rugby à XV | 1 | +8.14 € |
| Tennis | 15 | +112.72 € |

### M_modele_20 par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 8 | -11.60 € |
| 2026-10-11 | 9 | +110.97 € |
| 2026-10-12 | 2 | +23.15 € |
| 2026-10-13 | 6 | +135.00 € |
| 2026-10-14 | 1 | +0.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Basketball | 1 | -20.00 € |
| Football | 12 | -29.05 € |
| Formule 1 | 1 | -19.76 € |
| Hockey sur glace | 1 | -17.82 € |
| Tennis | 11 | +344.15 € |

## Sensibilité du modèle : les 9 variantes explorées

| EV estimée minimale | Mise maximale | Réglés | Gain net | ROI | Baisse maximale |
|---|---|---|---|---|---|
| 0 % | 5 € | 69 | -24.27 € | -7.1 % | -54.52 € |
| 0 % | 10 € | 47 | -47.96 € | -10.7 % | -88.52 € |
| 0 % | 20 € | 28 | +50.79 € | +10.0 % | -143.22 € |
| 5 % | 5 € | 54 | +10.50 € | +3.9 % | -52.25 € |
| 5 % | 10 € | 40 | +61.73 € | +16.0 % | -74.75 € |
| 5 % | 20 € | 26 | +257.52 € | +51.8 % | -85.88 € |
| 10 % | 5 € | 44 | +31.00 € | +14.1 % | -46.75 € |
| 10 % | 10 € | 33 | +78.25 € | +24.4 % | -79.75 € |
| 10 % | 20 € | 21 | +182.92 € | +46.2 % | -76.00 € |

## Classement exploratoire des 56 filtres

Ce classement a été trié après lecture de tous les résultats. Il sert à proposer des hypothèses, pas à valider une stratégie. Le meilleur filtre tennis repose sur très peu de paris.
| Filtre | Réglés | Gain net | ROI |
|---|---|---|---|
| sport:tennis:1.5-5 | 14 | +168.00 € | +120.0 % |
| sport:tennis:2-5 | 14 | +168.00 € | +120.0 % |
| sport:tennis:1.5-8 | 15 | +158.00 € | +105.3 % |
| sport:tennis:3-5 | 7 | +128.00 € | +182.9 % |
| sport:tennis:1.5-3.5 | 9 | +82.50 € | +91.7 % |
| sport:tennis:2-3.5 | 9 | +82.50 € | +91.7 % |
| sport:tennis:1.5-2.5 | 5 | +22.50 € | +45.0 % |
| sport:basketball:1.5-2.5 | 1 | +11.00 € | +110.0 % |
| sport:rugby:1.5-2.5 | 4 | +10.00 € | +25.0 % |
| sport:hockey sur glace:1.5-3.5 | 5 | +7.50 € | +15.0 % |
| sport:hockey sur glace:2-3.5 | 5 | +7.50 € | +15.0 % |
| sport:hockey sur glace:1.5-2.5 | 2 | +5.00 € | +25.0 % |
| sport:rugby:1.5-3.5 | 5 | +0.00 € | +0.0 % |
| sport:rugby:2-3.5 | 5 | +0.00 € | +0.0 % |
| bookmaker:Winamax:1.5-2.5 | 12 | -1.50 € | -1.2 % |
| sport:basketball:1.5-3.5 | 3 | -9.00 € | -30.0 % |
| sport:basketball:2-3.5 | 3 | -9.00 € | -30.0 % |
| sport:rugby:1.5-5 | 6 | -10.00 € | -16.7 % |
| sport:rugby:1.5-8 | 6 | -10.00 € | -16.7 % |
| sport:rugby:2-5 | 6 | -10.00 € | -16.7 % |
| bookmaker:Unibet:1.5-2.5 | 9 | -15.00 € | -16.7 % |
| tous:tous:1.5-2.5 | 21 | -16.50 € | -7.9 % |
| sport:rugby:3-5 | 2 | -20.00 € | -100.0 % |
| sport:basketball:1.5-5 | 5 | -29.00 € | -58.0 % |
| sport:basketball:1.5-8 | 5 | -29.00 € | -58.0 % |
| sport:basketball:2-5 | 5 | -29.00 € | -58.0 % |
| sport:hockey sur glace:1.5-5 | 9 | -32.50 € | -36.1 % |
| sport:hockey sur glace:2-5 | 9 | -32.50 € | -36.1 % |
| sport:hockey sur glace:3-5 | 7 | -37.50 € | -53.6 % |
| bookmaker:Unibet:3-5 | 4 | -40.00 € | -100.0 % |
| sport:basketball:3-5 | 4 | -40.00 € | -100.0 % |
| sport:hockey sur glace:1.5-8 | 10 | -42.50 € | -42.5 % |
| sport:football:1.5-2.5 | 7 | -45.00 € | -64.3 % |
| tous:tous:1.5-5 | 57 | -49.23 € | -9.2 % |
| tous:tous:2-5 | 57 | -49.23 € | -9.2 % |
| bookmaker:Unibet:1.5-3.5 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:1.5-5 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:1.5-8 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:2-3.5 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:2-5 | 18 | -53.00 € | -29.4 % |
| tous:tous:1.5-8 | 56 | -65.94 € | -12.4 % |
| sport:football:3-5 | 38 | -69.32 € | -18.7 % |
| bookmaker:Winamax:3-5 | 49 | -90.06 € | -19.0 % |
| bookmaker:Winamax:1.5-5 | 57 | -116.15 € | -21.2 % |
| bookmaker:Winamax:2-5 | 57 | -116.15 € | -21.2 % |
| bookmaker:Winamax:1.5-8 | 58 | -117.25 € | -21.3 % |
| tous:tous:3-5 | 48 | -119.83 € | -25.6 % |
| tous:tous:1.5-3.5 | 48 | -130.03 € | -27.9 % |
| tous:tous:2-3.5 | 48 | -130.03 € | -27.9 % |
| sport:football:1.5-3.5 | 36 | -142.74 € | -41.6 % |
| sport:football:2-3.5 | 36 | -142.74 € | -41.6 % |
| sport:football:1.5-5 | 41 | -146.93 € | -37.0 % |
| sport:football:1.5-8 | 41 | -146.93 € | -37.0 % |
| sport:football:2-5 | 41 | -146.93 € | -37.0 % |
| bookmaker:Winamax:1.5-3.5 | 46 | -189.07 € | -41.7 % |
| bookmaker:Winamax:2-3.5 | 46 | -189.07 € | -41.7 % |

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

Producteurs des 150 événements de règlement : {'gpt-6-luna': 150}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.
La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.

Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.
