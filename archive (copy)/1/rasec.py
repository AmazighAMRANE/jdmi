def decrypt_cesar_cipher(ciphertext, shift):
    """
    Déchiffre un texte chiffré avec le chiffre de César en utilisant un décalage donné.
    
    :param ciphertext: Texte chiffré à déchiffrer.
    :param shift: Décalage utilisé pour le chiffrement.
    :return: Texte déchiffré.
    """
    decrypted_message = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
            	base =  ord('A')
            else :
            	base =  ord('a')
            decrypted_message += chr((ord(char) - base - shift) % 26 + base) 
        else:
            decrypted_message += char
    return decrypted_message

def read_file(file_path):
    """
    Lit le contenu d'un fichier.
    
    :param file_path: Chemin vers le fichier à lire.
    :return: Contenu du fichier.
    """
    with open(file_path, 'r') as file:
        return file.read()

def main():
    """
    Fonction principale pour lire un message chiffré à partir d'un fichier,
    le déchiffrer en utilisant le chiffre de César, et afficher le message déchiffré.
    """
    
    shift = 0 # Modifier le 0 en le shift approprié
    
    """Lire le message chiffré depuis le fichier"""
    ciphertext = read_file() # Créer le fichier contenant le texte chiffré et donner le chemin vers ce fichier à read_file() 
    
    """ Déchiffrer le message """
    decrypted_message = decrypt_cesar_cipher(ciphertext, shift)
    
    """ Afficher le message déchiffré"""
    print("Message déchiffré :")
    print(decrypted_message)

if __name__ == "__main__":
    main()

