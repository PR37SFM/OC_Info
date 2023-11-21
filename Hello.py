from PIL import Image

image_to_change = "image/to/change.jpg"
img = Image.open(image_to_change)

#print("Image format:", img.format)
#print("Image mode:", img.mode)
#print("Image size:", img.size)
# pixel = image.getpixel((x, y))
#image.putpixel((x, y), new_color)

img.show()