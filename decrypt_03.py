from PIL import Image
import logging
from module_03 import bit_in_pixel, octet_to_char, input_filename

logging.basicConfig(level=logging.INFO)

image_in_filename = input_filename("Entrez le path de l'image :")

logging.info('open image=%s', image_in_filename)
image = Image.open(image_in_filename)
logging.info('image height=%s width=%s size=%s', image.height, image.width, image.size)
image = image.convert('RGB')

message = ''
octet = ''
coord_x = 0
coord_y = 0
eom_found = 0

while True:
    pixel = image.getpixel((coord_x, coord_y)) 
    bit = bit_in_pixel (pixel)
    octet = octet + bit
    if len(octet) == 8:
        if octet == '00000000':
            eom_found = 1
            break
        else:
            char = octet_to_char(octet)
            logging.info('octet=%s char=%s coord=%s', octet, char, (coord_x, coord_y))
            message = message + char
            octet = ''
    # coord of next pixel
    coord_x = coord_x + 1
    if coord_x == image.width:
        coord_x = 0
        coord_y = coord_y + 1
    if coord_y == image.height:
        break

logging.info('eom_found=%s', eom_found)
        
if eom_found == 1:
    print(message)
else:
    print('pas de message')
