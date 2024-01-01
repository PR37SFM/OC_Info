from PIL import Image
import logging
from module_03 import bit_in_pixel, octet_to_letter

logging.basicConfig(level=logging.INFO)

image_in_filename = 'google_changed.png'

logging.info('open image=%s', image_in_filename)
image = Image.open(image_in_filename)
logging.info('image height=%s width=%s size=%s', image.height, image.width, image.size)
image = image.convert('RGB')

coord_x = 0
coord_y = 0
binary = ''
message = ''
end_message = 0

while end_message == 0:
    pixel = image.getpixel((coord_x, coord_y)) 
    bit = bit_in_pixel (pixel)
    binary = binary + bit
    if len (binary) == 8:
        if binary == '00000000':
            end_message = 1
        else:
            letter = octet_to_letter (binary)
            logging.info('binary=%s letter=%s', binary, letter)
            message = message + letter
            binary = ''
    # coordinate of next pixel
    coord_x = coord_x + 1
    if coord_x == image.width:
        coord_x = 0
        coord_y = coord_y + 1





"""
for coord_y in range(image.height):
    if end_message == 1: break
    for coord_x in range(image.width):
        if end_message == 1: break
        pixel = image.getpixel((coord_x, coord_y))
        bit = bit_in_pixel (pixel)
        letter_in_binary = letter_in_binary + bit
        if len (letter_in_binary) == 8:
            if letter_in_binary == '00000000':
                end_message = 1
            else:
                letter = octet_to_letter (letter_in_binary)
                logging.info('binary=%s letter=%s', letter_in_binary, letter)
                message = message + letter
                letter_in_binary = ''
"""


print (message)
