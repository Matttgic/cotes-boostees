# Cotes boostées

**Webapp : https://cotes-boostees-five.vercel.app/** — interface de consultation, reliée à la branche `donnees`. Documentation : [`SITE.md`](SITE.md).

Suivi des cotes boostées de **Winamax, Unibet, OlyBet, Genybet, NetBet et Betsson** (sites français ; PMU et bet365 non suivis) pour savoir si elles sont rentables.

Douze simulations en argent fictif : A, B1/B2, B/B0 et les challengers C–I.

- **A « Tout miser »** : chaque boost publié, **toujours à la mise max** (10, 20 ou 50 €), à la cote
  boostée vue au premier passage. Bilan dans **`BILAN.md`** sur la branche `donnees` ;
- **B « Filtrée »** : seulement les boosts à +5 % d'EV ou plus face à la cote juste Pinnacle (marge retirée).

### Sept hypothèses (C à I)

| Code | Règle prédéfinie | Limitation du risque |
|---|---|---|
| C | Tous les boosts | 10 € maximum par boost |
| D | Cote boostée initiale de 1,60 à 3,50 | 10 € maximum |
| E | Match commençant dans les 48 h de la première collecte, hors longue durée | 10 € maximum |
| F | EV **exacte ≥ 8 %** et cote du premier calcul EV ≤ 4 | 10 € maximum |
| G | EV **exacte ≥ 5 %**, prix du premier calcul, quart Kelly | Banque fictive fixe de 1 000 €, 1 % maximum/pari |
| H | Un seul boost par événement, celui observé en premier | 10 € maximum |
| I | Un seul boost par événement avec cote de 1,60 à 3,50 | 10 € maximum |

L'EV minimale existante est **+5 % (pas +50 %)**. Une hausse du prix de la cote
boostée (par rapport au prix d'origine) **n'est pas** une preuve d'EV positive.
A/B restent inchangées comme étalons. I a été choisie après analyse des résultats
historiques : son bilan passé est donc exploratoire et ne constitue pas une validation.
Son test prospectif séparé, comparé au témoin A sur les mêmes boosts, commence le
13 octobre 2026 à 20:20 UTC. Le ROI, le gain et la pire baisse doivent être comparés **sur les
mêmes périodes** et avec assez de paris hors échantillon. Les mises plafonnées
réduisent la perte maximale par pari mais n'améliorent pas mécaniquement le ROI.
Les stratégies EV F/G refusent une évaluation tardive ou approximative et
utilisent le prix noté au premier calcul (pas une ancienne cote possiblement disparue).
Kelly n'est pas fiable sans calibration et diversification ; c'est un **test fictif**.


## Cerveau — mode observation prospective (v0.1)

Le fichier public `cerveau.json` (branche `donnees`) contient un journal **horodaté avant match** :

- **Sélection fictive** : pari simple ou combiné de rencontres distinctes avec référence `exacte` recalculée lors du passage, EV ≥ +5 %, cote entre 1,60 et 5, départ dans les 72 h, mise maximale **confirmée**. Mise fictive plafonnée à 10 €.
- **Écarté** : marché exactement évalué mais EV insuffisante ou cote hors bornes.
- **Abstention** : marché absent, combiné, manque de mise, longue durée, cotation ou référence non exploitable. Ne pas transformer les absences en paris perdants.

Une sélection se **verrouille au premier instant** où tous les critères sont réunis. Les cotes et les mises ne sont jamais remplacées par celles vues après coup ; les changements ultérieurs forment un journal distinct. Le module regarde les résultats uniquement après la prise de décision et publie gains nets, ROI et pire baisse des paris fictifs réglés. Les boosts anciennement observés et déjà terminés ne sont pas backfillés comme des prédictions.

**Diagnostic des abstentions (v1.1).** Les paris de saison et événements hors des 72 h sont classés `hors_perimetre` plutôt qu'en abstention technique. Les refus sans cote juste distinguent désormais rencontre introuvable, marché ou ligne absent, sport non pris en charge et combiné lié. Un combiné de rencontres distinctes peut être sélectionné uniquement si son calcul est `exacte`, chaque rencontre est identifiable et l'EV passe le seuil ; un combiné corrélé reste une abstention. Les résultats du passé ne sont jamais transformés rétrospectivement en sélections. Pour éviter les fausses correspondances, un nom d'équipe manquant n'est complété que si l'autre nom coïncide avec un titre d'affiche explicite.

**Important : c'est un moteur à règles, PAS encore un modèle entraîné.** Les caractéristiques archivées avant match pourront alimenter un modèle statistique après validation d'un échantillon suffisant. Le moteur ne place aucun pari, n'expose aucun secret et n'ajoute aucun appel aux API. Les règlements automatiques peuvent être erronés : corrections manuelles prévues dans le collecteur.

⚠️ Simulation uniquement. Les paris sportifs comportent un risque de perte.
Jeu responsable : Joueurs Info Service, 09 74 75 13 13.

## Fonctionnement

Toutes les heures (workflow « Collecte des boosts », `scripts/collecte.py`). GitHub sautant souvent les
tâches planifiées, chaque passage relance le suivant une heure après son début ; la tâche planifiée ne
sert qu'à redémarrer la chaîne. Dépôt public = minutes gratuites ; si le dépôt devient privé, mettre la
variable `CHAINE` à `non`.

1. lecture de la page « Cotes boostées » des bookmakers via une **IP française** (proxy Bright Data,
   zone ISP) et l'**empreinte d'un vrai Chrome** (`curl_cffi`), sans quoi les sites renvoient 403 ;
2. extraction de chaque boost : match, sport, intitulé du pari, **cote d'origine**, **cote boostée**,
   **mise max**, heure du match ;
3. mise à jour de l'historique sur la branche **`donnees`** : `boosts.json` (un enregistrement par boost,
   jamais effacé, avec première/dernière apparition et changements de cote) et `etat.json`
   (dernier passage, consommation du proxy, 200 derniers passages).

