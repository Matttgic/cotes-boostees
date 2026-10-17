# Recherche de stratégies — replay chronologique

Source initiale : branche donnees, commit `fb09dbd70b7d302838c1a107cc47e77db2a3bcdb` ; dernière observation du 2026-10-17T22:42:50+00:00.
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
| temoin_10 | 104 / 112 | 950.91 € | -49.56 € | -5.2 % | -167.12 € |
| temoin_20 | 64 / 68 | 1032.11 € | +134.62 € | +13.0 % | -162.12 € |
| value_0 | 3 / 3 | 30.00 € | -30.00 € | -100.0 % | -30.00 € |
| value_5 | 2 / 2 | 20.00 € | -20.00 € | -100.0 % | -20.00 € |
| J_adaptative | 44 / 45 | 424.43 € | +19.39 € | +4.6 % | -122.83 € |
| K_modele | 59 / 65 | 574.90 € | +120.73 € | +21.0 % | -74.75 € |
| L_kelly_dynamique | 62 / 67 | 406.85 € | +39.06 € | +9.6 % | -59.37 € |
| M_modele_20 | 43 / 49 | 818.57 € | +349.38 € | +42.7 % | -85.88 € |

Les témoins à 10 € et 20 € ont la même bankroll, la même période et les mêmes plafonds d'exposition. Leur population diffère des anciennes stratégies A–I qui couvrent tout l'historique.
M n'est pas un simple doublement de K : l'exposition limite le nombre de paris simultanés et change donc aussi les paris effectivement pris.

## Stabilité et calibration

Sur 233 prévisions réglées : score de Brier du modèle 0.2112, prior bookmaker 0.2129 (plus bas est meilleur). Un gain positif sur les paris sélectionnés ne suffit pas à prouver une meilleure calibration générale.

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
| 0 % | 5 € | 99 | -14.02 € | -2.9 % | -54.52 € |
| 0 % | 10 € | 76 | -6.26 € | -0.9 % | -92.44 € |
| 0 % | 20 € | 48 | +121.11 € | +13.8 % | -143.22 € |
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
| sport:football:3-5 | 69 | +27.12 € | +4.0 % |
| sport:tennis:1.5-2.5 | 6 | +12.50 € | +20.8 % |
| sport:hockey sur glace:1.5-2.5 | 2 | +5.00 € | +25.0 % |
| sport:basketball:1.5-2.5 | 2 | +1.00 € | +5.0 % |
| sport:hockey sur glace:1.5-3.5 | 12 | -5.50 € | -4.6 % |
| sport:hockey sur glace:2-3.5 | 12 | -5.50 € | -4.6 % |
| sport:football:1.5-5 | 75 | -9.73 € | -1.3 % |
| sport:football:2-5 | 75 | -9.73 € | -1.3 % |
| sport:rugby:1.5-3.5 | 15 | -14.00 € | -9.3 % |
| sport:rugby:2-3.5 | 15 | -14.00 € | -9.3 % |
| bookmaker:Unibet:1.5-3.5 | 37 | -15.50 € | -4.2 % |
| bookmaker:Unibet:2-3.5 | 37 | -15.50 € | -4.2 % |
| sport:rugby:3-5 | 5 | -17.50 € | -35.0 % |
| sport:football:1.5-8 | 76 | -19.73 € | -2.7 % |
| sport:rugby:1.5-2.5 | 7 | -20.00 € | -28.6 % |
| sport:rugby:1.5-5 | 16 | -24.00 € | -15.0 % |
| sport:rugby:1.5-8 | 16 | -24.00 € | -15.0 % |
| sport:rugby:2-5 | 16 | -24.00 € | -15.0 % |
| bookmaker:Unibet:1.5-5 | 38 | -25.50 € | -6.7 % |
| bookmaker:Unibet:1.5-8 | 38 | -25.50 € | -6.7 % |
| bookmaker:Unibet:2-5 | 38 | -25.50 € | -6.7 % |
| sport:basketball:1.5-3.5 | 6 | -29.00 € | -48.3 % |
| sport:basketball:2-3.5 | 6 | -29.00 € | -48.3 % |
| bookmaker:Winamax:1.5-2.5 | 27 | -31.50 € | -11.7 % |
| bookmaker:Unibet:1.5-2.5 | 14 | -42.50 € | -30.4 % |
| bookmaker:Unibet:3-5 | 11 | -44.50 € | -40.5 % |
| bookmaker:Winamax:3-5 | 89 | -46.93 € | -5.5 % |
| sport:basketball:1.5-5 | 8 | -49.00 € | -61.3 % |
| sport:basketball:1.5-8 | 8 | -49.00 € | -61.3 % |
| sport:basketball:2-5 | 8 | -49.00 € | -61.3 % |
| sport:basketball:3-5 | 5 | -50.00 € | -100.0 % |
| tous:tous:3-5 | 86 | -50.43 € | -6.1 % |
| sport:football:1.5-2.5 | 22 | -56.00 € | -25.5 % |
| sport:football:1.5-3.5 | 64 | -56.53 € | -9.3 % |
| sport:football:2-3.5 | 64 | -56.53 € | -9.3 % |
| tous:tous:2-5 | 104 | -57.45 € | -6.1 % |
| tous:tous:1.5-5 | 104 | -62.60 € | -6.6 % |
| tous:tous:1.5-8 | 100 | -76.23 € | -8.2 % |
| sport:hockey sur glace:1.5-5 | 23 | -79.50 € | -34.6 % |
| sport:hockey sur glace:2-5 | 23 | -79.50 € | -34.6 % |
| sport:hockey sur glace:3-5 | 19 | -90.50 € | -47.6 % |
| tous:tous:1.5-2.5 | 45 | -94.50 € | -21.0 % |
| sport:hockey sur glace:1.5-8 | 25 | -99.50 € | -39.8 % |
| bookmaker:Winamax:1.5-5 | 99 | -126.40 € | -13.3 % |
| bookmaker:Winamax:2-5 | 99 | -126.40 € | -13.3 % |
| tous:tous:2-3.5 | 89 | -132.18 € | -16.0 % |
| bookmaker:Winamax:1.5-8 | 103 | -153.25 € | -15.7 % |
| tous:tous:1.5-3.5 | 90 | -153.85 € | -18.7 % |
| bookmaker:Winamax:1.5-3.5 | 81 | -280.75 € | -36.2 % |
| bookmaker:Winamax:2-3.5 | 81 | -280.75 € | -36.2 % |

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

Producteurs des 275 événements de règlement : {'gpt-6-luna': 275}. Ils ne sont pas audités ici contre des résultats officiels. Toute performance est conditionnelle à leur exactitude.
La même petite période a déjà été examinée pour définir ces méthodes. Le replay respecte la disponibilité des informations, mais n'est pas un échantillon indépendant de la conception du protocole.

Reproduction : `python scripts/analyser_strategies.py --sortie analyses`. Les tests de temporalité sont dans `tests/test_recherche_strategies.py`.
