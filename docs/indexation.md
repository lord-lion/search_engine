# Système d'Indexation de Documents

Ce projet implémente un système simple d'indexation de documents textuels en Python. Il lit des fichiers textes, découpe le texte en mots, et construit un index permettant de retrouver rapidement dans quels documents chaque mot apparaît.

## Fonctionnalités

- **Lecture de fichiers** : Lit le contenu des fichiers textuels.
- **Découpage en mots** : Découpe le texte des documents en mots individuels.
- **Indexation** : Construit un index associant chaque mot aux documents dans lesquels il apparaît.
- **Affichage d'informations** : Affiche des informations sur l'index, comme la taille du vocabulaire et un échantillon des mots indexés.
- **Recherche de documents** : Permet de rechercher quels documents contiennent certains mots d'intérêt.
- **Sérialisation** : Sauvegarde l'index construit au format JSON dans un dossier spécifié.

## Comment ça marche ?

Le script `indexation.py` contient plusieurs fonctions dédiées à chaque étape du processus d'indexation :

1. `lire_fichier(chemin)`: Lit et retourne le contenu d'un fichier texte.
2. `decouper_mots(texte)`: Découpe un texte en mots.
3. `ajouter_mot_a_index(mot, chemin, index)`: Ajoute un mot et le chemin du document à l'index.
4. `construire_index(chemin_pattern, index)`: Construit l'index en lisant et en indexant les documents spécifiés.
5. `afficher_infos_index(index)`: Affiche des informations sur l'index construit.
6. `afficher_documents_mots(mots_interessants, index)`: Affiche les documents contenant certains mots.
7. `serialiser_index(index, nom_fichier)`: Sauvegarde l'index au format JSON.

## Utilisation

Pour utiliser ce script, assurez-vous d'avoir Python installé sur votre machine. Placez vos documents textuels dans un dossier et ajustez le chemin dans l'appel de la fonction `construire_index` pour pointer vers vos fichiers.

```python
index = {}
construire_index("./dataset/fr/*", index)
afficher_infos_index(index)
afficher_documents_mots(["exemple", "test", "python"], index)
serialiser_index(index, "index.json")
```
