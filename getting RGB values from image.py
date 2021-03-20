# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:01:44 2021

@author: DELL
"""

from PIL import Image
im=Image.open("test1.png")
#convert image to RGB values
rgb_img=im.convert('RGB')
r, g, b=rgb_img.getpixel((1,1))
print(r, g, b)
r, g, b=rgb_img.getpixel((150,1))
print(r, g, b)