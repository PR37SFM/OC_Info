from module_03 import char_to_octet, octet_to_char, modify_pixel, bit_in_pixel


def _test_char_to_octet():
    assert char_to_octet ('a') == '01100001'
    assert char_to_octet ('ä') == '11100100'
    assert char_to_octet ('#') == '00100011'
    assert char_to_octet ('') == '00000000'
    print("char_to_octet OK")

_test_char_to_octet()
