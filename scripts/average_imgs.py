import os
import sys
import numpy as np
import nibabel as nib

fpath = sys.argv[1]
img_list = os.listdir(fpath)
img_list = [os.path.join(fpath, x) for x in img_list]

example_img = nib.load(img_list[0])
template = np.zeros(example_img.get_data().shape)

for i in img_list:
    template += nib.load(i).get_data()

n_imgs = len(img_list)
template = template / n_imgs
# template_flipped = np.fliplr(template)
# template = (template + template_flipped) / 2
template_img = nib.Nifti1Image(template, example_img.affine)
nib.save(template_img, os.path.join(fpath, f'template_{n_imgs}.nii.gz'))
