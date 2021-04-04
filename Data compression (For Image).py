# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:32:31 2021

@author: Priyanka
"""

import numpy
from PIL import Image

im=Image.open('apple.jfif')
pixelMap=im.load()
I=numpy.asanyarray(Image.open("apple.jfif"))
print('I:',I)
#new image object, blank image, have no specific pixel values
img=Image.new(im.mode, im.size)
pixelNew=img.load()

'''
2^8=256  0 to 255
2^3=8     0 to 7
2^5=32    0 to 31

0-31=0
32-63=1
64-95=2
96-127=3
128-159=4
160-191=5
192-223=6
224-255=7

'''
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if (pixelMap[i,j]>=0 and pixelMap[i,j]<31):
            pixelnew[i,j]=0
        elif (pixelMap[i,j]>=32 and pixelMap[i,j]<=63):
            pixelnew[i,j]=1
        elif (pixelMap[i,j]>=64 and pixelMap[i,j]<=95):
            pixelnew[i,j]=2
        elif (pixelMap[i,j]>=96 and pixelMap[i,j]<=127):
            pixelnew[i,j]=3
        elif (pixelMap[i,j]>=128 and pixelMap[i,j]<=159):
            pixelnew[i,j]=4
        elif (pixelMap[i,j]>=160 and pixelMap[i,j]<=191):
            pixelnew[i,j]=5
        elif (pixelMap[i,j]>=192 and pixelMap[i,j]<=223):
            pixelnew[i,j]=6
        elif (pixelMap[i,j]>=224 and pixelMap[i,j]<=255):
            pixelnew[i,j]=7
                
            
img.save("apple_new.jpg")

j=numpy.asanyarray(Image.open("apple_new.jpg"))
print('j:',j)