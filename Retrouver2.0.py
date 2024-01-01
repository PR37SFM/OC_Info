#DECODAGE

from PIL import Image
import logging

#Etape 1 : reformation de l'alphabet.

#Etape 2 : analyse de chaque valeur R-G-B-A de tout les pixels, puis prend la valeur impaire si il en trouve.

#Etape 3 : retranscription des valeurs trouvés en alphabet normal.

logging.basicConfig(level=logging.INFO)

image_in_filename = 'google_changed.png'


def get_message_length (image, cx, cy):
    pixel = image.getpixel((cx,cy))
    length = pixel[1]
    logging.info('message l=%s x=%s y=%s', length, cx, cy)
    return length

logging.info('open image=%s', image_in_filename)
image = Image.open(image_in_filename)
logging.info('image height=%s width=%s size=%s', image.height, image.width, image.size)
image = image.convert('RGB')




len_message = get_message_length (image, 19, 10) 

message = ''
index = 0
while index < len_message:
    coord_x = 20 + index
    coord_y = 10
    pixel = image.getpixel((coord_x,coord_y))
    green = pixel[1]
    letter = chr (green)
    logging.info('valeur traité x=%s y=%s g=%s l=%s', coord_x, coord_y, green, letter)
    message = message + letter
    index = index + 1

print(message)