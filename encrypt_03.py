import logging
import os
from PIL import Image
from module_03 import char_to_octet, modify_pixel, input_text, input_filename, input_new_filename

logging.basicConfig(level=logging.INFO)

#image_in_filename = '/Users/maison/Downloads/warga.png'

image_in_filename = input_filename("Entrez le path de l'image :")
logging.info('open image=%s', image_in_filename)
image = Image.open(image_in_filename)
logging.info('image height=%s width=%s size=%s', image.height, image.width, image.size)

max_length =  int(image.height*image.width/8)
max_length = max_length - 1 # last character is eom
logging.info('max_size=%s', max_length)
message = input_text('Entrez le message :', 1, max_length)

image_out_filename = input("Entrez le nouveau nom de l'image :")
if len(image_out_filename) == 0:
    basename_with_ext = os.path.basename(image_in_filename)
    image_out_filename = basename_with_ext[:-4]
    image_out_filename = image_out_filename + '_modified'
if not image_out_filename.endswith('.png'):
    image_out_filename = image_out_filename + '.png'
image_out_filename = os.path.dirname(image_in_filename) + '/' + image_out_filename

image = image.convert('RGB')

# add end char to message
message = message + chr(0)
coord_x = 0
coord_y = 0

for char in message:
    octet = char_to_octet(char)
#    logging.info('char=%s octet=%s coord=%s', char, octet, (coord_x, coord_y))
    for bit in octet:
        old_pixel = image.getpixel((coord_x, coord_y))
        new_pixel = modify_pixel (old_pixel, bit)
        image.putpixel((coord_x, coord_y), new_pixel)
        # logging.info('    bit=%s coord=%s old=%s new%s', bit, (coord_x, coord_y), old_pixel, new_pixel)
        # coord of next pixel
        coord_x = coord_x + 1
        if coord_x == image.width:
            coord_x = 0
            coord_y = coord_y + 1

logging.info('write image=%s', image_out_filename)
image.save(image_out_filename)
 