import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
import itertools as it
from matplotlib.animation import FuncAnimation 
import cv2

plt.rcParams['figure.figsize'] = (14,7)

f_name = 'pil_brightness_15.jpg'
im_data = plt.imread(f_name)
print(im_data)

gray_img = cv2.cvtColor(im_data, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_img,cmap='gray')

kernel = np.array([[-1,-1,-1],
                   [-1,1,-1],
                   [-1,-1,-1]])

edited_img = signal.convolve2d(gray_img,kernel,mode='same')
plt.imshow(edited_img,cmap='gray')