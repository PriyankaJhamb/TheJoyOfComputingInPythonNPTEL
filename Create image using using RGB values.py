# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 11:51:48 2021

@author: DELL
"""
import numpy as np
from PIL import Image
width=50
height=40
array=np.zeros([height,width,3],dtype=np.uint8)
#np.zeros make an array of given dimensions and 3 byte values for RGB
#Each byte dedicated to particular Red or blue or green
#datatype assigned=unsigned int

img=Image.fromarray(array)
img.save('test.png')


array1=np.zeros([100, 200, 3], dtype=np.uint8)
#for left
array1[:,:100]=[255, 200, 3]#orange
#for right
array1[:,100:]=[0, 0, 255]#blue color
img=Image.fromarray(array1)
img.save('test1.png')