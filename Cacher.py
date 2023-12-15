from PIL import Image

image_to_change = "lapin.jpeg"
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

for x in range(largeur):
    for y in range(hauteur):
        changeRGB(x,y)
        print(img.getpixel((x,y)))

img.show()

valeur_numerique_des_lettres_du_message = []

message = "Farouk aura 18,5 l'année prochaine"

for i in range(len(message)):
    ord(i)