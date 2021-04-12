# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 11:18:22 2021

@author: DELL
"""
# 3n+1 problem
# Collatz Conjecture
def checkNum(num):
    iterations=1
    print(num, iterations)
    while(num!=1):
        if(num%2==0):
            num=int(num/2)
            iterations+=1
            print(num, iterations)
        else:
            num=(num*3)+1
            iterations+=1
            print(num, iterations)
        
    print("At Last",num, iterations)
    
checkNum(7)