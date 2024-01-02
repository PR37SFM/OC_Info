

import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)
"""
answer = input('entrez oui :')
while answer.lower() != 'oui':
    answer = input('entrez oui :')
print (answer)


answer = ''
while 1==1:
    answer = input('entrez oui :')
    if answer.lower() == 'oui':
        break

print (answer)
"""


def input_name_file(message):
    filename_out = input(message)
    while len(filename_out) == 0 or filename_out[:4] != ".png":
        print('! text is empty or format ".png" not precised')
        text = input(message)
    
input_name_file('entrez nom fichier :')