4. règlement des boosts terminés (match commencé depuis 4 h ou plus) par une **IA avec recherche web**
   (`boosts/reglement.py`) : **ChatGPT** si le secret `OPENAI_API_KEY` est présent (gpt-6-luna aux deux
   premiers essais, puis gpt-6.1-sol), sinon Claude (`ANTHROPIC_API_KEY`) ; variable `REGLEMENT_MODELE`
   pour imposer un modèle :
   verdict gagné / perdu / remboursé avec score, explication et sources ; « inconnu » = nouvel essai 6 h
   plus tard, 4 essais au plus puis « à la main ». Corrections manuelles prioritaires dans
   `reglements_manuels.json` (`{"id du boost": "gagné"}`) ;
5. valeur face à Pinnacle (stratégie B, `boosts/evaluation.py`) : l'IA décompose chaque nouveau boost en
   conditions simples (`boosts/jambes.py`), chacune est cherchée telle quelle chez Pinnacle (API publique,
   `boosts/pinnacle.py` copié de cotes-value, gratuite, sans quota) et sa probabilité juste (marge
   retirée) donne la cote juste et l'EV (`boosts/valeur.py`). Si Pinnacle n'a pas la condition, elle est
   cherchée sur l'**échange Betfair via PulseScore** (milieu achat/vente, seulement si l'écart est serré
   et l'argent engagé suffisant ; requêtes PulseScore seulement dans ce cas). « exacte » : un pari ou des matchs différents ; « approx » : conditions
   liées sur un même match (produit des probabilités) ; « non évaluable » : une condition absente chez
   Pinnacle (jamais devinée) ;
   Équivalences exactes quand le marché direct manque : « X gagne » ≡ handicap -0,5 sur la période ;
   tennis « X gagne 2-1 » ≡ P(X gagne) − P(X -1,5 set). Ligne absente d'un total ≥ 10 : interpolée entre
   deux lignes en ,5 à 3 unités au plus (statut « interpolee », compté à part) ;
6. bilan : `bilan.json` et `BILAN.md` — A, B-exacte, B-approx et C à I (sept challengers).
   A reste ventilée par valeur, mise max, cote, sport, mois. Les 12 simulations sont visibles dans le site.

Si aucun bookmaker n'est lisible, le workflow passe au rouge (e-mail de GitHub).

