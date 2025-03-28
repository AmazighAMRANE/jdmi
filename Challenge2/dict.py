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
                parts = line.strip().split()
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
    print()  

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
            contenu = file.read().replace('\n', ' ')
    except FileNotFoundError:
        print(f"Le fichier {fichier} n'a pas été trouvé.")
        return
    # La variable dictionnaire est un mappage où chaque clé représente une paire de lettres chiffrées 
    # et chaque valeur correspond à la lettre déchiffrée associée.
    # Ce mappage est basé sur les données fournies dans le fichier dictionnaire.txt.
    # Par exemple dicitionnaire[AA] = a    
    dictionnaire = {v: k for k, v in dictionnaire.items() if v}
    
    
    #Construction du déchiffré"
    message_dechiffre = ""

    paires_chiffrees = contenu.split()
    for pair in paires_chiffrees:
        if len(pair) == 2 and pair in dictionnaire:
            message_dechiffre += pair + " " # Remplacer "pair" par sa valeur dans la variable dictionnaire
        else:
            message_dechiffre += pair + " "
    
    print("\nMessage déchiffré :")
    print(message_dechiffre)
    print() 

""" Nom des fichiers contenant le dictionnaire et le message chiffré """
fichier_dictionnaire =  # Mettre le fichier contenant le dictionnaire
fichier_message = 	# Mettre le chemin vers le fichier contenant le message chiffré


alphabet_dict = lire_dictionnaire(fichier_dictionnaire)


afficher_lettres_inconnues(alphabet_dict)


dechiffrer_message(fichier_message, alphabet_dict)

