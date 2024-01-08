from PIL import Image


def compter_impair_colonne(x,img):
    """
    Cette fonction reçoit un int x (x représentant une colonne de l'image) et un string (le nom du fichier png de l'image qu'il veut décrypter).
    Cette fonction regardera la valeur R de chaque pixel de la colonne x et compte le ombre d'impair de la colonne.
    Elle renvoie le nombre de valeur R impair de la colonne x.
    
    inputs:
    - int x (x-ème colonne de l'image)
    - string (png file to solve)
    
    output:
    - int (nombre de R impair sur la colonne x)
    """
    n_red_impair = 0
    largeur, hauteur = img.size
    for i in range(hauteur):
        red, green, blue,alpha = img.getpixel((x,i))
        if red%2 == 1:
            n_red_impair = n_red_impair + 1
    return n_red_impair


def decoder_message(image_to_solve):
    """
    Cette fonction reçoit l'image dont il en faut extracter le message caché.
    Elle fait appelle à la fonction compter_impair_colonne (x,img).
    Pour chaque return, elle transforme l'int n_red_impair et utilise chr() pour extracter le caractère que l'int représente.
    La fonction ajoute chacun de ces caractères dans l'ordre dans une nouvelle string nommée message.
    Après avoir parcourut la longeur de l'image, la fonction return la string message contenant le message caché.
    
    input:
    - string (png file to solve)
    
    output:
    - string (message caché)
    """
    message = ""
    img = Image.open(image_to_solve)
    largeur, hauteur = img.size
    for x in range(largeur):
        message += chr(compter_impair_colonne(x,img))
    return message




image_to_solve = input("Donne moi le nom du fichier qui contient le message caché: ")

print(decoder_message(image_to_solve))