# Recherche de stratégies — replay chronologique

Source initiale : branche donnees, commit `fb09dbd70b7d302838c1a107cc47e77db2a3bcdb` ; dernière observation du 2026-10-17T11:55:48+00:00.
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
| temoin_10 | 97 / 107 | 887.25 € | -47.40 € | -5.3 % | -167.12 € |
| temoin_20 | 59 / 66 | 953.05 € | +90.68 € | +9.5 % | -162.12 € |
| value_0 | 2 / 3 | 20.00 € | -20.00 € | -100.0 % | -20.00 € |
| value_5 | 1 / 2 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| J_adaptative | 43 / 45 | 414.14 € | +29.68 € | +7.2 % | -122.83 € |
| K_modele | 56 / 61 | 544.90 € | +150.73 € | +27.7 % | -74.75 € |
| L_kelly_dynamique | 59 / 64 | 369.17 € | +76.74 € | +20.8 % | -59.37 € |
| M_modele_20 | 40 / 45 | 758.57 € | +409.38 € | +54.0 % | -85.88 € |

Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.
M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.

## Stabilité et calibration

Sur 212 prévisions réglées : score de Brier du modèle 0.2112, prior bookmaker 0.2126 (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.

| Simulation | Dispersion ROI à 90 % par bootstrap de rencontres |
|---|---|
| J_adaptative | [-31.4, 47.2] |
| K_modele | [-8.3, 66.1] |
| L_kelly_dynamique | [-14.0, 58.3] |
| M_modele_20 | [9.4, 101.1] |
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
| 2026-10-16 | 5 | +69.50 € |

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
| 2026-10-16 | 5 | +26.40 € |

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
| 2026-10-16 | 4 | +140.61 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Basketball | 1 | -20.00 € |
| Football | 15 | +25.56 € |
| Formule 1 | 1 | -19.76 € |
| Hockey sur glace | 1 | -17.82 € |
| Rugby | 0 | +0.00 € |
| Tennis | 22 | +441.40 € |

## Sensibilité du modèle : les 9 variantes explorées

| EV estimée minimale | Mise maximale | Réglés | Gain net | ROI | Baisse maximale |
|---|---|---|---|---|---|
| 0 % | 5 € | 92 | +20.98 € | +4.6 % | -54.52 € |
| 0 % | 10 € | 69 | +59.59 € | +9.0 % | -92.44 € |
| 0 % | 20 € | 42 | +241.11 € | +31.8 % | -143.22 € |
| 5 % | 5 € | 70 | +55.00 € | +15.7 % | -52.25 € |
| 5 % | 10 € | 56 | +150.73 € | +27.7 % | -74.75 € |
| 5 % | 20 € | 40 | +409.38 € | +54.0 % | -85.88 € |
| 10 % | 5 € | 57 | +57.25 € | +20.1 % | -46.75 € |
| 10 % | 10 € | 46 | +130.75 € | +29.0 % | -79.75 € |
| 10 % | 20 € | 33 | +264.03 € | +42.6 % | -76.00 € |

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
| sport:rugby:1.5-3.5 | 12 | +16.00 € | +13.3 % |
| sport:rugby:2-3.5 | 12 | +16.00 € | +13.3 % |
| sport:rugby:1.5-2.5 | 4 | +10.00 € | +25.0 % |
| sport:rugby:1.5-5 | 13 | +6.00 € | +4.6 % |
| sport:rugby:1.5-8 | 13 | +6.00 € | +4.6 % |
| sport:rugby:2-5 | 13 | +6.00 € | +4.6 % |
| sport:hockey sur glace:1.5-2.5 | 2 | +5.00 € | +25.0 % |
| sport:basketball:1.5-2.5 | 2 | +1.00 € | +5.0 % |
| bookmaker:Winamax:1.5-2.5 | 24 | -1.50 € | -0.6 % |
| sport:hockey sur glace:1.5-3.5 | 12 | -5.50 € | -4.6 % |
| sport:hockey sur glace:2-3.5 | 12 | -5.50 € | -4.6 % |
| bookmaker:Unibet:1.5-3.5 | 31 | -17.00 € | -5.5 % |
| bookmaker:Unibet:2-3.5 | 31 | -17.00 € | -5.5 % |
| sport:rugby:3-5 | 5 | -17.50 € | -35.0 % |
| bookmaker:Unibet:1.5-2.5 | 12 | -22.50 € | -18.8 % |
| tous:tous:1.5-2.5 | 38 | -24.50 € | -6.4 % |
| bookmaker:Unibet:1.5-5 | 32 | -27.00 € | -8.4 % |
| bookmaker:Unibet:1.5-8 | 32 | -27.00 € | -8.4 % |
| bookmaker:Unibet:2-5 | 32 | -27.00 € | -8.4 % |
| sport:football:3-5 | 63 | -27.88 € | -4.5 % |
| sport:basketball:1.5-3.5 | 6 | -29.00 € | -48.3 % |
| sport:basketball:2-3.5 | 6 | -29.00 € | -48.3 % |
| sport:football:1.5-2.5 | 20 | -36.00 € | -18.0 % |
| sport:football:1.5-5 | 68 | -46.23 € | -7.0 % |
| sport:football:1.5-8 | 68 | -46.23 € | -7.0 % |
| sport:football:2-5 | 68 | -46.23 € | -7.0 % |
| sport:basketball:1.5-5 | 8 | -49.00 € | -61.3 % |
| sport:basketball:1.5-8 | 8 | -49.00 € | -61.3 % |
| sport:basketball:2-5 | 8 | -49.00 € | -61.3 % |
| sport:basketball:3-5 | 5 | -50.00 € | -100.0 % |
| bookmaker:Winamax:3-5 | 85 | -51.93 € | -6.4 % |
| tous:tous:2-5 | 97 | -56.17 € | -6.4 % |
| tous:tous:1.5-5 | 97 | -61.89 € | -7.0 % |
| bookmaker:Unibet:3-5 | 10 | -69.50 € | -69.5 % |
| tous:tous:1.5-8 | 94 | -77.73 € | -8.9 % |
| sport:hockey sur glace:1.5-5 | 23 | -79.50 € | -34.6 % |
| sport:hockey sur glace:2-5 | 23 | -79.50 € | -34.6 % |
| tous:tous:3-5 | 81 | -81.59 € | -10.4 % |
| sport:football:1.5-3.5 | 57 | -88.38 € | -16.2 % |
| sport:football:2-3.5 | 57 | -88.38 € | -16.2 % |
| sport:hockey sur glace:1.5-8 | 24 | -89.50 € | -37.3 % |
| sport:hockey sur glace:3-5 | 19 | -90.50 € | -47.6 % |
| bookmaker:Winamax:1.5-5 | 93 | -111.80 € | -12.5 % |
| bookmaker:Winamax:2-5 | 93 | -111.80 € | -12.5 % |
| bookmaker:Winamax:1.5-8 | 95 | -122.50 € | -13.6 % |
| tous:tous:2-3.5 | 83 | -139.20 € | -18.1 % |
| tous:tous:1.5-3.5 | 84 | -163.28 € | -21.2 % |
| bookmaker:Winamax:1.5-3.5 | 77 | -241.75 € | -32.8 % |
| bookmaker:Winamax:2-3.5 | 77 | -241.75 € | -32.8 % |

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

Producteurs des 254 événements de règlement : {'gpt-6-luna': 254}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.
La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.

Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.
