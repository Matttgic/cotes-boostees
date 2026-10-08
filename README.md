# Cotes boostées

Suivi des cotes boostées de **Winamax, Unibet et PMU** pour savoir si elles sont rentables.

Deux stratégies simulées en parallèle, en argent fictif, chaque boost misé à son plafond :

- **A « Tout miser »** : chaque boost publié ;
- **B « Filtrée »** : seulement les boosts à +5 % d'EV ou plus face à la cote juste Pinnacle (marge retirée).

⚠️ Simulation uniquement. Les paris sportifs comportent un risque de perte.
Jeu responsable : Joueurs Info Service, 09 74 75 13 13.

## État

Étape 0 : **sonde des sources** (workflow « Sonde des sources », lancé à la main).
Elle vérifie si PulseScore fournit les boosts et si les sites des bookmakers répondent depuis
les serveurs GitHub. Résultats sur la branche `sonde` (`resume.json`).

## Secrets

- `PULSESCORE_KEY` : clé PulseScore (Settings → Secrets and variables → Actions).
- `BRIGHTDATA_CUSTOMER_ID`, `BRIGHTDATA_ZONE`, `BRIGHTDATA_PASSWORD` : zone proxy (ISP, sans vérification d’identité)
  Bright Data. Les sites des bookmakers refusent les serveurs GitHub (403, IP américaines) :
  on passe par une IP française (`-country-fr`). Certificat du proxy dans `certs/`.
