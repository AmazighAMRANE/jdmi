import string

def lire_dictionnaire(fichier):
    """
    Lit un fichier contenant le dictionnaire de substitution.
    
    Le fichier doit contenir chaque lettre de l'alphabet suivie de sa paire de caractères correspondante, 
    séparées par des espaces ou des sauts de ligne.

    Args:
        fichier (str): Le nom du fichier contenant le dictionnaire.

    Returns:
        dict: Un dictionnaire où les clés sont les lettres de l'alphabet et les valeurs sont des paires de caractères.
    """
    dictionnaire = {}
    try:
        with open(fichier, 'r') as file:
            for line in file:
                # Supprimer les espaces en début et fin de ligne, puis diviser par les espaces
                parts = line.strip().split()
                # Traiter chaque paire de lettres trouvée
                for i in range(0, len(parts), 2):
                    if i + 1 < len(parts):
                        key = parts[i]
                        value = parts[i + 1]
                        if len(value) == 2:
                            dictionnaire[key] = value
                        else:
                            print(f"Valeur incorrecte ignorée : {value}")                 
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
        return {}
    return dictionnaire

def afficher_lettres_inconnues(dictionnaire):
    """
    Affiche les lettres pour lesquelles la valeur est encore inconnue.

    Args:
        dictionnaire (dict): Le dictionnaire de substitution.
    """
    lettres_connues = set(dictionnaire.keys())
    lettres_toutes = set(string.ascii_lowercase)
    lettres_inconnues = lettres_toutes - lettres_connues

    if lettres_inconnues:
        print("\nLettres dont la valeur est inconnue :")
        for lettre in lettres_inconnues:
            print(lettre)
    else:
        print("\nToutes les lettres ont des valeurs connues.")
    print()  # Ajouter une ligne vide pour une meilleure lisibilité

def dechiffrer_message(fichier, dictionnaire):
    """
    Lit un fichier contenant un message chiffré et le déchiffre en utilisant le dictionnaire fourni.
    
    Le message chiffré doit être constitué de paires de caractères séparées par des espaces.

    Args:
        fichier (str): Le nom du fichier contenant le message chiffré.
        dictionnaire (dict): Un dictionnaire où les clés sont des lettres de l'alphabet et les valeurs sont des paires de caractères.
    """
    try:
        with open(fichier, 'r') as file:
            # Lire le message chiffré en conservant les sauts de ligne
            contenu = file.read().replace('\n', ' ')
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
        return
    
    # Inverser le dictionnaire pour obtenir un dictionnaire de déchiffrement
    # inverse_dict contient des paires de lettres majuscule comme clés et le déchiffré de cette paire comme valeur : inverse_dict[paire] = dechiffré de la paire.
    dicticonnaire = {v: k for k, v in dictionnaire.items() if v}
    
    message_dechiffre = ""
    # Diviser le contenu en paires en utilisant les espaces comme séparateurs
    paires_chiffrees = contenu.split()
    for pair in paires_chiffrees:
        if len(pair) == 2 and pair in dicticonnaire:
            message_dechiffre += dicticonnaire[pair] + " " # Remplacer ??? par la valeur corresondante à pair dans inverse_dict
        else:
            # Si la paire n'est pas trouvée ou est mal formatée, la laisser telle quelle
            message_dechiffre += pair + " "
    
    print("\nMessage déchiffré :")
    print(message_dechiffre)
    print()  # Ajouter une ligne vide pour une meilleure lisibilité

# Nom des fichiers contenant le dictionnaire et le message chiffré
fichier_dictionnaire = "dictionnaire.txt"
fichier_message = "message.txt"

# Lire le dictionnaire à partir du fichier
alphabet_dict = lire_dictionnaire(fichier_dictionnaire)

# Afficher les lettres dont la valeur est inconnue
afficher_lettres_inconnues(alphabet_dict)

# Déchiffrer le message en utilisant le dictionnaire
dechiffrer_message(fichier_message, alphabet_dict)

