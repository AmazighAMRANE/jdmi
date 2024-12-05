def decrypt_cesar_cipher(ciphertext, shift):
    """
    Déchiffre un texte chiffré avec le chiffre de César en utilisant un décalage donné.
    
    :param ciphertext: Texte chiffré à déchiffrer.
    :param shift: Décalage utilisé pour le chiffrement.
    :return: Texte déchiffré.
    """
    decrypted_message = ""
    # Avant toute chose, tester les fonctions ord(lettre) et chr(entier) sur le terminal pour comprendre leur fonctionnement.
    for char in ciphertext:
        if char.isalpha():
	    # Traitement des caractères alphabétiques
            # Déterminer la base ASCII selon que le caractère est majuscule ou minuscule.
            # base est la valeur que je dois soustraire à ord(lettre) pour que ord(lettre) - base = la position de lettre entre 0 et 25.    
            # Exemple ord('c') - base doit être égal à 2.          
            if char.isupper():
            	base = ord('A') # Remplacer ? par la base ASCII pour les majuscules
            else :
            	base = ord('a') # Remplacer ? par la base ASCII pour les minuscules
            # Calculer le caractère déchiffré en utilisant les fonctions ord(caractère) et chr(entier) puis l'ajouter à decrypted_message
            # Le ramener vers l'encodage 0 -> 25, faire le shift, puis retourner vers l'encodage base -> (base + 25)
            # Attention à ne pas descendre au dessous de 0 en faisant le shift: penser au modulo
            decrypted_message += chr((ord(char) - base - shift) % 26 + base) # Remplacer ? par l'expression correct DONNER PLUS D'INDICATION ICI
        else:
            # Ajouter les caractères non alphabétiques tels quels
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
    # Chemin du fichier contenant le message chiffré
    file_path = 'message.txt'
    
    # Demander le décalage utilisé pour chiffrer le message
    shift = int(input("Entrez le décalage utilisé pour chiffrer le message : "))
    
    # Lire le message chiffré depuis le fichier
    ciphertext = read_file(file_path)
    
    # Déchiffrer le message
    decrypted_message = decrypt_cesar_cipher(ciphertext, shift)
    
    # Afficher le message déchiffré
    print("Message déchiffré :")
    print(decrypted_message)

if __name__ == "__main__":
    main()

