# Cotes boostées

**Webapp : https://cotes-boostees-five.vercel.app/** — interface de consultation, reliée à la branche `donnees`. Documentation : [`SITE.md`](SITE.md).

Suivi des cotes boostées de **Winamax, Unibet et PMU** pour savoir si elles sont rentables.

Neuf variantes de simulation en parallèle, en argent fictif : trois originales A/B1/B2 et six challengers C–H.

- **A « Tout miser »** : chaque boost publié, **toujours à la mise max** (10, 20 ou 50 €), à la cote
  boostée vue au premier passage. Bilan dans **`BILAN.md`** sur la branche `donnees` ;
- **B « Filtrée »** : seulement les boosts à +5 % d'EV ou plus face à la cote juste Pinnacle (marge retirée).

### Six nouvelles hypothèses (C à H)

| Code | Règle prédéfinie | Limitation du risque |
|---|---|---|
| C | Tous les boosts | 10 € maximum par boost |
| D | Cote boostée initiale de 1,60 à 3,50 | 10 € maximum |
| E | Match commençant dans les 48 h de la première collecte, hors longue durée | 10 € maximum |
| F | EV **exacte ≥ 8 %** et cote du premier calcul EV ≤ 4 | 10 € maximum |
| G | EV **exacte ≥ 5 %**, prix du premier calcul, quart Kelly | Banque fictive fixe de 1 000 €, 1 % maximum/pari |
| H | Un seul boost par événement, celui observé en premier | 10 € maximum |

L'EV minimale existante est **+5 % (pas +50 %)**. Une hausse du prix de la cote
boostée (par rapport au prix d'origine) **n'est pas** une preuve d'EV positive.
A/B restent inchangées comme étalons. Les autres hypothèses sont exploratoires :
pas d'optimisation a posteriori des seuils avec 13 paris seulement réglés
au 9 octobre 2026. Le ROI, le gain et la pire baisse doivent être comparés **sur les
mêmes périodes** et avec assez de paris hors échantillon. Les mises plafonnées
réduisent la perte maximale par pari mais n'améliorent pas mécaniquement le ROI.
Les stratégies EV F/G refusent une évaluation tardive ou approximative et
utilisent le prix noté au premier calcul (pas une ancienne cote possiblement disparue).
Kelly n'est pas fiable sans calibration et diversification ; c'est un **test fictif**.


## Cerveau — mode observation prospective (v0.1)

Le fichier public `cerveau.json` (branche `donnees`) contient un journal **horodaté avant match** :

- **Sélection fictive** : uniquement pari simple et référence `exacte` recalculée lors du passage, EV ≥ +5 %, cote entre 1,60 et 5, départ dans les 72 h, mise maximale **confirmée**. Mise fictive plafonnée à 10 €.
- **Écarté** : marché exactement évalué mais EV insuffisante ou cote hors bornes.
- **Abstention** : marché absent, combiné, manque de mise, longue durée, cotation ou référence non exploitable. Ne pas transformer les absences en paris perdants.

Une sélection se **verrouille au premier instant** où tous les critères sont réunis. Les cotes et les mises ne sont jamais remplacées par celles vues après coup ; les changements ultérieurs forment un journal distinct. Le module regarde les résultats uniquement après la prise de décision et publie gains nets, ROI et pire baisse des paris fictifs réglés. Les boosts anciennement observés et déjà terminés ne sont pas backfillés comme des prédictions.

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
6. bilan : `bilan.json` et `BILAN.md` — A, B-exacte, B-approx et C à H (six nouvelles variantes).
   A reste ventilée par valeur, mise max, cote, sport, mois. Les 9 simulations sont visibles dans le site.

Si aucun bookmaker n'est lisible, le workflow passe au rouge (e-mail de GitHub).

| Bookmaker | État (8/10/2026) |
|---|---|
| Winamax | ✅ collecté (`boosts/winamax.py`) |
| PMU | ⛔ boosts visibles seulement une fois connecté (offre Kambi « pmusportsfr » publique, mais sans boosts) |
| Unibet | ✅ collecté (`boosts/unibet.py`) : page /cotes-boostees + page de chaque paquet de boosts, par la zone ISP (le Web Unlocker refuse les sites de jeux sans vérification d'identité ; l'offre Kambi « ub » est Unibet international, pas unibet.fr). Mise max lue dans l'intitulé (25 € par défaut). Paris de saison marqués « long terme » : pas de valeur Pinnacle, règlement à partir de 120 jours puis chaque semaine |

Étapes suivantes : PMU ; correction des combinés liés grâce aux cotes simples Winamax (PulseScore) ; alerte Telegram des boosts à +5 % d'EV.

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
