from PIL import Image
import logging

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







"""
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
"""