
from module_03 import char_to_octet, octet_to_char, modify_pixel, bit_in_pixel

assert char_to_octet ('a') == '01100001'
assert char_to_octet ('ä') == '11100100'
assert char_to_octet ('#') == '00100011'

assert octet_to_char ('01100001') == 'a'
assert octet_to_char ('11100100') == 'ä'
assert octet_to_char ('00100011') == '#'

assert modify_pixel ((12,12,12), '0') == (12,12,12)
assert modify_pixel ((12,12,13), '0') == (12,12,12)
assert modify_pixel ((12,12,0), '0') == (12,12,0)
assert modify_pixel ((12,12,255), '0') == (12,12,254)
assert modify_pixel ((12,12,12), '1') == (12,12,13)
assert modify_pixel ((12,12,13), '1') == (12,12,13)
assert modify_pixel ((12,12,0), '1') == (12,12,1)
assert modify_pixel ((12,12,255), '1') == (12,12,255)

assert bit_in_pixel ((12,12,12)) == '0'
assert bit_in_pixel ((12,12,13)) == '1'
assert bit_in_pixel ((12,12,0)) == '0'
assert bit_in_pixel ((12,12,255)) == '1'
