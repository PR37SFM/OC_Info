import os
from PIL import Image
from module_03 import char_to_octet, modify_pixel, input_text, input_filename, encrypt_image

#image_in_filename = input_filename("Entrez le path de l'image :")
image_in_filename = './nature.png'
image_in = Image.open(image_in_filename)

max_length = int(image_in.height*image_in.width/8)
max_length = max_length - 1 # car on rajouter le end of message
#message = input_text('Entrez le message :', 1, max_length)
message = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque blandit leo ut euismod consectetur. Ut lobortis dolor vel orci commodo, nec accumsan dui lobortis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Donec arcu ipsum, placerat a arcu non, dapibus sodales sem. Suspendisse convallis nunc diam, sit amet sagittis erat laoreet eleifend. Sed varius est sed dictum fermentum. Interdum et malesuada fames ac ante ipsum primis in faucibus. Nulla lacus lorem, convallis nec lectus non, ornare auctor nibh. Phasellus varius mauris erat, quis commodo ipsum interdum in. Cras id dolor orci. Nunc ex augue, sollicitudin non dictum ac, vestibulum id sem. Sed at pretium est. Aliquam erat volutpat. Cras porttitor turpis sed dignissim aliquet. Vivamus placerat posuere nulla eget faucibus.

Donec in orci ex. Sed pulvinar massa elit, mattis ultricies lorem finibus et. In hac habitasse platea dictumst. Duis sed mollis est, congue egestas lorem. Duis eu volutpat mauris. Suspendisse quis sapien faucibus erat fermentum ultrices non iaculis lectus. Maecenas mollis bibendum est, ac dignissim risus imperdiet et. Cras dignissim ultricies ex, sit amet tempus nulla egestas at. Maecenas in neque vel dolor porttitor efficitur. Cras pulvinar libero quis nisi pulvinar efficitur at vel sem. Nullam feugiat nibh porttitor, volutpat sapien ac, vehicula leo. Donec pulvinar cursus dolor quis dignissim. Proin luctus sed libero nec lobortis. Quisque porttitor ullamcorper ex, ac porttitor libero eleifend sit amet.

In convallis turpis ornare neque convallis iaculis. Suspendisse ultrices augue turpis, quis rhoncus orci suscipit eu. Duis nec sem id mauris blandit rhoncus a ac neque. Aenean ullamcorper in massa id viverra. Ut laoreet lorem vestibulum, sodales erat ut, imperdiet erat. Nulla facilisi. Fusce sit amet dui nec felis accumsan elementum. Nam ac cursus nisl. Aenean libero mauris, porttitor lacinia vestibulum sed, maximus eleifend massa. Nulla et turpis ut sem fermentum feugiat ornare quis ipsum. Nam fermentum commodo risus at elementum. Nam sed sapien ac ex efficitur volutpat. Phasellus sem tellus, rutrum sed ultrices at, ultricies id turpis. Quisque laoreet ultricies aliquam. Duis id molestie sapien, nec commodo tortor. Nulla facilisi.

Donec porttitor erat non erat scelerisque ornare. Nulla ac velit cursus, commodo massa vitae, lacinia risus. Sed nec ipsum mi. Maecenas varius sapien nec felis tempus, ut aliquet sem rhoncus. Nam malesuada sit amet augue eget egestas. Aliquam in urna quis lorem mollis bibendum. Donec ut mauris vehicula, vestibulum ex at, convallis nisl. In dapibus commodo convallis. Nam in sapien nulla. Aliquam venenatis, magna ut elementum finibus, lorem libero fermentum arcu, quis placerat urna est non est. Morbi efficitur nunc sapien, vel rutrum felis imperdiet nec. Phasellus vulputate eu lectus in scelerisque. Pellentesque tortor justo, ornare at justo id, ultricies auctor orci. Morbi auctor non enim dignissim iaculis. Curabitur in condimentum lectus. Ut rhoncus ante in augue laoreet, vel pharetra arcu maximus.

Quisque eleifend purus non magna aliquet, a varius erat euismod. Mauris non pellentesque augue. Morbi finibus varius ex in eleifend. Mauris euismod nibh et ex ornare aliquet. Sed rhoncus pellentesque eros, in sagittis dolor. Nunc eu nibh vel quam pretium auctor a eget lacus. Aenean non dolor id tellus faucibus varius. Aenean felis urna, tincidunt et tempus ac, luctus in leo. Ut et ultrices magna. Vestibulum mattis nisi sit amet mi commodo, sagittis maximus eros ultricies. Nam iaculis tempus fringilla. Donec pretium quam nec ligula dictum laoreet. Nam volutpat lacus vitae interdum commodo. Duis tortor enim, blandit nec purus ut, faucibus elementum risus.
"""

#image_out_filename = input("Entrez le nouveau nom de l'image :")
image_out_filename = ''
if len(image_out_filename) == 0:
    basename_with_ext = os.path.basename(image_in_filename)
    image_out_filename = basename_with_ext[:-4]
    image_out_filename = image_out_filename + '_modified'
if not image_out_filename.endswith('.png'):
    image_out_filename = image_out_filename + '.png'
image_out_filename = os.path.dirname(image_in_filename) + '/' + image_out_filename

image_out = encrypt_image(image_in, message)
image_out.save(image_out_filename)
print(f'image sauvegardé en {image_out_filename}')
