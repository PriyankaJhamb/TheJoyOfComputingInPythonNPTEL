# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 21:22:15 2021

@author: DELL
"""

# flipping the image
from PIL import Image
import cv2
#Opening the Image
img=Image.open('picture.jpg')
#transposing(flipping the image)
transposed_img=img.transpose(Image.FLIP_LEFT_UP)
#save it to a file in a human understandable format
transposed_img.save('Corected.png')
print('Done flipping')

#Image Enhancement technique  (CLAHE (Histogram Equilisation))
#Read the image
img=cv2.imread('wall.jpg')
#Preparation for CLAHE
clahe=cv2.createCLAHE()
#Convert it into gray scale image
gray_img=cv2.cvtColor(img, cv2Color_BGR2GRAY)
#Apply enhancement
enh_img=clahe.apply(gray_img)
#save it to a file
cv2.inwrite('enhanced.png', enh_img)
print("Done enhancing")