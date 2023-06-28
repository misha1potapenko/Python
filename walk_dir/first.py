import os
from os.path import join, getsize

for root, dirs, files in os.walk('walk_dir', topdown=True, onerror=None, followlinks=False):
    print(root, "consumes", end=" ")
    print(dirs, end=" ")
    print(files)
