import pandas as pd

# Charger le fichier
file_path = 'bank-additional-full.csv'
data = pd.read_csv(file_path, sep=';')


def apply_filters(data):
    print("Colonnes disponibles pour filtrer :")
    print(data.columns.tolist())

    column = input("\nEntrez le nom de la colonne à filtrer : ")
    if column not in data.columns:
        print("Colonne non valide. Veuillez réessayer.")
        return data

    print("\nChoisissez le type de filtre :")
    print("1 - Valeur spécifique")
    print("2 - Plage de valeurs (pour les colonnes numériques)")
    filter_type = input("Entrez le numéro du type de filtre : ")

    if filter_type == "1":
        value = input(f"Entrez la valeur que vous souhaitez garder dans la colonne '{column}': ")
        filtered_data = data[data[column] == value]
    elif filter_type == "2":
        if not pd.api.types.is_numeric_dtype(data[column]):
            print(f"La colonne '{column}' n'est pas numérique. Plage de valeurs non applicable.")
            return data
        min_value = float(input(f"Entrez la valeur minimale pour '{column}': "))
        max_value = float(input(f"Entrez la valeur maximale pour '{column}': "))
        filtered_data = data[(data[column] >= min_value) & (data[column] <= max_value)]
    else:
        print("Type de filtre invalide. Veuillez réessayer.")
        return data

    print(f"\nFiltre appliqué sur '{column}' :")
    print(filtered_data.head())
    return filtered_data


filtered_data = data
while True:
    filtered_data = apply_filters(filtered_data)
    more_filters = input("\nVoulez-vous ajouter un autre filtre ? (oui/non) : ").lower()
    if more_filters != "oui":
        break

output_path = '/mnt/data/filtered_data.csv'
filtered_data.to_csv(output_path, index=False)
print(f"\nLes données filtrées ont été exportées dans : {output_path}")
