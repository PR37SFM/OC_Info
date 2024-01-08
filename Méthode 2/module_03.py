import os
from PIL import Image

def char_to_octet (char):
    """
    Cette fonction prends le paramètre char, qui represente un caractère dans la chaine de caractère du message entré, et va le transformer en octet, suivant sa valeur décimal en ASCII.
    Elle prend en compte uniquement ce paramètre et renvoie sa forme 'char' en binaire (en octet).
    
    inputs:
    - 1 string (caractère du message entré)
    
    output:
    - 1 string (chaine de caractère, étant l'octet du caractère tranformé)
    """
    # convert to binary
    char_int = ord (char)
    char_octet = bin (char_int)
    # remove 2 first chars (0b)
    char_octet = char_octet[2:]
    # add 0 before to have exactly 8 chars
    while len(char_octet) < 8:
        char_octet = '0' + char_octet
    # return result
    return char_octet

def octet_to_char (octet):
    """
    Cette fonction prends le paramètre octet, qui est la transcription d'un caractère du message caché en binaire, et va la transformer en caractère ASCII selon ce que l'octet donne decimal, puis en symbole.
    Elle prend en compte uniquement ce paramètre et renvoie sa forme binaire (octet) en caractère.
    
    inputs:
    - 1 string (octet trouvé par le programme)
    
    output:
    - 1 string (le caractère que l'octet représentait)
    """
    octet_int = int (octet, 2)
    octet_char = chr (octet_int)
    return octet_char

def modify_pixel (pixel, bit):
    """
    Cette fonction prends le paramètre pixel car il s'agit ici de determiner la parité de la valeur bleu du pixel.
    Cette fonction prends aussi en compte le paramètre bit, qui ne peut que '0' ou '1' dans l'octet trouvé plus haut, car il permet de savoir si la valeur bleu du pixel doit être pair (si le bit a pour valeur '0') ou être impair (si le bit a pour valeur '1').    
    Elle prend ces deux paramètres et renvoie une valeur bleu changé ou inchangé.
    
    inputs:
    - 1 string (bit de l'octet)
    - 1 int (valeur bleu du pixel)
    
    output:
    - 1 int (nouvelle valeur bleu du pixel)
    """
    old_blue = pixel[2]
    if bit == '0':
        if old_blue%2 == 0: new_blue = old_blue
        else: new_blue = old_blue - 1
    else:
        if old_blue%2 == 0: new_blue = old_blue + 1
        else: new_blue = old_blue
    return (pixel[0], pixel[1], new_blue)

def bit_in_pixel (pixel):
    """
    Cette fonction permet de trouver, par l'analyse de la parité de la valeur du pixel, si le bit et '0' (si pair) ou '1' (si impair).
    Donc il ne prends en compte uniquement le pixel pour renvoyer un bit.
    
    inputs:
    - 1 int (valeur bleu du pixel)
    
    output:
    - 1 string (bit qui va être ajouté à l'octet)
    """
    blue = pixel[2]
    if blue%2 == 0:
        return '0'
    else:
        return '1'
    
def input_text(message, min_length, max_length):
    """
    Cette fonction sert à demander à l'utilisateur du programme un message (text) à dissimuler dans une image, sans que celui-ci ne soit trop petit (len(message) == 0) ou trop grand (superieur à la taille que l'image peut dissimuler).
    Il prends donc comme paramètre le message, qui demande à l'utilisateur quel est le message à dissimuler afin connaitre la taille qu'il represente, d'ou les deux autres paramètres, la longueur max et min du message.
    La longueur max du message a été calculé ultérieurement, il s'agit du nombre de pixel de l'image
    
    inputs:
    - 1 string (message de demande (quel est le message ?))
    - 2 int (longueur maximum et minimum du message, pour qu'il soit valide)
    
    output:
    - 1 string (le message validé par la fonction)    
    """
    text = input(message)
    while len(text) < min_length or len(text) > max_length:
        print(f'! text must have length between {min_length} and {max_length}')
        text = input(message)
    return text
    
def input_filename(message):
    """
    Cette fonction sert à ce que ce programme et python puisse acceder à l'image pour y dissimuler le message.
    Il ne prend donc en paramètre uniquement le message qui demande à l'utilisateur le lieu où se trouve l'image, soit le 'path'.
    
    inputs:
    - 1 string (message de demande)
    
    output:
    - 1 string (nom de l'image)    
    """
    filename = input(message)
    while not os.path.isfile(filename):
        print(f'! file {filename} not found')
        filename = input(message)
    return filename

#def input_new_filename(message, directory):
#    filename_out = input(message)
#    while len(filename_out) == 0:
#        print(f'! text is empty')
#        filename_out = input(message)
#    filename_out = filename_out + '.png'
#    return filename_out



def encrypt_image(image, message):
    """
    Cette fonction va cacher le message dans les valeur (couleur) des pixel de l'image.
    Pour cela, le programme a besoin d'un message et d'une image.

    inputs:
    - 2 string (nom de l'image et message)
    
    output:
    - 1 string (nom de l'image avec les valeurs des couleurs des pixels modifiés)
    """
    image = image.convert('RGB')
    
    # ajouter le caractere de fin au message
    message = message + chr(0)
    coord_x = 0
    coord_y = 0
    
    for char in message:
        octet = char_to_octet(char)
        for bit in octet:
            old_pixel = image.getpixel((coord_x, coord_y))
            new_pixel = modify_pixel (old_pixel, bit)
            image.putpixel((coord_x, coord_y), new_pixel)
            # coordonnées du prochain pixel
            coord_x = coord_x + 1
            if coord_x == image.width:
                coord_x = 0
                coord_y = coord_y + 1

    return image     
    

def decrypt_image(image):
    """
    Cette fonction va retrouver le message caché dans l'image. Pour ce faire, il a besoin du path de l'image sous forme .png et déposé dans OC info, ou sinon du path (input).
    Elle a donc uniquement besoin de son nom comme paramètre pour y acceder et retrouver le message.

    inputs:
    - 1 string (nom de l'image)
    
    output:
    - 1 string (message caché)
    """
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
        # quand la taille = 8
        if len(octet) == 8:
            # si la fin du message stopper la boucle
            if octet == '00000000':
                eom_found = 1
                break
            # convertir en caractère, et recommencer
            else:
                char = octet_to_char(octet)
                message = message + char
                octet = ''
        # coordonnées du prochain pixel
        coord_x = coord_x + 1
        if coord_x == image.width:
            coord_x = 0
            coord_y = coord_y + 1
        # si c'est la fin de l'image, stopper
        if coord_y == image.height:
            break
            
    if eom_found == 1:
        return message
    else:
        return ''
