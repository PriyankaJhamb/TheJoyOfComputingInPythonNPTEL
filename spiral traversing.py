# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 14:43:40 2021

@author: DELL
"""

def spiralPrint(m, n, a):
    '''

    Parameters
    ----------
    m : number of rows
    n : number of columns
    a : list
    
    01 02 03 04
    05 06 07 08
    09 10 11 12 
    13 14 15 16
    
    Returns
    -------
    None.

    '''
    k=0 #k=starting index of rows
    l=0 #l=starting index of columns
    
    while (k<m and l<n):
        # printing the first row fromteh remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
            
        k+=1
        
        # printing the last full column from the remaining columns
        
        for i in range(k,m):
            print(a[i][n-1],end=" ")
            
        n-=1
        
        # Printing the last row from remaining rows
        if k<m:
            for i in range(n-1, l-1, -1):
                print(a[m-1][i], end=" ")
            
        m-=1
        
        #printing the first column from the remaining columns
        for i in range(m-1, k-1, -1):
            print(a[i][l], end=" ")
            
        l+=1

a=[]
count=1
for i in range(3):
    l=[]
    for j in range(6):
        l.append(count)
        count+=1
    a.append(l)
    
spiralPrint(3, 6,a)


    