
def char_to_octet (char):
    char_int = ord (char)
    char_octet = bin (char_int)
    # remove 2 first chars (0b)
    char_octet = char_octet[2:]
    # add 0 to have exactly 8 chars
    while len (char_octet) < 8:
        char_octet = '0' + char_octet
    return char_octet

def octet_to_char (octet):
    octet_int = int (octet, 2)
    octet_char = chr (octet_int)
    return octet_char

"""
  bit '0' - blue even : already ok
  bit '0' - blue odd : remove 1 (255->254, 1->0)
  bit '1' - blue even : add 1 (0->1, 254->255)
  bit '1' - blue odd : already ok
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

#print (char_to_octet ('a'))
#print (char_to_octet ('ä'))
#print (char_to_octet ('#'))
#print (octet_to_char ('01100001'))
#print (octet_to_char ('11100100'))
#print (octet_to_char ('00100011'))

#print (modify_pixel ((12,12,12), '0'))
#print (modify_pixel ((12,12,13), '0'))
#print (modify_pixel ((12,12,0), '0'))
#print (modify_pixel ((12,12,255), '0'))
#print (modify_pixel ((12,12,12), '1'))
#print (modify_pixel ((12,12,13), '1'))
#print (modify_pixel ((12,12,0), '1'))
#print (modify_pixel ((12,12,255), '1'))

#bit_in_pixel ((12,12,12))
#bit_in_pixel ((12,12,13))
#bit_in_pixel ((12,12,0))
#bit_in_pixel ((12,12,255))
#bit_in_pixel ((12,12,12))
#bit_in_pixel ((12,12,13))
#bit_in_pixel ((12,12,0))
#bit_in_pixel ((12,12,255))

"""