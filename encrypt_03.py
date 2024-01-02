import logging
from PIL import Image
from module_03 import char_to_octet, modify_pixel

logging.basicConfig(level=logging.DEBUG)

image_in_filename = 'warga.png'
image_out_filename = 'warga_changed.png'
message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum eleifend lacus ac erat feugiat rhoncus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla fringilla in nisl non commodo. Mauris tincidunt nisi ut varius laoreet. Nulla sagittis pulvinar elementum. Cras ac mi sit amet odio vulputate iaculis at eget arcu. Sed tempor ante vitae lectus congue, in fringilla purus lobortis. Nam interdum vulputate metus, sit amet euismod eros porttitor in. Nulla massa sem, tempor non suscipit vitae, scelerisque quis elit. Donec tristique lectus eu massa ultrices, eu blandit orci eleifend.

Suspendisse leo justo, vulputate ut volutpat ut, faucibus et magna. Donec et luctus tellus. Sed convallis, mauris ut vestibulum venenatis, eros arcu vestibulum ex, ut molestie mi felis sit amet eros. Nullam suscipit luctus leo vel blandit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus id leo diam. Nam ut enim facilisis, fermentum nibh a, pulvinar nisi. Sed in gravida augue. Sed molestie maximus commodo. Phasellus mauris lectus, scelerisque ac lectus et, pharetra mattis nunc. Praesent id odio sed nunc cursus ultrices ac quis orci. Curabitur tristique commodo nibh, sit amet lobortis augue imperdiet a. Mauris tristique, mauris non elementum blandit, nibh orci sodales erat, eget congue neque odio eget leo.

Aenean dignissim vitae nibh sed porttitor. Praesent eget massa eu turpis ultrices convallis non a ipsum. Cras nec massa tincidunt, condimentum lectus et, auctor nisl. Vivamus molestie ullamcorper nisi vel semper. Curabitur aliquam vehicula nunc at aliquam. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In scelerisque purus orci, ac viverra nisi elementum vitae. Praesent aliquet leo pulvinar nunc faucibus accumsan. Nullam urna justo, suscipit et euismod in, ornare at nisi. Aenean molestie lectus ex. Morbi ante velit, venenatis ut dignissim et, porttitor vel felis. Fusce dapibus auctor tellus, id efficitur purus.

Sed vestibulum risus sapien, in convallis purus faucibus auctor. Pellentesque posuere ante vel mi gravida eleifend. Maecenas sit amet vestibulum purus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Suspendisse convallis tempus elit. Nunc ac neque et lacus cursus viverra. Fusce blandit cursus magna in lacinia. Nullam egestas id lacus vitae consequat. Aliquam tempor risus magna, vitae blandit nibh semper at. Pellentesque eget nisi in dolor rhoncus ornare. Fusce porta lacus a mauris aliquet, eget commodo diam pellentesque.

Morbi condimentum felis non ex eleifend, sed molestie dolor consectetur. Suspendisse dictum eu risus ac pretium. Vestibulum nec viverra est, ac finibus ligula. In egestas turpis eget mauris pellentesque egestas. Proin eget metus tincidunt, luctus urna vel, tincidunt orci. Morbi eu tortor vulputate, semper nibh id, condimentum diam. Ut sed mi vitae leo pulvinar placerat. Nullam aliquet augue neque.

In aliquam nunc sit amet ex posuere auctor. In hac habitasse platea dictumst. In nisi mauris, imperdiet et elit ut, ultricies eleifend urna. Pellentesque consequat imperdiet vehicula. Praesent blandit vitae libero id rutrum. Praesent sit amet cursus diam. Nulla nunc nisi, vehicula eu libero eget, feugiat ullamcorper urna. Curabitur id ante sem. Fusce ac massa urna. Sed blandit nibh ac metus molestie congue. Suspendisse potenti. Nunc quis neque luctus libero feugiat tincidunt in eget ex. Etiam posuere id tellus eget mattis. Ut vel nisi ac nisi bibendum porta. Curabitur volutpat lectus nec libero dictum, ut mollis ex accumsan. Duis pellentesque viverra purus.

Pellentesque maximus diam ac varius semper. Fusce condimentum, lacus ac hendrerit fringilla, tortor justo tincidunt ex, vel tristique leo nibh quis lacus. Pellentesque et dictum enim. Nunc lacinia, lacus in viverra tempor, magna purus ultricies dui, eget pellentesque lectus massa vitae tellus. Duis laoreet orci sed neque eleifend fringilla. Nam tincidunt porta posuere. Nulla varius dui arcu, eget accumsan nisl maximus in. Aliquam erat volutpat. Nam ornare ipsum non risus aliquam aliquam. Donec commodo metus ut faucibus blandit. Nullam nec quam dui. Mauris vel pellentesque eros. Suspendisse id scelerisque elit.

In hac habitasse platea dictumst. Ut porta malesuada metus, vel varius dolor lobortis at. Etiam ullamcorper odio quis turpis elementum pretium. Nullam eu orci posuere nibh luctus placerat. Nunc accumsan semper egestas. Phasellus in commodo nulla, eget viverra turpis. Nunc sit amet urna a orci varius pulvinar ut et mauris. Mauris felis dui, mollis at ex dapibus, egestas scelerisque eros. Morbi porta diam lorem, et venenatis ipsum ornare a. Nam fermentum est vel tristique interdum.
"""

logging.info('open image=%s', image_in_filename)
image = Image.open(image_in_filename)
logging.info('image height=%s width=%s size=%s', image.height, image.width, image.size)
image = image.convert('RGB')

# add end char to message
message = message + chr(0)
coord_x = 0
coord_y = 0

for char in message:
    octet = char_to_octet(char)
    logging.info('char=%s octet=%s coord=%s', char, octet, (coord_x, coord_y))
    for bit in octet:
        old_pixel = image.getpixel((coord_x, coord_y))
        new_pixel = modify_pixel (old_pixel, bit)
        image.putpixel((coord_x, coord_y), new_pixel)
        # logging.info('    bit=%s coord=%s old=%s new%s', bit, (coord_x, coord_y), old_pixel, new_pixel)
        # coord of next pixel
        coord_x = coord_x + 1
        if coord_x == image.width:
            coord_x = 0
            coord_y = coord_y + 1

logging.info('write image=%s', image_out_filename)
image.save(image_out_filename)
 