# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 12:04:35 2021

@author: DELL
"""


from PIL import Image

import random
img=Image.open("map.jfif")
rgb_im=img.convert("RGB")

count_punjab=0
count_india=0
count=0

while(count<=1000000):
    #breadth
    x=random.randint(0,299)
    #length
    y=random.randint(0,248)
    #2-dimensional
    z=0
    r,g,b= rgb_im.getpixel((y, x))
    if (r==248):
        count_india+=1
        count+=1
    else:
        if(r==180):
            count_punjab+=1
            count+=1
            
area_punjab=(count_punjab/count_india)*3287263

print(area_punjab)
    
