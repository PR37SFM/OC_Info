from PIL import Image


### À changer pour input

image_to_solve = "/Users/Kenan/Documents/OC_Info_Projet/image_changed.jpeg"


### À changer pour input


img = Image.open(image_to_solve)

largeur, hauteur = img.size




def compter_impair_colonne (x):
    n_red_impair = 0
    for i in range(hauteur):
        red, green, blue = img.getpixel((x,i))
        if red%2 == 1:
            n_red_impair = n_red_impair + 1
    return n_red_impair

print(img.getpixel((0,0)))

for x in range(1):
   print(chr(compter_impair_colonne(x)))

