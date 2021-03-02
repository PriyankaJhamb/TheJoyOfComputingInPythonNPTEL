# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 17:50:00 2021

@author: DELL
"""
def binary_search(l,f,start,end):
    
    if start==end:
        if l[start]==f:
            print(f," is found at position", start+1)
        else:
            print("Element not found.")
    else: 
        mid=int((start+end)/2)                  
        if l[mid]==f:
            print(f," is found at position", mid+1)
        elif (l[mid]>f):
            binary_search(l,f,start, mid-1)
        elif (l[mid]<f):
            binary_search(l,f,mid+1, end)
        else:
            print("Not found")
        
l=[]
print("How many elements you have to put in the list: ")
length=int(input())
print("Enter element in the list: ")
for i in range(length):
    p=int(input())
    l.append(p)
    
l.sort()    
                
f=int(input('Enter what you want to find: '))
binary_search(l,f,0, len(l)-1)
