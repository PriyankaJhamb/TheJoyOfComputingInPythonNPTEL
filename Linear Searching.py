# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:27:44 2021

@author: DELL
"""
iterations=0
list_numbers=[]
n=int(input())
flag=0
for i in range(1001):
    list_numbers.append(i)
    
for i in list_numbers:
    iterations+=1
    if i==n:
        print("Yes , I found the number at the position : "+str(i))
        flag=1
        break
if flag==0:
     print("No, I did not find the number.")
print(iterations) 