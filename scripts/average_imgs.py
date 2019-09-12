import os
import sys
import numpy as np
import nibabel as nib

fpath = sys.argv[1]
img_list = os.listdir(fpath)
img_list = [os.path.join(fpath, x) for x in img_list]

example_img = nib.load(img_list[0])
template = np.zeros(example_img.get_data().shape)
print(example_img.affine)

# for i in os.listdir(fpath):
#     template += nib.load(i).get_data()

# template = template / len(img_list)
# template_img = nib.Nifti1Image(template, example_img.affine)
