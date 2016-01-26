import os

dir_list = os.listdir(".")

for dir_name in dir_list:
    if os.path.isdir(dir_name):
        image_list = os.listdir("./" + dir_name)
        print dir_name
        for image in image_list:
            if "0x2" in image:
                source_dir = dir_name + "/" + image
                dest_dir = "./blur-2"
                os.system("cp " + source_dir + " " + dest_dir)
            elif "0x6" in image:
                source_dir = dir_name + "/" + image
                dest_dir = "./blur-6"
                os.system("cp " + source_dir + " " + dest_dir)
            elif "0x10" in image:
                source_dir = dir_name + "/" + image
                dest_dir = "./blur-10"
                os.system("cp " + source_dir + " " + dest_dir)
            elif "0x8" in image:
                source_dir = dir_name + "/" + image
                dest_dir = "./blur-8"
                os.system("cp " + source_dir + " " + dest_dir)
            elif "0x4" in image:
                source_dir = dir_name + "/" + image
                dest_dir = "./blur-4"
                os.system("cp " + source_dir + " " + dest_dir)
            else:
                source_dir = dir_name + "/" + image
                dest_dir = "./good_images"

                if dir_name != "good_images":
                    os.system("cp " + source_dir + " " + dest_dir)
