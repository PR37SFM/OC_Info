#CODAGE

from PIL import Image
import logging

#Etape 1 : créer un alphabet de a-z + A-Z + numéro + caractère spéciaux visibles (/!\ pas ceux non visibles et inutiles).

Alphabet = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
print(Alphabet[2])

#Etape 2 : attribuer à chaque caractère un nombre impaire. /!\ pas dépasser 255. Puis transformer message.

logging.basicConfig(level=logging.INFO)

image_in_filename = 'google.png'                                            #input
image_out_filename = 'google_changed.png'                                   #input
message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'        #input

logging.info('open image=%s', image_in_filename)
image = Image.open(image_in_filename)
logging.info('image height=%s width=%s size=%s', image.height, image.width, image.size)
image = image.convert('RGB')

len_message = len(message)
coord_x = 19
coord_y = 10
old_pixel = image.getpixel((coord_x,coord_y))
old_green = old_pixel[1]
new_green = len_message
new_pixel = (old_pixel[0], new_green, old_pixel[2])
image.putpixel((coord_x,coord_y), new_pixel)
logging.info('message size=%s x=%s y=%s og=%s ng=%s', len_message, coord_x, coord_y, old_green, new_green)

index = 0
for letter in message:
    coord_x = 20 + index
    coord_y = 10
    old_pixel = image.getpixel((coord_x,coord_y))
    old_green = old_pixel[1]
    new_green = ord(letter)
    new_pixel = (old_pixel[0], new_green, old_pixel[2])
    image.putpixel((coord_x,coord_y), new_pixel)
    logging.info('lettre traité =%s x=%s y=%s og=%s ng=%s', letter, coord_x, coord_y, old_green, new_green)
    index = index + 1

logging.info('write image=%s', image_out_filename)
image.save(image_out_filename)



#Etape 3 : rendre R-G-B-A tous pair en faisant +1 lorsque impaire.

#Etape 4 : fonction qui traite chaque ligne vertical de l'image, une par une, caractère par caractère.

#Etape 5 : compare chaque valeur R-G-B-A de tous les pixels de la ligne avec valeur numérique du message.

#Etape 6 : pixel dont la valeur est la plus proche de celle du message est remplacé.

#Etape 7 : renvoi l'image avec tout le message caché dans chaque ligne vertical de l'image dans le sens -> horinzontal.