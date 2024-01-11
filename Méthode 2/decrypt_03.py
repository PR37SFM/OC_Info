from PIL import Image
from module_03 import input_filename, decrypt_image

filename = input_filename("Entrez l'image :")
#filename = './nature_modified.png'
image = Image.open(filename)
message = decrypt_image(image)
if message == '':
    print('pas de message')
else:
    print(f'message trouvé : {message}')