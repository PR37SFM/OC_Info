from PIL import Image


#Cryptage du message
message = input("inserez un message")
DemandeCryptage = input("Voulez-vous crypté votre message avec une clé ?")
if DemandeCryptage.lower() == "oui" or "non":
    if "oui" == DemandeCryptage.lower():
        clé = input("inserez votre clé. Attention! ne pas mettre plus d'une fois le même caractère.")
    elif "non" == DemandeCryptage.lower():
        None
else:
    print("veuillez répondre à la question par oui ou par non.")

def Cryptage(message, clé):
    alphabetNormal = "abcdefghijklmnopqrstuvwxyz"
    alphabizzare = ""
    alphabizzare += clé
    for lettre in alphabetNormal:
        if lettre not in clé:
            alphabizzare += lettre
    messageCrypte = ""
    for lettre0 in message:
        if lettre0 not in alphabizzare:
            messageCrypte += lettre0
        else:
            pos = alphabetNormal.index(lettre0)
            newlettre = alphabizzare[pos]
            newlettre = newlettre.upper()
            messageCrypte += newlettre
    return messageCrypte












#CODAGE

#Etape 1 : créer un alphabet de a-z + A-Z + numéro + caractère spéciaux visibles (/!\ pas ceux non visibles et inutiles),
#puis introduire une clé mode Cesar2 (optionnel pour l'utilisateur).

#Etape 2 : attribuer à chaque caractère un nombre impaire. /!\ pas dépasser 255. Puis transformer message.

#Etape 3 : rendre R-G-B-A tous pair en faisant +1 lorsque impaire.

#Etape 4 : fonction qui traite chaque ligne vertical de l'image, une par une, caractère par caractère.

#Etape 5 : compare chaque valeur R-G-B-A de tous les pixels de la ligne avec valeur numérique du message.

#Etape 6 : pixel dont la valeur est la plus proche de celle du message est remplacé.

#Etape 7 : renvoi l'image avec tout le message caché dans chaque ligne vertical de l'image dans le sens -> horinzontal.



#DECODAGE

#Etape 1 : redemande si il y'avait une clé ou non, si oui introduire la clé.

#Etape 2 : formation de l'alphabet.

#Etape 3 : analyse de chaque valeur R-G-B-A de tout les pixels, puis prend la valeur impaire si il en trouve.

#Etape 4 : retranscription des valeurs trouvés en alphabet normal.