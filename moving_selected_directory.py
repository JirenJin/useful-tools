import os

dir_list = os.listdir(".")

for dir_name in dir_list:
    if os.path.isdir(dir_name):
        if "not" in dir_name:
            os.system("cp " + dir_name + "/* ./bad_images")
        else:
            if dir_name != "good_images":
                os.system("cp " + dir_name + "/* ./good_images")
