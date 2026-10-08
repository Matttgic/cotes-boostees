# Cotes boostées

Suivi des cotes boostées de **Winamax, Unibet et PMU** pour savoir si elles sont rentables.

Deux stratégies simulées en parallèle, en argent fictif, chaque boost misé à son plafond :

- **A « Tout miser »** : chaque boost publié, **toujours à la mise max** (10, 20 ou 50 €), à la cote
  boostée vue au premier passage. Bilan dans **`BILAN.md`** sur la branche `donnees` ;
- **B « Filtrée »** : seulement les boosts à +5 % d'EV ou plus face à la cote juste Pinnacle (marge retirée).

⚠️ Simulation uniquement. Les paris sportifs comportent un risque de perte.
Jeu responsable : Joueurs Info Service, 09 74 75 13 13.

## Fonctionnement

Toutes les heures (workflow « Collecte des boosts », `scripts/collecte.py`) :

1. lecture de la page « Cotes boostées » des bookmakers via une **IP française** (proxy Bright Data,
   zone ISP) et l'**empreinte d'un vrai Chrome** (`curl_cffi`), sans quoi les sites renvoient 403 ;
2. extraction de chaque boost : match, sport, intitulé du pari, **cote d'origine**, **cote boostée**,
   **mise max**, heure du match ;
3. mise à jour de l'historique sur la branche **`donnees`** : `boosts.json` (un enregistrement par boost,
   jamais effacé, avec première/dernière apparition et changements de cote) et `etat.json`
   (dernier passage, consommation du proxy, 200 derniers passages).

4. règlement des boosts terminés (match commencé depuis 4 h ou plus) par **Claude avec recherche web**
   (`boosts/reglement.py`, secret `ANTHROPIC_API_KEY`, modèle réglable par la variable `REGLEMENT_MODELE`) :
   verdict gagné / perdu / remboursé avec score, explication et sources ; « inconnu » = nouvel essai 6 h
   plus tard, 4 essais au plus puis « à la main ». Corrections manuelles prioritaires dans
   `reglements_manuels.json` (`{"id du boost": "gagné"}`) ;
5. bilan de la stratégie A : `bilan.json` et `BILAN.md` (gain net, ROI, par mise max, cote, sport, mois).

Si aucun bookmaker n'est lisible, le workflow passe au rouge (e-mail de GitHub).

| Bookmaker | État (8/10/2026) |
|---|---|
| Winamax | ✅ collecté (`boosts/winamax.py`) |
| PMU | 🔍 accessible depuis l'IP française, source des données à trouver |
| Unibet | ⛔ protégé par DataDome (défi JavaScript) : nécessiterait le Web Unlocker de Bright Data |

Étapes suivantes : PMU, cote juste Pinnacle (stratégie B), règlement des paris, simulations A et B.

## Sondes

Workflow « Sonde des sources » (lancé à la main) : `scripts/sonde.py` (PulseScore : pas de boosts ;
accès direct : 403), `sonde2.py` (empreinte Chrome : Winamax OK), `sonde3.py` (structure des boosts
Winamax). Résultats sur la branche `sonde`.

## Secrets

- `ANTHROPIC_API_KEY` : clé de l'API Anthropic (console Claude), pour le règlement automatique.
- `PULSESCORE_KEY` : clé PulseScore (Settings → Secrets and variables → Actions).
- `BRIGHTDATA_CUSTOMER_ID`, `BRIGHTDATA_ZONE`, `BRIGHTDATA_PASSWORD` : zone proxy ISP Bright Data
  (sans vérification d'identité). Port 44445 (variable `BRIGHTDATA_PORT` pour le changer).
  Certificat du proxy dans `certs/`.

## Développement

```bash
pip install -r requirements.txt -r requirements-dev.txt
python -m pytest -q
```
