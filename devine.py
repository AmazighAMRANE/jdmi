import os

# Vérification de l'existence du fichier avant de l'importer
try:
    if os.path.exists("pasImportantDevine.pyc"):
        from pasImportantDevine import *  # Importation si le fichier existe
    else:
        print("T'as laissé passer ta chance frère")
        exit(1)  # Sortir si le fichier n'existe plus
except Exception as e:
    print(f"Erreur lors de l'importation de pasImportantDevine.py: {e}")
    exit(1)  # Sortir si une erreur d'importation se produit

# Exécution du programme principal
if __name__ == "__main__":
    mainDevine()

