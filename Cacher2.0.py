from PIL import Image





AlphabetNormal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

print(len(AlphabetNormal))




a = "␁"
print(a)






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