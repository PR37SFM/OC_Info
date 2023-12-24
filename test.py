from PIL import Image

liste_de_chaines = []

# Ajouter une chaîne de caractères initiale à la liste
chaine_initiale = "Bonjour"
liste_de_chaines.append(chaine_initiale)

# Ajouter des lettres à la chaîne de caractères
lettre_a_ajouter = "X"
chaine_modifiee = chaine_initiale + lettre_a_ajouter
liste_de_chaines.append(chaine_modifiee)

# Vous pouvez également ajouter des lettres directement à la dernière chaîne ajoutée
lettre_suivante = "Y"
liste_de_chaines[-1] += lettre_suivante

# Afficher le résultat
print(liste_de_chaines)



"""
from PIL import Image


def changeRGB(img:Image, x,y):
    
    
    Cette fonction prend la valeur R d'un pixel et la rend pair.
    
    color = img.getpixel((x, y))
    print(color[0])
    if color[0] == 255:
        color = (color[0] - 1, color[1], color[2])
    else:
        if color[0] % 2 == 1:
            color = (color[0] + 1, color[1], color[2])
    
    img.putpixel((x, y), color)
    
    

img =  img = Image.open("image.png")

largeur, hauteur = img.size

print(img.getpixel((600,600)))
help(Image.getpixel())


for x in range(largeur):
    for y in range(hauteur):
        changeRGB(img,x,y)
        print(img.getpixel((x,y)))
        
"""