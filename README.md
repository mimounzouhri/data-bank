Arbre de Décision pour les Données Bancaires
Ce projet implémente un modèle d'arbre de décision pour analyser les données bancaires et prédire si un client acceptera une offre basée sur plusieurs caractéristiques.

Prérequis
Assurez-vous d'avoir les bibliothèques suivantes installées dans votre environnement Python :

pandas : pour manipuler les données
matplotlib : pour visualiser l'arbre de décision
scikit-learn : pour créer le modèle d'arbre de décision
Installation des bibliothèques
Vous pouvez installer les dépendances nécessaires avec la commande suivante :

pip install pandas matplotlib scikit-learn
Fichier de données
Le fichier de données utilisé est bank-additional-full.csv, qui contient des informations provenant d'une campagne bancaire. Assurez-vous que ce fichier est dans le même répertoire que le script Python ou fournissez le chemin correct.

Contenu du Script
Le script effectue les étapes suivantes :

Chargement des données : Lecture du fichier CSV contenant les données bancaires.
Préparation des données :
Transformation de la colonne cible y en valeurs binaires (1 pour "yes", 0 pour "no").
Sélection des colonnes pertinentes comme variables explicatives.
Construction du modèle :
Division des données en ensembles d'entraînement et de test.
Création d'un modèle d'arbre de décision avec une profondeur maximale de 5.
Visualisation de l'arbre :
Affichage et sauvegarde de l'arbre de décision sous forme d'image (decision_tree_bank.jpg).
Exemple d'Exécution
Voici comment exécuter le script :

Placez le fichier bank-additional-full.csv dans le même répertoire que le script Python.
Lancez le script :
python main.py
Une fois le script terminé, l'arbre de décision sera affiché et enregistré sous forme d'image dans le fichier decision_tree_bank.jpg.
Résultat
L'image générée montre un arbre de décision interprétable qui aide à comprendre les facteurs influençant la réponse d'un client à une offre bancaire.

Auteurs
[ZOUHRI Mimoun]
Licence
Ce projet est sous licence libre. Vous êtes libre de le modifier et de le partager.