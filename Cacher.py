from PIL import Image

import random




def changeRGB(img, x,y):
    
    """
    Cette fonction reçoit une image et une coordonnée. Elle renvois une liste d'int.
    Cette fonction prend la valeur R (red) d'un pixel à la position (x,y) et la rend pair (avec une variation maximal de la valeur initial de ±1)
    
    inputs:
    - 1 string (PNG file)
    - 1 int (coordonnée x)
    - 1 int (coordonnée y)
    
    output:
    - None (la valeur R du pixel (x,y) aura été changé mais aucun return)
    
    
    """
    color = img.getpixel((x, y))
    
    if color[0] == 255:
        color = (color[0] - 1, color[1], color[2])
    else:
        if color[0] % 2 == 1:
            color = (color[0] + 1, color[1], color[2])
    
    img.putpixel((x, y), color)




def numeriser_message(message):
    """
    Cette fonction reçoit un message et renvoie une liste.
    Chaque élément de la liste est la valeur numérique en ascii d'un caractère du message.
    Les éléments de la liste sont dans le même ordre que les caractères du message.
    
    input:
    - string (message choisi)
    
    output:
    - return 1 list of int (charactères du message numérisé en ascii et intégré dans la liste)
    

    """
    message_en_ascii = []
    for i in range(len(message)):
        message_en_ascii.append(ord(message[i]))
    return message_en_ascii




def liste_coordonnées_alea(hauteur, n_coord_aléa):
    """
    
    Cette fonction reçoit une hauteur d'image ainsi qu'un int x (x représentant à chaque fois la valeur ascii d'un caractère du message)
    Elle renvoie une nouvelle liste de x éléments entiers différents appartenant à l'intervalle [0, hauteur].
    Les x sont choisis aléatoirement.
    
    inputs:
    - int (hauteur de l'image)
    - int (valeurs ascii d'un caractère)
    
    output:
    - return lisste d'int d'une longeur égale à la valeur du 2ème input.
    """
    liste_des_valeurs_y_possible = []
    for i in range(0, hauteur):
        liste_des_valeurs_y_possible.append(i)
    coordonnées_alea = random.sample(liste_des_valeurs_y_possible, n_coord_aléa)
    return coordonnées_alea




def cache_nombre_sur_une_colonne(img,x,message):
    """
    Cette fonction reçoit une image ainsi qu'un int x.
    L'int x indique qu'on veut cacher le x-ème élément du message (d'où le rapelle de la fonction numeriser_message())
    
    Le programme run la fonction listes_coordonnées_alea(hauteur,n_coord_aléa) avec:
    - 1er argument la hauteur de l'image.
    - 2ème argument la valeur int k du x-ème caractère du message en ascii

    La fonction listes_coordonnées_alea() resort d'une une liste de longeur k contenant des coordonnées possible de y différentes.
    Puis, le programme prend les pixels de coordonnés (x,y), avec plusieurs y, et rend la valeur R du pixel impair.
    
    
    inputs:
    - string (png file)
    - int x (pour cacher le x-ème caractère du message)
    - string (message)
    
    output:
    - None (la valeur R de y pixels sur la colonne x est changée en impair)
    """
    largeur, hauteur = img.size    
    for i in liste_coordonnées_alea(hauteur, numeriser_message(message)[x]):
        red, green, blue, alpha = img.getpixel((x,i))
        red = red + 1
        img.putpixel((x,i),(red, green, blue,alpha))




def cacher_message(image_to_change,message,image_changed):

    """
    
    Cette fonction demande comme premier argument le nom du fichier png de l'image dans laquelle l'utilisateur veut cacher un message.
    Le 2ème argument est le message que l'utilisateur veut cacher.
    Le 3ème argument est le nom du fichier png dans lequel l'image modifiée sera enregistrée.
    
    Si le message est plus long que la largeur de l'image, le message est trop long et la fonction échoue.
    Sinon, le programme utilise la fonction changeRGB pour rendre tout les pixels pair.
    Ensuite, elle appelle la fonction cache_nombre_sur_une_colonne(img,x).
    Elle fait varier x sur toute la longeur du message pour cacher ainsi l'entièreté du message dans l'image.
    Finalement, le programme enregistre cette image modifié dans le nom du nouveau fichier png que l'utilisateur aura choisi.
    
    inputs:
    - string (png file que l'utilisateur veut utiliser pour cacher le message)
    - string (message que l'utilisateur veut cacher)
    - string (nom du nouveau fichier png où l'utilisateur veut enregistrer l'image modifiée)
    
    output:
    - string (png file, image avec le message caché à l'interieur)
    """
        
    img = Image.open(image_to_change)
    largeur, hauteur = img.size
    
    if len(message) > largeur:
        print("Votre message est trop long pour l'image")
    else:
        for x in range(largeur):
            for y in range(hauteur):
                changeRGB(img,x,y)

        for x in range(len(message)):
            cache_nombre_sur_une_colonne(img,x,message)
        
        img.save(image_changed)

        img.close()
    

"""
The path of the righteous man is beset on all sides By the inequities of the selfish and the tyranny of evil men Blessed is he who, in the name of charity and good will Shepherds the weak through the valley of darkness For he is truly his brother's keeper and the finder of lost children And I will strike down upon thee With great vengeance and furious anger Those who attempt to poison and destroy my brothers And you will know my name is the Lord When I lay my vengeance upon thee
"""


message = input("Ecris-moi le message que tu veux cacher dans l'image: ")

image_to_change = input("Ecris-moi le nom du fichier png de l'image où tu veux cacher un message: ")

image_changed = input("Ecris le nom du fichier dans lequel ton image modifiée sera enregistrée: ")

cacher_message(image_to_change,message,image_changed)
print("Hello")