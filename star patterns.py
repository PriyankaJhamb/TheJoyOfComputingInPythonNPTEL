# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 20:43:58 2021

@author: DELL
"""
def star_pattern(n):
   
    for i in range(1, n+1):
        for j in range(i):
            print('*', end="")
        print()
        
    i=0
    while i<n+1:
        j=0
        while j<i:
            print("*", end="")
            j=j+1
        print()
        i=i+1
        
    print()
    for i in range(n):
        for j in range(n):
            if j<i:
                print(" ", end="")
            else:
                print('*', end="")
        print()
        
    for i in range( n):
        for j in range(n):
            if j>i:
                print(" ", end="")
            else:
                print('*', end="")
        print()
    print()
        
    for i in range( n+1):
        for j in range(n-i):
            print('*', end="")
        print()
   
    for i in range(1,n+1):
        for j in range(n):
            if (j<n-i):
                print(' ',end="")
            else:
                print('*',end="")
        print()
    m=0
    while m<n+1:
        c=0
        while c<n:
            if (c<n-m):
                print(' ', end="")
            else:
                print('*', end="")
            c=c+1
        m=m+1
        print()
    
        
    
star_pattern(5)