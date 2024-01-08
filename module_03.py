import os

def char_to_octet (char):
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
    octet_int = int (octet, 2)
    octet_char = chr (octet_int)
    return octet_char

def modify_pixel (pixel, bit):
    old_blue = pixel[2]
    if bit == '0':
        if old_blue%2 == 0: new_blue = old_blue
        else: new_blue = old_blue - 1
    else:
        if old_blue%2 == 0: new_blue = old_blue + 1
        else: new_blue = old_blue
    return (pixel[0], pixel[1], new_blue)

def bit_in_pixel (pixel):
    blue = pixel[2]
    if blue%2 == 0:
        return '0'
    else:
        return '1'
    
def input_text(message, min_length, max_length):
    text = input(message)
    while len(text) < min_length or len(text) > max_length:
        print(f'! text must have length between {min_length} and {max_length}')
        text = input(message)
    return text
    
def input_filename(message):
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
