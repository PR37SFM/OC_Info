from PIL import Image
import logging
from module_03 import letter_to_octet, modify_pixel

logging.basicConfig(level=logging.INFO)


    
image_in_filename = 'google.png'
image_out_filename = 'google_changed.png'
message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut interdum urna ac erat efficitur varius. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin lacinia ligula vitae ante pharetra tincidunt. Vivamus quis tortor at nibh iaculis imperdiet a at turpis. Sed sit amet tristique felis, eget sagittis eros.'
#message = 'Lor'


logging.info('open image=%s', image_in_filename)
image = Image.open(image_in_filename)
logging.info('image height=%s width=%s size=%s', image.height, image.width, image.size)
image = image.convert('RGB')

coord_x = 0
coord_y = 0

message = message + chr(0)

for letter in message:
    binary = letter_to_octet (letter)
    logging.info('letter=%s binary=%s x=%s y=%s', letter, binary, coord_x, coord_y)
    for bit in binary:
        old_pixel = image.getpixel((coord_x, coord_y))
        new_pixel = modify_pixel (old_pixel, bit)
        image.putpixel((coord_x,coord_y), new_pixel)
        # logging.info('    letter=%s bin=%s bit=%s x=%s y=%s old=%s new%s', letter, binary, bit, coord_x, coord_y, old_pixel, new_pixel)
        # coordinate of next pixel
        coord_x = coord_x + 1
        if coord_x == image.width:
            coord_x = 0
            coord_y = coord_y + 1

logging.info('write image=%s', image_out_filename)
image.save(image_out_filename)
 
 
        

 







