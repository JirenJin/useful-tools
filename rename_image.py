import os
import sys

image_pre = sys.argv[1]
image_list = sorted(os.listdir("."))
image_num = 0
for image in image_list:
    image_ext = os.path.splitext(image)[1]
    if image_ext.lower() in ('.jpg', '.jpeg', '.png', '.gif'):
        image_pre = '{:0>5}'.format(str(image_pre))
        image_name = image_pre + image_ext
        os.rename(image, image_name)
        image_pre = int(image_pre)
        image_pre += 1
        image_num += 1
print("%d images renamed.") % image_num
