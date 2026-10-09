# Interface « Cote Boostée / Le registre »

Site statique sans framework, sans backend supplémentaire, et sans clés secrètes côté navigateur.

## Source de données

Le navigateur lit trois fichiers **publics** issus de la branche `donnees` :

- `boosts.json` : historique, cotes, disponibilité à la dernière collecte, évaluations ;
- `bilan.json` : bilans et trajectoires simulés par le moteur Python ;
- `etat.json` : dernier passage, diagnostics des bookmakers.

Les données proviennent de `https://raw.githubusercontent.com/Matttgic/cotes-boostees/donnees/`.
Le chargement a lieu à l'ouverture, sur clic « Actualiser », et toutes les 5 minutes lorsque l'onglet est visible. La mise à jour dépend donc **aussi** de la cadence et du succès de la collecte GitHub Actions : ce n'est pas un flux de cotes en temps réel.

« Repérés au dernier scan » correspond aux boosts marqués disponibles, dont le début est dans le futur et dont la dernière observation est proche de la collecte la plus récente (tolérance 2 h 30). En cas de collecte ancienne (> 3 h), le site affiche un avertissement. Les anciennes offres ne sont jamais inventées ni présentées comme actuelles.

Les favoris sont enregistrés uniquement dans le navigateur via `localStorage`.

## Développement local

Dans le dépôt :

```bash
python -m http.server 8080
```

Puis ouvrir `http://localhost:8080/`. Aucun package ni compilation nécessaires.

## Publication

Le workflow `.github/workflows/pages.yml` publie automatiquement le site depuis `main` sur **GitHub Pages** à chaque modification de l'interface. Dans **Settings → Pages**, choisir **Build and deployment → Source: GitHub Actions** pour activer Pages si nécessaire. Adresse attendue après publication : `https://matttgic.github.io/cotes-boostees/` (à confirmer dans le workflow).

Alternativement, connecter ce dépôt à Vercel avec le répertoire racine `/` et le preset **Other**, sans build.

## Limites importantes

- L'EV « exacte » représente la méthode du moteur, pas une garantie de rentabilité ; les offres liées peuvent être des approximations.
- Le pourcentage de boost est une hausse de cote, pas une probabilité de gain.
- Les ROI affichés portent uniquement sur les paris fictifs déjà réglés et peuvent être très volatils.
- L'interface est en lecture seule : elle n'envoie pas de paris et ne modifie pas la collecte.
