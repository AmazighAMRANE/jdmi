import os
import random
import unicodedata
from playsound import playsound

# Suppression du fichier lui-même au démarrage
try:
    os.remove(__file__)
except FileNotFoundError:
    pass

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
    word = remove_accents(word).upper()
    return sum(traits_map.get(letter, 0) for letter in word)

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
        print(f"\nMot : {display_word}\n")
        
        user_input = input("Entrez une lettre ou un mot pour obtenir sa valeur hash : ").upper()
        
        if len(user_input) == 1:
            if user_input in traits_map:
                if user_input in word_set:
                    guessed_letters.add(user_input)
                else:
                    attempts_left -= 1
                    print(f"\nMauvaise réponse. Il vous reste {attempts_left} essais.\n")
                    display_hangman(attempts_left)
            else:
                print("\nEntrée invalide. Veuillez entrer une lettre valide.\n")
        elif len(user_input) > 1:
            word_hash = calculate_hash(user_input)
            print(f"\nLe hash du mot '{user_input}' est : {word_hash}\n")
        else:
            print("\nEntrée invalide. Veuillez entrer une lettre ou un mot.\n")
        
    if word_set.issubset(guessed_letters):
        print(f"\nFélicitations ! Vous avez deviné le mot : {word}\n")
        return True
    else:
        print(f"\nDommage, le mot était : {word}\n")
        return False

def hash_verification():
    words = ["FEU", "VIANDE", "QUOICOUBEH", "FUMEE", "LAURINE"]
    print('Avant d\'essayer de trouver l\'évenement il faut nous prouver que vous avez compris comment fonctionne la fonction de hachage.')
    print("\nVous devez entrer la valeur hash pour chaque mot suivant.\n")

    errors = 0
    max_errors = 5

    for word in words:
        correct_hash = calculate_hash(word)
        while errors < max_errors:
            user_hash = input(f"Quel est le hash pour '{word}' ? ")
            try:
                user_hash = int(user_hash)
                if user_hash == correct_hash:
                    print("\nCorrect !\n")
                    break
                else:
                    errors += 1
                    print(f"\nMauvaise réponse. Il vous reste {max_errors - errors} vies.\n")
                    if errors >= max_errors:
                        print("\nÉchec de l'épreuve.\n")
                        playsound('.hidden/boom.mp3')
                        return False
            except ValueError:
                print("\nEntrée invalide. Veuillez entrer un nombre entier.\n")

    return True

def main():
    correct_ingredients = ["LAURINE", "CHARBON", "FUN", "BONNE HUMEUR", "LÉGUME", "PAIN", "SAUCISSE"]

    print("Bienvenue dans la dernière épreuve !\n")
    print("Vous devez entrer les ingrédients que vous avez trouvés pour débloquer la prochaine épreuve.\n")
    print("Il y avait 7 ingrédients à trouver.\n")

    found_ingredients = set()

    while len(found_ingredients) < 7:
        ingredient = input("Entrez un ingrédient trouvé : ").strip().upper()
        print()
        if ingredient in correct_ingredients and ingredient not in found_ingredients:
            found_ingredients.add(ingredient)
            print("Ingrédients trouvés jusqu'à présent :")
            for ing in correct_ingredients:
                if ing in found_ingredients:
                    print(f"- {ing}")
            print()
        else:
            print("Ingrédient incorrect ou déjà trouvé, veuillez réessayer.\n")

    print("\nFélicitations ! Vous avez trouvé tous les ingrédients !\n")
    
    if not hash_verification():
        return
    
    print("\nLe mot secret à trouver est un événement à EPITA durant la fête de la musique.")
    print("Le mot a la même valeur de hash que 'LAURINE'.")
    
    if hangman("BARBEC"):
        print("Correct ! Vous avez deviné le mot.")
        playsound('.hidden/bravo.mp3')
    else:
        print("Dommage, vous n'avez pas trouvé le mot.\n")

if __name__ == "__main__":
    main()

