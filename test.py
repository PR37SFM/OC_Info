import os

# Get the current working directory
current_directory = os.getcwd()

# Combine the current directory with the image filename
image_filename = "image_changed.jpeg"
image_path = os.path.join(current_directory, image_filename)

print("Path to the image:", image_path)