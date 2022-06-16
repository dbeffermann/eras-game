from PIL import Image
import sys

#read the image
im = Image.open(f"{sys.argv[1]}")

#rotate image
angle = int(sys.argv[2])
out = im.rotate(angle)
out.save(f"{sys.argv[1].split('.')[0]}2.{sys.argv[1].split('.')[1]}")