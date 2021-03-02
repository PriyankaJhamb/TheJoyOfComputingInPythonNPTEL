# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:47:20 2021

@author: DELL
"""

def fibonacci(n):
    if(n<2):
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(10))