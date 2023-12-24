from PIL import Image


### À changer pour input

image_to_solve = input("Donne moi le nom du fichier qui contient le message caché: ")



img = Image.open(image_to_solve)

largeur, hauteur = img.size




def compter_impair_colonne (x):
    n_red_impair = 0
    for i in range(hauteur):
        red, green, blue,alpha = img.getpixel((x,i))
        if red%2 == 1:
            n_red_impair = n_red_impair + 1
    return n_red_impair


message = ""

for x in range(largeur):
    message += chr(compter_impair_colonne(x))
    
print(message)

