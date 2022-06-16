# Importing Image class from PIL module
from PIL import Image
import sys
# Opens a image in RGB mode
im = Image.open(f"{sys.argv[1]}")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

newsize = (int(sys.argv[2]), int(sys.argv[3]))
im1 = im.resize(newsize)#.transpose(Image.FLIP_LEFT_RIGHT)
# Shows the image in image viewer
im1.show()
im1.save(f"{sys.argv[1].split('.')[0]}2.{sys.argv[1].split('.')[1]}")


