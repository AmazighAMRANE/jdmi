# Base de données des prénoms avec leurs indices et hashes
database = {
    "Aymeric": ("suite", 307),
    "Cathaline": ("malade", 139),
    "César": ("trousse", 941),
    "Corentin": ("chocolat", 593),
    "Denis": ("perdu", 593),
    "Élisabeth": ("arroser", 47),
    "Éloi": ("terrible", 811),
    "Emy": ("argent", 863),
    "Frédéric": ("tente", 811),
    "Gaspard": ("s′asseoir", 281),
    "Ghislain": ("col", 787),
    "Gladys": ("savon", 677),
    "Lana": ("gens", 271),
    "Leila": ("pas tomate", 739),
    "Lili": ("craie", 11),
    "Lucile": ("rang", 479),
    "Margot": ("vert", 739),
    "Paul": ("végé", 739),
    "Perceval": ("usine", 307),
    "Quitterie": ("laisse", 719),
    "Romain": ("strasbourg", 257),
    "Sarah": ("amusant", 673),
    "Siméon": ("toulouse", 257),
    "Stanislas": ("francfort", 257),
    "Vincent": ("désordre", 173),
    "Yannick": ("levure", 593)
}

def get_info(prenom):
    """
    Cherche le prénom dans la base de données et renvoie l'indice et le hash correspondants.

    Args:
        prenom (str): Le prénom à chercher.

    Returns:
        tuple: Un tuple contenant l'indice et le hash.
    """
    info = database.get(prenom)
    if info:
        indice, hash_val = info
        return indice, hash_val
    else:
        return None, None

# Boucle principale
while True:
    # Demander à l'utilisateur de saisir un prénom
    prenom = input("Entrez un prénom (ou tapez 'q' pour quitter) : ").strip()
    
    # Condition d'arrêt
    if prenom.lower() == 'q':
        print("Arrêt du programme.")
        break

    # Obtenir les informations correspondantes
    indice, hash_val = get_info(prenom)

    if indice and hash_val:
        print(f"Indice : {indice}")
        print(f"Hash : {hash_val}")
    else:
        print("Prénom non trouvé dans la base de données.")

