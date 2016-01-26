import os

directory_list = os.listdir(".")
for file_name in directory_list:
    if os.path.isdir(file_name):
        image_list = sorted(os.listdir("./" + file_name))
        image_num = 0
        for image in image_list:
            image_ext = os.path.splitext(image)[1]
            image_pre = os.path.splitext(image)[0]
            if image_ext.lower() in ('.png', '.jpg', '.jpeg', '.png', '.gif'):
                image_name = file_name + '_' + image_pre + image_ext
                os.rename("./" + file_name + "/" + image, "./" + file_name + "/" + image_name)
                image_num += 1
        print("%d images renamed.") % image_num
