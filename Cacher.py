from PIL import Image

import random




def changeRGB(img, x,y):
    
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




def numeriser_message(message):
    """
    1 arg (string) -> list of int
    Cette fonction reçoit un message et renvoie une liste.
    Chaque élément de la liste est la valeur numérique en ascii d'un caractère du message.
    Les éléments de la liste sont dans le même ordre que les caractères du message.
    """
    message_en_ascii = []
    for i in range(len(message)):
        message_en_ascii.append(ord(message[i]))
    return message_en_ascii


        
    
def liste_coordonnées_alea (hauteur, n_coord_aléa):
    """
    input:  1 int -> output: 1 new_liste
    Cette fonction reçoit un  nombre x.
    Elle renvoie une nouvelle liste de x éléments différents de la liste liste_des_valeurs_y_possible de façon aléatoire
    """
    liste_des_valeurs_y_possible = []
    for i in range(1, hauteur):
        liste_des_valeurs_y_possible.append(i)
    coordonnées_alea = random.sample(liste_des_valeurs_y_possible, n_coord_aléa)
    return coordonnées_alea




def cache_nombre_sur_une_colonne(img,x):
    """
    1 int -> return None
    cette Fonction reçoit un nombre x.
    Elle reçoit 
    """
    largeur, hauteur = img.size    
    for i in liste_coordonnées_alea(hauteur, numeriser_message(message)[x]):
        red, green, blue = img.getpixel((x,i))
        red = red + 1
        img.putpixel((x,i),(red, green, blue))




def cacher_message(image_to_change,message):

    """
    input: (string,string)
    
    Cette fonction demande comme premier argument le nom du fichier jpeg de l'image dans laquelle l'utilisateur veut cacher un message.
    Puis comme 2ème argument le message que l'utilisateur veut cacher.
    """
    img = Image.open(image_to_change)
    largeur, hauteur = img.size
    
    for x in range(largeur):
        for y in range(hauteur):
            changeRGB(img,x,y)

    for x in range(len(message)):
        cache_nombre_sur_une_colonne(img,x)
    
    img.save("image_changed.jpeg")

    img.close()
    


        
message = input("Ecris-moi le message que tu veux caché dans l'image:")

image_to_change = input("Ecris-moi le nom du fichier jpeg de l'image où tu veux cacher un message:")

cacher_message(image_to_change,message)





"""

Ici, on a la version de trouver le message qui marche mais seulement ici.



def compter_impair_colonne (img, x):
    
    largeur, hauteur = img.size
    
    n_red_impair = 0
    for i in range(hauteur):
        red, green, blue = img.getpixel((x,i))
        if red%2 == 1:
            n_red_impair = n_red_impair + 1
    return n_red_impair



for x in range(len(message)):
    print(chr(compter_impair_colonne(img,x)))
    
    """