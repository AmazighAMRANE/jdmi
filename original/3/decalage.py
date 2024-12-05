
def rearrange_block(block, permutation):
    """
    Réarrange un bloc de caractères selon une permutation donnée.
    
    Args:
        block (str): Le bloc de caractères à réarranger.
        permutation (list): La permutation des positions.
    
    Returns:
        str: Le bloc réarrangé.
    """
	# Exemple d'utilisation
    # block = "abcde"  # Le bloc de caractères initial
	# permutation = [4, 2, 0, 3, 1]  # La permutation des positions

	# La permutation indique :
	# Le caractère à la position 0 (a) va à la position 4
	# Le caractère à la position 1 (b) va à la position 2
	# Le caractère à la position 2 (c) va à la position 0
	# Le caractère à la position 3 (d) va à la position 3
	# Le caractère à la position 4 (e) va à la position 1

	# Après permutation :
	# a -> position 4
	# b -> position 2
	# c -> position 0
	# d -> position 3
	# e -> position 1

	# Le bloc réarrangé sera donc "cbeda"   
    rearranged_block = [''] * len(block)  # Initialiser une liste vide de la même longueur que le bloc
    for i in range(len(block)):  # Itérer sur chaque index du bloc
        new_pos =  permutation[i]  # Trouver la nouvelle position de l'élément à l'index i
        if i < len(block) and new_pos < len(block):  # Vérifier que les indices sont valides
            rearranged_block[new_pos] = block[i]  # Assigner le caractère à la position i de block à la nouvelle position dans rearranged_block
    return ''.join(rearranged_block)  # Combiner les caractères réarrangés en une seule chaîne

def read_file(file_path):
    """
    Lit le contenu d'un fichier.
    
    Args:
        file_path (str): Le chemin du fichier à lire.
    
    Returns:
        str: Le contenu du fichier.
    """
    with open(file_path, 'r') as file:
        return file.read()

def main():
    # Chemin du fichier chiffré
    file_path = 'ADecaler.txt'
    
    # Taille de chaque bloc à réaranger 
    taille_bloc = 4
    
    # Permutation des positions pour chaque caractère du bloc 
    # C'est une liste de taille taille_bloc où à chaque position i de la permutation on met la position entre 0 et taille_bloc où devrait être la ieme lettre d'un bloc
    permutation = [2,3 ,0,1]
    
    
    
    # Lire le message chiffré à partir du fichier
    ciphertext = read_file(file_path)
    
    # Initialiser le message déchiffré
    decrypted_message = ""
    
    # Parcourir le message chiffré par blocs de taille_bloc caractères
    for i in range(0, len(ciphertext), taille_bloc):
        block = ciphertext[i:i+taille_bloc]
        # Déchiffrer le bloc et l'ajouter au message déchiffré
        decrypted_message += rearrange_block(block, permutation)
    
    # Afficher le message clair
    print("Message déchiffré :")
    print(decrypted_message)

if __name__ == "__main__":
    main()

