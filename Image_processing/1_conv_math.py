# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 11:03:39 2023

@author: dhamu
"""

import numpy as np
from scipy.signal import convolve2d

a = np.array([1,5,9,8,7])
b = np.array([9,4,5,6,3])

print('mode = default',np.convolve(a, b))
print('mode = same',np.convolve(a,b,mode='same'))
print('mode = valid',np.convolve(a,b,mode='valid'))
print('mode = full',np.convolve(a,b,mode='full'))


print('===================================')

a2 = np.array([[1,2,4,5],
               [4,5,6,7],
               [5,6,9,7],
               [5,6,9,4]])

b2 = np.array([[4,1],
               [2,1]])

convolutional_data = convolve2d(a2,b2, mode='valid')
print(convolutional_data)
