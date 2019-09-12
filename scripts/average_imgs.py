import os
import sys
import numpy as np
import nibabel as nib

fpath = sys.argv[1]
img_list = os.listdir(fpath)
img_list = [os.path.join(fpath, x) for x in img_list]
print(img_list)

# for i in os.listdir(fpath):
