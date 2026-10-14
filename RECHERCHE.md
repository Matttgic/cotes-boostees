# Recherche de stratégies — replay chronologique

Source initiale : branche donnees, commit `fb09dbd70b7d302838c1a107cc47e77db2a3bcdb` ; dernière observation du 2026-10-14T00:45:46+00:00.
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
| temoin_10 | 53 / 58 | 504.01 € | -46.94 € | -9.3 % | -107.52 € |
| temoin_20 | 29 / 35 | 519.06 € | +26.31 € | +5.1 % | -161.00 € |
| value_0 | 1 / 1 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| value_5 | 1 / 1 | 10.00 € | -10.00 € | -100.0 % | -10.00 € |
| J_adaptative | 29 / 32 | 281.24 € | -68.10 € | -24.2 % | -122.83 € |
| K_modele | 37 / 42 | 354.90 € | +31.73 € | +8.9 % | -74.75 € |
| L_kelly_dynamique | 40 / 45 | 234.53 € | +7.25 € | +3.1 % | -59.37 € |
| M_modele_20 | 23 / 28 | 436.95 € | +197.52 € | +45.2 % | -85.88 € |

Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.
M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.

## Stabilité et calibration

Sur 104 prévisions réglées : score de Brier du modèle 0.1986, prior bookmaker 0.2004 (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.

| Simulation | Dispersion ROI à 90 % par bootstrap de rencontres |
|---|---|
| J_adaptative | [-62.8, 17.3] |
| K_modele | [-34.4, 53.5] |
| L_kelly_dynamique | [-37.5, 46.7] |
| M_modele_20 | [-10.1, 106.9] |
Ces intervalles décrivent la dispersion des paris déjà sélectionnés ; ils ne corrigent pas la sélection a posteriori des méthodes et ne simulent pas un nouvel apprentissage complet.

### J_adaptative par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 14 | -28.27 € |
| 2026-10-11 | 12 | -82.06 € |
| 2026-10-13 | 3 | +42.23 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Football | 19 | -119.44 € |
| Football Américain | 1 | -9.05 € |
| Formule 1 | 1 | -10.00 € |
| Hockey sur glace | 1 | -9.52 € |
| Rugby | 2 | +5.00 € |
| Tennis | 5 | +74.91 € |

### K_modele par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -32.25 € |
| 2026-10-11 | 14 | +23.98 € |
| 2026-10-12 | 3 | +2.50 € |
| 2026-10-13 | 4 | +37.50 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -10.00 € |
| Basketball | 1 | -10.00 € |
| Football | 14 | -14.50 € |
| Football Américain | 1 | -10.00 € |
| Formule 1 | 3 | -30.00 € |
| Hockey sur glace | 1 | -9.00 € |
| Rugby | 3 | -5.00 € |
| Rugby à XV | 1 | +8.48 € |
| Tennis | 12 | +111.75 € |

### L_kelly_dynamique par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 16 | -20.08 € |
| 2026-10-11 | 17 | -7.25 € |
| 2026-10-12 | 3 | +2.09 € |
| 2026-10-13 | 4 | +32.49 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Baseball | 1 | -3.94 € |
| Basketball | 1 | -3.65 € |
| Football | 14 | -62.20 € |
| Football Américain | 2 | -11.83 € |
| Formule 1 | 3 | -11.09 € |
| Hockey sur glace | 3 | -5.08 € |
| Rugby | 2 | +11.14 € |
| Rugby à XV | 1 | +8.14 € |
| Tennis | 13 | +85.76 € |

### M_modele_20 par jour de décision

| Jour | Réglés | Gain net |
|---|---|---|
| 2026-10-10 | 8 | -11.60 € |
| 2026-10-11 | 9 | +110.97 € |
| 2026-10-12 | 2 | +23.15 € |
| 2026-10-13 | 4 | +75.00 € |

| Sport | Réglés | Gain net |
|---|---|---|
| Basketball | 1 | -20.00 € |
| Football | 11 | -9.05 € |
| Formule 1 | 1 | -19.76 € |
| Hockey sur glace | 1 | -17.82 € |
| Tennis | 9 | +264.15 € |

## Sensibilité du modèle : les 9 variantes explorées

| EV estimée minimale | Mise maximale | Réglés | Gain net | ROI | Baisse maximale |
|---|---|---|---|---|---|
| 0 % | 5 € | 64 | -29.27 € | -9.3 % | -54.52 € |
| 0 % | 10 € | 44 | -35.52 € | -8.3 % | -88.52 € |
| 0 % | 20 € | 26 | +70.79 € | +15.2 % | -143.22 € |
| 5 % | 5 € | 51 | -4.50 € | -1.8 % | -52.25 € |
| 5 % | 10 € | 37 | +31.73 € | +8.9 % | -74.75 € |
| 5 % | 20 € | 23 | +197.52 € | +45.2 % | -85.88 € |
| 10 % | 5 € | 42 | +11.00 € | +5.3 % | -46.75 € |
| 10 % | 10 € | 31 | +38.25 € | +12.7 % | -79.75 € |
| 10 % | 20 € | 19 | +102.92 € | +28.9 % | -76.00 € |

## Classement exploratoire des 56 filtres

Ce classement a été trié après lecture de tous les résultats. Il sert à proposer des hypothèses, pas à valider une stratégie. Le meilleur filtre tennis repose sur très peu de paris.
| Filtre | Réglés | Gain net | ROI |
|---|---|---|---|
| sport:tennis:1.5-5 | 12 | +128.00 € | +106.7 % |
| sport:tennis:2-5 | 12 | +128.00 € | +106.7 % |
| sport:tennis:1.5-8 | 13 | +118.00 € | +90.8 % |
| sport:tennis:3-5 | 6 | +88.00 € | +146.7 % |
| sport:tennis:1.5-3.5 | 8 | +82.50 € | +103.1 % |
| sport:tennis:2-3.5 | 8 | +82.50 € | +103.1 % |
| sport:tennis:1.5-2.5 | 5 | +22.50 € | +45.0 % |
| sport:basketball:1.5-2.5 | 1 | +11.00 € | +110.0 % |
| sport:rugby:1.5-2.5 | 4 | +10.00 € | +25.0 % |
| sport:rugby:1.5-3.5 | 5 | +0.00 € | +0.0 % |
| sport:rugby:2-3.5 | 5 | +0.00 € | +0.0 % |
| sport:hockey sur glace:1.5-3.5 | 4 | -7.50 € | -18.8 % |
| sport:hockey sur glace:2-3.5 | 4 | -7.50 € | -18.8 % |
| sport:basketball:1.5-3.5 | 3 | -9.00 € | -30.0 % |
| sport:basketball:2-3.5 | 3 | -9.00 € | -30.0 % |
| sport:hockey sur glace:1.5-2.5 | 1 | -10.00 € | -100.0 % |
| sport:rugby:1.5-5 | 6 | -10.00 € | -16.7 % |
| sport:rugby:1.5-8 | 6 | -10.00 € | -16.7 % |
| sport:rugby:2-5 | 6 | -10.00 € | -16.7 % |
| bookmaker:Unibet:1.5-2.5 | 9 | -15.00 € | -16.7 % |
| bookmaker:Winamax:1.5-2.5 | 11 | -16.50 € | -15.0 % |
| sport:rugby:3-5 | 2 | -20.00 € | -100.0 % |
| sport:basketball:1.5-5 | 5 | -29.00 € | -58.0 % |
| sport:basketball:1.5-8 | 5 | -29.00 € | -58.0 % |
| sport:basketball:2-5 | 5 | -29.00 € | -58.0 % |
| tous:tous:1.5-5 | 54 | -30.23 € | -6.0 % |
| tous:tous:2-5 | 54 | -30.23 € | -6.0 % |
| tous:tous:1.5-2.5 | 20 | -31.50 € | -15.8 % |
| sport:hockey sur glace:3-5 | 7 | -37.50 € | -53.6 % |
| bookmaker:Unibet:3-5 | 4 | -40.00 € | -100.0 % |
| sport:basketball:3-5 | 4 | -40.00 € | -100.0 % |
| sport:football:1.5-2.5 | 7 | -45.00 € | -64.3 % |
| tous:tous:1.5-8 | 53 | -46.94 € | -9.3 % |
| sport:hockey sur glace:1.5-5 | 8 | -47.50 € | -59.4 % |
| sport:hockey sur glace:2-5 | 8 | -47.50 € | -59.4 % |
| bookmaker:Unibet:1.5-3.5 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:1.5-5 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:1.5-8 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:2-3.5 | 18 | -53.00 € | -29.4 % |
| bookmaker:Unibet:2-5 | 18 | -53.00 € | -29.4 % |
| sport:hockey sur glace:1.5-8 | 9 | -57.50 € | -63.9 % |
| sport:football:3-5 | 37 | -59.32 € | -16.4 % |
| bookmaker:Winamax:3-5 | 47 | -78.06 € | -16.9 % |
| bookmaker:Winamax:1.5-5 | 53 | -86.15 € | -16.9 % |
| bookmaker:Winamax:2-5 | 53 | -86.15 € | -16.9 % |
| bookmaker:Winamax:1.5-8 | 54 | -87.25 € | -17.1 % |
| tous:tous:3-5 | 47 | -109.83 € | -23.9 % |
| tous:tous:1.5-3.5 | 46 | -121.03 € | -27.0 % |
| tous:tous:2-3.5 | 46 | -121.03 € | -27.0 % |
| sport:football:1.5-5 | 40 | -136.93 € | -35.4 % |
| sport:football:1.5-8 | 40 | -136.93 € | -35.4 % |
| sport:football:2-5 | 40 | -136.93 € | -35.4 % |
| sport:football:1.5-3.5 | 35 | -139.72 € | -41.0 % |
| sport:football:2-3.5 | 35 | -139.72 € | -41.0 % |
| bookmaker:Winamax:1.5-3.5 | 43 | -169.07 € | -40.0 % |
| bookmaker:Winamax:2-3.5 | 43 | -169.07 € | -40.0 % |

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

Producteurs des 142 événements de règlement : {'gpt-6-luna': 142}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.
La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.

Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.
