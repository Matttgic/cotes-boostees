# Interface « Cote Boostée / Le registre »

Site statique sans framework, sans backend supplémentaire, et sans clés secrètes côté navigateur.

## Source de données

Le navigateur lit quatre fichiers **publics** issus de la branche `donnees` :

- `boosts.json` : historique, cotes, disponibilité à la dernière collecte, évaluations ;
- `bilan.json` : bilans et trajectoires simulés par le moteur Python ;
- `etat.json` : dernier passage, diagnostics des bookmakers ;
- `cerveau.json` : signaux prospectifs, abstentions, historiques de décision pré-match et bilans fictifs. Le fichier est facultatif tant que la première collecte ne l'a pas créé.

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

La version publique est déployée sur **Vercel** : https://cotes-boostees-five.vercel.app/

Le projet `cotes-boostees` est connecté au dépôt GitHub. La branche `main` est la branche de production. Framework **Other** (site HTML/CSS/JavaScript, sans build). Toute mise à jour de l'interface poussée sur `main` peut déclencher un nouveau déploiement Vercel. Aucun secret du collecteur n'est utilisé côté navigateur.

## Limites importantes

- L'EV « exacte » représente la méthode du moteur, pas une garantie de rentabilité ; les offres liées peuvent être des approximations.
- Le pourcentage de boost est une hausse de cote, pas une probabilité de gain.
- Les ROI affichés portent uniquement sur les paris fictifs déjà réglés et peuvent être très volatils.
- L'interface est en lecture seule : elle n'envoie pas de paris et ne modifie pas la collecte.

## Cerveau v0.1

L'onglet « Le cerveau » lit **seulement** `cerveau.json` et refuse d'afficher des recommandations inventées si ce fichier manque. Filtrage par sélection fictive / écarté / abstention, explications documentées, prix au moment de la première sélection et performance de sélection historique. Les cartes ne sont pas des recommandations de jouer.

La sélection et la journalisation ont lieu côté Python dans `boosts/cerveau.py` **après collecte et évaluation, mais avant règlement**. Les instantanés figent les informations disponibles à ce moment, avec date et version de protocole, et excluent les matchs déjà commencés. Le fichier est archivé automatiquement sur la branche `donnees`. Aucun entraînement n'est activé et rien n'est optimisé sur les gains du passé.

## Comprendre les abstentions (v1.1)

Le laboratoire sépare :
- **Hors champ** : offres long terme, date non identifiable ou match hors des 72 h ; ce ne sont pas des rejets pour manque d'EV ;
- **Abstention** : aucune probabilité de référence exploitable, combiné lié, équipe introuvable ou mise maximale inconnue ;
- **Écarté** : référence exacte disponible mais EV insuffisante ou cote hors des bornes du protocole ;
- **Sélection fictive** : référence exacte et actualisée, EV ≥ 5 % et mise fictive plafonnée.

Le détail des raisons est enregistré sous `motif_code`, `raisons`, `reference_raison` et agrégé dans `bilan.motifs_courants`. Les anciens instantanés restent inchangés, et leur `motif_code` absent figure comme `ancien_format` jusqu'à une nouvelle observation pré-match. Le cerveau peut maintenant traiter plusieurs jambes sur des rencontres **distinctes** avec EV calculée exactement, mais les combinés liés et les marchés non cotés restent sans signal.

L'amélioration des correspondances n'élargit pas les seuils de similarité des noms. Un nom manquant est rempli uniquement quand l'autre équipe correspond à l'affiche explicite « domicile - extérieur », sinon l'offre reste non évaluable.
