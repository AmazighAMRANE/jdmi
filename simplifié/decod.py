def decode_cesar(text):
    decoded_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr(((ord(char) - 97 - 3) % 26) + 97) if char.islower() else chr(((ord(char) - 65 - 3) % 26) + 65)
            decoded_text += shifted_char
        else:
            decoded_text += char
    return decoded_text

def decode_file_with_cesar(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            decoded_text = decode_cesar(text)
            return decoded_text
    except FileNotFoundError:
        return "Le fichier n'a pas été trouvé."

# Exemple d'utilisation :
file_path = "chemin/vers/votre/fichier.txt"
decoded_text = decode_file_with_cesar(file_path)
print(decoded_text)


# Le dictionnaire fourni
dict = {'DG':'j', 'FD':'n', 'AV': 'e', 'FG': 'p', 'DF': 'i', 'GD': 't', 'AA': 'a', 'AF': 'c', 'FA': 'm', 'GF': 'u', 'GA': 's', 'FX': 'r', 'AD': 'b', 'FF': 'o', 'DA': 'g', 'AG': 'd', 'GV': 'w', 'VV': '2', 'VF': '0',  'DX': 'l'}

# Le message codé
message = "AV FG DF GD AA AF AA FA FG GF GA GA GD FX AA GA AD FF GF FX DA , DX AV VG XV DG GF DF FD VV VF VV VV GF FD AV FD FF GD AV GA AV AF FX AV GD AV FD FF GF GA AG DF GD FV GF AV DX AV GA DF FD DA FX AV AG DF AV FD GD GA GA FF FD GD : AG GF AF DD AA FX AD FF FD . AG GF AX GF FD . AG AV DX AA AD FF FD FD AV DD GF FA AV GF FX . FG AG GV , AG DF FX AV AF GD AV GF FX AG AV DX ' AV FG DF GD AA"

# Fonction pour déchiffrer le message
def dechiffrer(message, dictionnaire):
	result = ""
	i = 0
	message = message.replace(" ","")
	message = message.replace("'","")
	message = message.replace(".","")	
	message = message.replace(":","")
	message = message.replace(",","")
	print(message)
	print("ici")
	while i < len(message):
		# Récupérer la paire de caractères actuelle
		paire = message[i:i+2]
		# Vérifier si la paire existe dans le dictionnaire
		if paire in dictionnaire:
			# Ajouter la lettre déchiffrée au résultat
			result += dictionnaire[paire]
		else:
			result+=paire
		# Passer à la prochaine paire de caractères
		i += 2
	return result

# Déchiffrer le message
message_dechiffre = dechiffrer(message, dict)
print(message_dechiffre)




def dechiffrerPermut(message):
	chiffre = message.replace(" ","")
	clair = ""
	sousClair = " "*4
	print(len(sousClair))
	i = 0
	while i < len(message)-1:
		sousClair[0] = message[i+2]
		print(sousClair)
		sousClair[1] = message[i+3]
		sousClair[2] = message[i+1]
		sousClair[3] = message[i]
		print(sousClair)
		clair+=sousClair
		i=i+4
	return clair




print(dechiffrerPermut("TIEPmaACSspusatrruboelg,uj21\ninaçAhesnegnmasaepoP!\néd"))





