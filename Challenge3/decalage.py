
def rearrange_block(block, permutation):
    """
    Réarrange un bloc de caractères selon une permutation donnée.
    
    Args:
        block (str): Le bloc de caractères à réarranger.
        permutation (list): La permutation des positions.
    
    Returns:
        str: Le bloc réarrangé.
    """
    rearranged_block = [''] * len(block)  
    for i in range(len(block)):  
        new_pos =  permutation[i]  
        if i < len(block) and new_pos < len(block):  
            rearranged_block[new_pos] = block[i]  
    return ''.join(rearranged_block)  

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
    
    file_path =	       # Chemin du fichier où se trouve le chiffré. Il faut garder les sauts de lignes
    
    taille_bloc =      # Taille de chaque bloc à réaranger 
    
    # Permutation des positions pour chaque caractère du bloc 
    permutation = 	# C'est une liste de taille taille_bloc où à chaque position i de la permutation on met la position entre 0 et taille_bloc où devrait être la ieme lettre d'un bloc
    '''Exemple : Si le texte chiffré est abcdef, la taille du block est 3 et la permutation est [2,1,0] alors après déchiffrement on obtient : cbafed'''
    
    
    ''' Lire le message chiffré à partir du fichier '''
    ciphertext = read_file(file_path)
    
    ''' Initialiser le message déchiffré '''
    decrypted_message = ""
    
    ''' Parcourir le message chiffré par blocs de taille_bloc caractères '''
    for i in range(0, len(ciphertext), taille_bloc):
        block = ciphertext[i:i+taille_bloc]
        ''' Déchiffrer le bloc et l'ajouter au message déchiffré '''
        decrypted_message += rearrange_block(block, permutation)
    
    ''' Afficher le message clair '''
    print("Message déchiffré :")
    print(decrypted_message)

if __name__ == "__main__":
    main()

