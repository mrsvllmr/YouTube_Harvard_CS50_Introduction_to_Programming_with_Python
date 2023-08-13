import sys
from PIL import Image

# goal: create a gif

images = []

# iterate cli arguments (except file name) and append images to the list
for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

# save the file to disk
images[0].save(
    "costumes.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)
