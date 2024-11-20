# Importer les bibliothèques nécessaires
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split

# Charger les données depuis le fichier CSV
data = pd.read_csv('bank-additional-full.csv', sep=';')  # Spécifier le séparateur correct
print(data.head())  # Vérifiez les premières lignes des données

# Convertir la colonne cible 'y' en valeurs binaires
data['y'] = data['y'].map({'yes': 1, 'no': 0})  # 1 pour 'yes', 0 pour 'no'

# Préparer les variables explicatives et la cible
X = data[['age', 'campaign', 'previous', 'emp.var.rate', 'cons.price.idx', 'cons.conf.idx', 'euribor3m', 'nr.employed']]
y = data['y']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Créer le classificateur d'arbre de décision
clf = DecisionTreeClassifier(max_depth=5, random_state=42)
clf.fit(X_train, y_train)

# Visualiser l'arbre de décision
plt.figure(figsize=(15, 10))
plot_tree(clf, feature_names=X.columns, class_names=['No', 'Yes'], filled=True)
plt.savefig("decision_tree_bank.jpg", format='jpg', dpi=300)  # Enregistrer l'arbre en image
plt.show()
