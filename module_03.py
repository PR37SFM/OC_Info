import logging





def letter_to_octet (letter):
    letter_in_decimal = ord (letter)
    letter_in_binary = bin (letter_in_decimal)
    letter_in_binary = letter_in_binary[2:]
    while len (letter_in_binary) < 8:
        letter_in_binary = '0' + letter_in_binary
    return letter_in_binary

def octet_to_letter (octet):
    octet_to_int = int (octet, 2)
    octet_to_char = chr (octet_to_int)
    return octet_to_char

"""
  '0' - blue pair : pas de modification
  '0' - blue impair : on enleve 1 (255->254, 1->0)
  '1' - blue pair : on ajoute 1 (0->1, 254->255)
  '1' - blue impair : pas de modification
"""
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

"""
    letter_in_decimal = ord (letter)
    letter_in_binary = bin (letter_in_decimal)
    letter_in_binary = letter_in_binary[2:]
    while len (letter_in_binary) < 8:
        letter_in_binary = '0' + letter_in_binary
    return letter_in_binary
"""

#print (letter_to_octet ('a'))
#print (letter_to_octet ('ä'))
#print (letter_to_octet ('#'))
#print (octet_to_letter ('01100001'))
#print (octet_to_letter ('11100100'))
#print (octet_to_letter ('00100011'))

"""
print (modify_pixel ((12,12,12), '0'))
print (modify_pixel ((12,12,13), '0'))
print (modify_pixel ((12,12,0), '0'))
print (modify_pixel ((12,12,255), '0'))
print (modify_pixel ((12,12,12), '1'))
print (modify_pixel ((12,12,13), '1'))
print (modify_pixel ((12,12,0), '1'))
print (modify_pixel ((12,12,255), '1'))
"""

bit_in_pixel ((12,12,12))
bit_in_pixel ((12,12,13))
bit_in_pixel ((12,12,0))
bit_in_pixel ((12,12,255))
bit_in_pixel ((12,12,12))
bit_in_pixel ((12,12,13))
bit_in_pixel ((12,12,0))
bit_in_pixel ((12,12,255))