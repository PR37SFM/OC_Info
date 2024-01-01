from PIL import Image
import logging

logging.basicConfig(level=logging.INFO)

image_in_filename = 'google.png'
image_out_filename = 'google_changed.png'
message = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit.'

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
