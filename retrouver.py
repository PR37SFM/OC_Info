from PIL import Image





def compter_impair_colonne (x,img):
    n_red_impair = 0
    largeur, hauteur = img.size
    for i in range(hauteur):
        red, green, blue,alpha = img.getpixel((x,i))
        if red%2 == 1:
            n_red_impair = n_red_impair + 1
    return n_red_impair


def decoder_message(image_to_solve):
    message = ""
    img = Image.open(image_to_solve)
    largeur, hauteur = img.size
    for x in range(largeur):
        message += chr(compter_impair_colonne(x,img))
    return message


 
image_to_solve = input("Donne moi le nom du fichier qui contient le message caché: ")

print(decoder_message(image_to_solve))