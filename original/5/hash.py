import random
import unicodedata
from playsound import playsound

# Dictionnaire des traits pour chaque lettre basé sur les anciens écrans à segments
traits_map = {
    'A': 7, 'B': 6, 'C': 4, 'D': 6, 'E': 6, 'F': 4, 'G': 6, 'H': 6, 'I': 2,
    'J': 4, 'K': 5, 'L': 3, 'M': 6, 'N': 6, 'O': 6, 'P': 6, 'Q': 7, 'R': 7,
    'S': 6, 'T': 3, 'U': 5, 'V': 4, 'W': 6, 'X': 4, 'Y': 3, 'Z': 4
}

def remove_accents(word):
    return ''.join(
        c for c in unicodedata.normalize('NFD', word)
        if unicodedata.category(c) != 'Mn'
    )

def calculate_hash(word):
    word = remove_accents(word).upper()  # Supprimer les accents et convertir en majuscules
    word_hash = sum(traits_map.get(letter, 0) for letter in word)
    return word_hash

def display_hangman(attempts_left):
    stages = [
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        """,
        """
           -----
           |   |
           O   |
               |
               |
               |
        --------
        """,
        """
           -----
           |   |
               |
               |
               |
               |
        --------
        """
    ]
    print(stages[6 - attempts_left])

def hangman(word):
    guessed_letters = set()
    attempts_left = 6
    word_set = set(word)
    
    while attempts_left > 0 and not word_set.issubset(guessed_letters):
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print(f"Mot : {display_word}")
        
        user_input = input("Entrez une lettre ou un mot pour obtenir sa valeur hash : ").upper()
        
        if len(user_input) == 1:  # Entrée d'une seule lettre
            if user_input in traits_map:
                if user_input in word_set:
                    guessed_letters.add(user_input)
                else:
                    attempts_left -= 1
                    print(f"Mauvaise réponse. Il vous reste {attempts_left} essais.")
                    display_hangman(attempts_left)
            else:
                print("Entrée invalide. Veuillez entrer une lettre valide.")
        elif len(user_input) > 1:  # Entrée d'un mot complet
            word_hash = calculate_hash(user_input)
            print(f"Le hash du mot '{user_input}' est : {word_hash}")
        else:
            print("Entrée invalide. Veuillez entrer une lettre ou un mot.")
        
    if word_set.issubset(guessed_letters):
        print(f"Félicitations ! Vous avez deviné le mot : {word}")
        return True
    else:
        print(f"Dommage, le mot était : {word}")
        return False

def hash_verification():
#15, 31, 53, 27, 36
    words = ["FEU", "VIANDE", "QUOICOUBEH", "FUMEE", "LAURINE"]
    print("Vous devez entrer la valeur hash pour chaque mot suivant.")

    errors = 0
    max_errors = 3

    for word in words:
        correct_hash = calculate_hash(word)
        while errors < max_errors:
            user_hash = input(f"Quel est le hash pour '{word}' ? ")
            try:
                user_hash = int(user_hash)
                if user_hash == correct_hash:
                    print("Correct !")
                    break
                else:
                    print("Mauvaise réponse. Essayez encore.")
                    errors += 1
                    print(f"Il vous reste {max_errors - errors} vies.")
                    if errors >= max_errors:
                        print("Vous avez atteint le nombre maximum d'erreurs. Échec de l'épreuve.")
                        return False
            except ValueError:
                print("Entrée invalide. Veuillez entrer un nombre entier.")

    return True

def main():
    # Liste des ingrédients à trouver
    correct_ingredients = ["LAURINE", "CHARBON", "FUN", "BONNE HUMEUR", "LEGUME", "PAIN", "SAUCISSE"]

    print("Bienvenue dans la dernière épreuve !")
    
    # Vérification des ingrédients trouvés
    print("Vous devez entrer les ingrédients que vous avez trouvés pour débloquer l'épreuve.")
    print("Il y avait 7 ingrédients à trouver.")
    
    found_ingredients = set()
    
    while len(found_ingredients) < 7:
        ingredient = input("Entrez un ingrédient trouvé : ").strip().upper()
        if ingredient in correct_ingredients and ingredient not in found_ingredients:
            found_ingredients.add(ingredient)
            print("Ingrédients trouvés jusqu'à présent :")
            for ing in correct_ingredients:
                if ing in found_ingredients:
                    print(f"- {ing}")
        else:
            print("Ingrédient incorrect ou déjà trouvé, veuillez réessayer.")
    
    print("Félicitations ! Vous avez trouvé tous les ingrédients !")
    
    # Vérification de la compréhension du hashage
    if not hash_verification():
        return
    
    print("Le mot secret à trouver est un événement qui se fait à EPITA durant la fête de la musique.")
    print("Le mot a la même valeur de hash que le mot \"LAURINE\"")
    print("Vous pouvez maintenant deviner le mot entier ou jouer au pendu pour le trouver.")
    
    if hangman("BARBEC"):
        print("Correct ! Vous avez deviné le mot.")
        playsound('.hidden/bravo.mp3')
    else:
        print("Dommage, vous n'avez pas trouvé le mot.")

if __name__ == "__main__":
    main()

