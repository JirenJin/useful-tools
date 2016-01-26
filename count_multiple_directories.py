import os
import sys

dirs = sys.argv[1:]
count = 0

for dir_name in dirs:
    count += len([name for name in os.listdir(dir_name) if os.path.isfile(os.path.join(dir_name,name))])
print count
