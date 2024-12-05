import os
import time
from playsound import playsound

def afficher_introduction():
    print("""
    Les fonctions de condensat (hash functions, en anglais) sont des fonctions qui associent une 
    valeur de taille fixe à des données de taille quelconque. Si deux données sont identiques, elles 
    ont le même hash. Cependant, l'inverse n'est pas toujours vrai : des données différentes peuvent 
    avoir le même hash, ce que l'on appelle une collision. Cette valeur, le hash, n'a rien à voir avec 
    la donnée elle-même et ne permet pas de retrouver directement la donnée d'origine.

    • Vous avez obtenu une liste d'utilisateurs avec le hash de leurs mots de passe.
    Grâce aux indices, trouvez les trois ingrédients nécessaires à l'événement !

    Nom           | Hash
    ---------------------
    Aymeric       | 307
    Cathaline     | 139
    César         | 941
    Corentin      | 593
    Denis         | 593
    Élisabeth     | 47
    Éloi          | 811
    Emy           | 863
    Frédéric      | 811
    Gaspard       | 281
    Ghislain      | 787
    Gladys        | 677
    Lana          | 271
    Leila         | 739
    Lili          | 11
    Lucile        | 479
    Margot        | 739
    Paul          | 739
    Perceval      | 307
    Quitterie     | 719
    Romain        | 257
    Sarah         | 673
    Siméon        | 257
    Stanislas     | 257
    Vincent       | 173
    Yannick       | 593
    """)




# Define the correct hashes, their corresponding ingredients, and hints
hash_ingredient_map = {
    257: ("saucisse", ["Strasbourg", "Toulouse", "Francfort"]),
    593: ("pain", ["Chocolat", "Perdu", "Levure"]),
    739: ("légume", ["Pas tomate", "Vert", "Végé"])
}

# Keep track of found ingredients
found_ingredients = set()

# Maximum number of cumulative attempts allowed
MAX_ATTEMPTS = 10

# Lock file to ensure the program can only be run once
LOCK_FILE = ".hidden/program_lock.lock"

def get_ingredient_and_hints(hash_value):
    return hash_ingredient_map.get(hash_value, (None, None))

def display_found_ingredients():
    print("Ingrédients trouvés :")
    for ingredient in found_ingredients:
        print(f"- {ingredient}")
    
    if len(found_ingredients) == 3:
        print("Félicitations ! Vous avez trouvé tous les ingrédients !")
    else:
        print("Le programme s'est terminé avant que vous ayez trouvé tous les ingrédients.")

def self_destruct():
    display_found_ingredients()
    print("Le programme s'autodétruira dans 3 secondes...")
    playsound('.hidden/boom.mp3')  # Play the boom sound
    time.sleep(1)  # Allow the sound to play for 3 seconds
    if os.path.exists(__file__):
        os.remove(__file__)
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)

def create_lock_file():
    with open(LOCK_FILE, 'w') as file:
        file.write("This program is locked to prevent multiple runs.")

def main():

    # Introduction message
    print("Bienvenue dans la collecte d'ingrédients !")
    print("Vous devez deviner trois ingrédients en fournissant les hash correspondants.")
    print("Pour chaque hash il y a un ingrédient à deviner en s'aidant des indices correspondants.")
    print("Une fois que vous commencez à essayer de deviner, vous ne pourrez plus relancer le programme.")
    print("Vous avez droit à 10 essais. Si vous échouez, le programme s'autodétruira.")
    print("Commençons !\n")
    
    
    afficher_introduction()
    
    # Check if the lock file exists to prevent multiple runs
#    if os.path.exists(LOCK_FILE):
#        print("Le programme a déjà été exécuté une fois. Exécution multiple non autorisée.")
#        return
#    else:
    create_lock_file()

    attempts = 0
    
    while len(found_ingredients) < 3:
        if attempts >= MAX_ATTEMPTS:
            self_destruct()
            return

        hash_input = input("Entrez un hash pour obtenir les indices : ")
        
        try:
            hash_value = int(hash_input)
        except ValueError:
            print("Hash invalide. Veuillez entrer un nombre entier.")
            attempts += 1
            print(f"Il vous reste {MAX_ATTEMPTS - attempts} essais.")
            if attempts >= MAX_ATTEMPTS:
                self_destruct()
                return
            continue
        
        ingredient, hints = get_ingredient_and_hints(hash_value)
        
        if ingredient:
            if ingredient in found_ingredients:
                print("Ingrédient déjà trouvé. Veuillez essayer un autre hash.")
                continue

            print(f"Hash trouvé ! Voici les indices : {', '.join(hints)}")
            while attempts < MAX_ATTEMPTS:
                guessed_ingredient = input("Quel est l'ingrédient ? ").strip().lower()
                
                if guessed_ingredient == ingredient:
                    print("Bonne réponse !")
                    found_ingredients.add(ingredient)
                    break
                else:
                    attempts += 1
                    print(f"Mauvaise réponse. Vous avez {MAX_ATTEMPTS - attempts} essais restants.")
                    
                    if attempts < MAX_ATTEMPTS and len(found_ingredients) < 2:
                        print("Vous pouvez essayer un autre hash si vous le souhaitez.")
                        break

            if len(found_ingredients) == 3:
                break
        else:
            print("Hash incorrect. Veuillez réessayer.")
            attempts += 1
            print(f"Il vous reste {MAX_ATTEMPTS - attempts} essais.")
            if attempts >= MAX_ATTEMPTS:
                self_destruct()
                return
    
    display_found_ingredients()

if __name__ == "__main__":
    main()

