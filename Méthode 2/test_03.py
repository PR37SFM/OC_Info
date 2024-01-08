from module_03 import char_to_octet, octet_to_char, modify_pixel, bit_in_pixel, input_text

def _test_char_to_octet():
    assert char_to_octet (' ') == '00100000'
    assert char_to_octet ('ÿ') == '11111111'
    assert char_to_octet ('#') == '00100011'
    assert char_to_octet ('~') == '01111110'
    print("char_to_octet OK")

_test_char_to_octet()

def _test_octet_to_char():
    assert octet_to_char ('00100000') == ' '
    assert octet_to_char ('11111111') == 'ÿ'
    assert octet_to_char ('00100011') == '#'
    assert octet_to_char ('01111110') == '~'
    print("octet_to_char OK")

_test_octet_to_char()

def _test_modify_pixel():
    assert modify_pixel ((12,12,12), '0') == (12,12,12)
    assert modify_pixel ((12,12,13), '0') == (12,12,12)
    assert modify_pixel ((12,12,0), '0') == (12,12,0)
    assert modify_pixel ((12,12,255), '0') == (12,12,254)
    assert modify_pixel ((12,12,12), '1') == (12,12,13)
    assert modify_pixel ((12,12,13), '1') == (12,12,13)
    assert modify_pixel ((12,12,0), '1') == (12,12,1)
    assert modify_pixel ((12,12,255), '1') == (12,12,255)
    print("modify_pixel OK")

_test_modify_pixel()

def _test_bit_in_pixel():
    assert bit_in_pixel ((12,12,12)) == '0'
    assert bit_in_pixel ((12,12,13)) == '1'
    assert bit_in_pixel ((12,12,0)) == '0'
    assert bit_in_pixel ((12,12,255)) == '1'
    print("bit_in_pixel OK")

_test_bit_in_pixel()

def _test_input_text():
    assert len (input_text ('entrez un message :', 1, 2)) > 0
    assert len (input_text ('entrez un message :', 1, 2)) == 1 or 2
    assert len (input_text ('entrez un message :', 1, 2)) < 3
    print("input_text OK")

_test_input_text()