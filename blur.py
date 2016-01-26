import os
import sys

# usage
# python blur.py "image_directory_name" "sigma"

image_dir = sys.argv[1]
radius = 0
sigma = sys.argv[2]
args = str(radius) + "x" + str(sigma)
blur_image_dir = image_dir + "_blur_" + args
if not os.path.exists(blur_image_dir):
    os.mkdir(blur_image_dir)

import time
start = time.time()
image_list = os.listdir(image_dir)
for image in os.listdir(image_dir):
    image_pre = os.path.splitext(image)[0]
    image_ext = os.path.splitext(image)[1]
    if image_ext.lower() in ('.jpg', '.jpeg', '.png', '.gif'):
        image = os.path.join(image_dir, image)
        image_pre = os.path.join(blur_image_dir, image_pre)
        os.system("convert -blur " + args + " " + image + " " + image_pre + "_blur_" + args + image_ext)

stop = time.time()

print (stop - start) / len(image_list)
