# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:18:12 2021

@author: shyam
"""

import scipy.io
import numpy as np


mat = scipy.io.loadmat("eg_fix/Fixation_16.mat")
print(mat.keys())
print(np.where(mat["fixations"]==1))


mat1 = scipy.io.loadmat("eg_fix/COCO_train2014_000000000009.mat")
print(mat1.keys())
fixations_array = [gaze[2] for gaze in mat1['gaze'][:, 0]]
fix_map = np.zeros((480, 640), dtype=np.uint8)
for subject_fixations in fixations_array:
    fix_map[subject_fixations[:, 1] - 1, subject_fixations[:, 0] - 1] = 255
    
print(np.where(fix_map==255))