#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import shutil

"""remove all subdirectories with name argv[1]."""
remove_dir_name = sys.argv[1]
dir_list = os.listdir(".")
for directory in dir_list:
    if os.path.isdir(directory):
        remove_path = os.path.join(directory, remove_dir_name)
        if os.path.exists(remove_path):
            shutil.rmtree(remove_path)
            print remove_path + " removed!"
