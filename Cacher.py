from PIL import Image

import random

### À changer pour input

image_to_change = "image.jpeg"

### À changer pour input


img = Image.open(image_to_change)

#print("Image format:", img.format)
#print("Image mode:", img.mode)
#print("Image size:", img.size)
# pixel = image.getpixel((x, y))
#image.putpixel((x, y), new_color)

largeur, hauteur = img.size

def changeRGB(x,y):
    
    """
    Cette fonction prend la valeur R d'un pixel et la rend pair.
    """
    red, green, blue = img.getpixel((x,y))
    if red == 255:
        red = red - 1
    else:
        if red%2 == 1:
            red = red + 1
    img.putpixel((x, y), (red,green, blue))




### À changer pour input

message = "(Farouk aura 18,5 ans l'année prochaine.)"

### À changer pour input

message_en_ascii = []

def numeriser_message(message):
    
    """
    1 arg (string) -> list of int
    
    Cette fonction reçoit un message et renvoie une liste.
    Chaque élément de la liste est la valeur numérique en ascii d'un caractère du message.
    Les éléments de la liste sont dans le même ordre que les caractères du message.
    
    """
    
    for i in range(len(message)):
        message_en_ascii.append(ord(message[i]))
        
    return message_en_ascii


        
    
def choisir_coordonnées_alea (n_coord_aléa):
    """
    input:  1 int -> output: 1 new_liste
    
    Cette fonction reçoit un un nombre x.
    Elle renvoie une nouvelle liste de x éléments différents de la liste liste_des_valeurs_y_possible de façon aléatoire
    """
    liste_des_valeurs_y_possible = []
    for i in range(1, hauteur):
        liste_des_valeurs_y_possible.append(i)

    coordonnées_alea = random.sample(liste_des_valeurs_y_possible, n_coord_aléa)
    return coordonnées_alea



for x in range(largeur):
    for y in range(hauteur):
        changeRGB(x,y)  


def cache_nombre_sur_une_colonne(i):
    for y in choisir_coordonnées_alea (numeriser_message(message)[i]):
        red, green, blue = img.getpixel((i,y))
        red = red + 1
        img.putpixel((i,y),(red, green, blue))

for x in range(len(message)):
    cache_nombre_sur_une_colonne(x)





img.save("image_changed.jpeg")

def compter_impair_colonne (x):
    n_red_impair = 0
    for i in range(hauteur):
        red, green, blue = img.getpixel((x,i))
        if red%2 == 1:
            n_red_impair = n_red_impair + 1
    return n_red_impair


for x in range(len(message)):
   print(chr(compter_impair_colonne(x)))



"""    
def cache_nombre_sur_une_colonne(i):
    
    for x in range(largeur):
        for y in range(hauteur):
            changeRGB(x,y)
    

    valeurs_y = choisir_coordonnées_alea(numeriser_message(message)[i])
    
    for z in valeurs_y:
        red, green, blue = img.getpixel((i,z))
        red = red + 1
        img.putpixel((i, valeurs_y[z]), (red,green, blue))
        
    return red
        
print(cache_nombre_sur_une_colonne(0))



        
img.save("image_changed.jpeg")

img.show()
        
"""
"""
    reçoit liste d'int
    pour le int de valeur x à la n-ième position, prendre coordonée (n,y) de l'image.
    prendre aléatoirement x éléments de cette liste (a,b,c,...)
    changer le R en faisant + 1 (ou -1 si max) de la position (x,a),(x,b),...)
    changer 
    
    """
        