| Bookmaker | État (8/10/2026) |
|---|---|
| Winamax | ✅ collecté (`boosts/winamax.py`) |
| PMU | ⛔ boosts visibles seulement une fois connecté (offre Kambi « pmusportsfr » publique, mais sans boosts) |
| Unibet | ✅ collecté (`boosts/unibet.py`) : page /cotes-boostees + page de chaque paquet de boosts, par la zone ISP (le Web Unlocker refuse les sites de jeux sans vérification d'identité ; l'offre Kambi « ub » est Unibet international, pas unibet.fr). Mise max lue dans l'intitulé (25 € par défaut). Paris de saison marqués « long terme » : pas de valeur Pinnacle, règlement à partir de 120 jours puis chaque semaine |
| OlyBet | ✅ collecté depuis le 13/10/2026 (`boosts/olybet.py`) : API « swarm » de BetConstruct (WebSocket) avec l'identifiant du site **olybet.fr** (offre française uniquement), sans proxy. Cote d'origine non publiée. Gain net plafonné à 25 € → mise max = 25 / (cote − 1). **Hors protocole gelé** (bilan propre dans « par bookmaker ») |
| Genybet, NetBet | ✅ collectés depuis le 13/10/2026 (`boosts/sportnco.py`) : plateforme Sportnco, page « Super Cotes » (/super-cotes) de **sport.genybet.fr** et **netbet.fr** par l'IP française ; état `window.__NUXT__` lu sans exécuter de JavaScript (`boosts/nuxt.py`). Mise max 10 € (constatée), cote d'origine non publiée. Hors protocole gelé |
| Betsson | ✅ collecté depuis le 13/10/2026 (`boosts/betsson.py`) : API de contenu de **betsson.fr** (cartes « Cotes Boostées » / Flash Boost), cote d'origine lue dans le marché normal du même match, mise max dans l'intitulé (« Max 20€ »). Betsson refuse une partie des IP du proxy (géolocalisées hors de France par sa base) : changement d'IP automatique, session gagnante gardée. Hors protocole gelé |
| bet365 | ⛔ non suivi : site lisible seulement dans un vrai navigateur (≈ 9 Mo par passage) et pas de cotes simples boostées sur la version française (seulement des combinés boostés) |

Étapes suivantes : PMU ; correction des combinés liés grâce aux cotes simples Winamax (PulseScore) ; alerte Telegram des boosts à +5 % d'EV.

## Protocole gelé (gel-1, 11/10/2026 22 h)

Pour ne pas « optimiser » sur le hasard des premiers résultats, quatre stratégies sont figées et jugées
**uniquement sur les boosts découverts après le gel** (`boosts/simulation.py`, `DATE_GEL`) :
Population : Winamax et Unibet uniquement (`BOOKMAKERS_GEL`). A (témoin), B (valeur ≥ +5 %, exacte ou interpolée, mise max), B0 (valeur ≥ 0 %), D (hypothèse : cotes
1,60–3,50, 10 € max, repérée en regardant les premiers résultats). Indicateur principal à court terme :
la **valeur moyenne jouée** (cote prise face à la cote juste), bien moins bruitée que le ROI.
I combine D (zone de cote modérée et mise plafonnée) et H (un pari par match). Comme cette règle vient
de la lecture des résultats passés, son archive ne prouve pas sa rentabilité ; son essai prospectif
séparé, contre A, démarre le 13/10/2026 à 20:20 UTC. Les autres stratégies restent calculées pour mémoire.
Diagnostic des boosts non évaluables :
`scripts/diagnostic_valeur.py` (workflow « Sonde des sources »).

## Sondes

Workflow « Sonde des sources » (lancé à la main) : `scripts/sonde.py` (PulseScore : pas de boosts ;
accès direct : 403), `sonde2.py` (empreinte Chrome : Winamax OK), `sonde3.py` (structure des boosts
Winamax). Résultats sur la branche `sonde`.

## Secrets

- `OPENAI_API_KEY` : clé de l'API OpenAI, pour le règlement automatique (ou `ANTHROPIC_API_KEY`).
- `PULSESCORE_KEY` : clé PulseScore (Settings → Secrets and variables → Actions).
- `BRIGHTDATA_CUSTOMER_ID`, `BRIGHTDATA_ZONE`, `BRIGHTDATA_PASSWORD` : zone proxy ISP Bright Data
  (sans vérification d'identité). Port 44445 (variable `BRIGHTDATA_PORT` pour le changer).
  Certificat du proxy dans `certs/`.

## Développement

```bash
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q
```

