# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:23:29 2021

@author: DELL
"""

import turtle
from random import randint
turtle.bgcolor("black")
seurat=turtle.Turtle()
width=5
height=7
dot_distance=25
seurat.penup()

list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey", "red"]
seurat.setpos(-250, 250)# for top most left corner


def spiralPrint(m, n):
    
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
        col=randint(0,10)
        seurat.color(list_color[col])
        # printing the first row fromteh remaining rows
        for i in range(l, n):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[k][i], end=" ")
            
        k+=1
        
        seurat.right(90)
        # printing the last full column from the remaining columns
        col=randint(0,10)
        seurat.color(list_color[col])
        for i in range(k,m):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][n-1],end=" ")
            
        n-=1
        seurat.right(90)
        
        # Printing the last row from remaining rows
        col=randint(0,10)
        seurat.color(list_color[col])
        if k<m:
            for i in range(n-1, l-1, -1):
                seurat.dot()
                seurat.forward(dot_distance)
                #print(a[m-1][i], end=" ")
            
        m-=1
        seurat.right(90)
        
        #printing the first column from the remaining columns
        col=randint(0,10)
        seurat.color(list_color[col])
        for i in range(m-1, k-1, -1):
            seurat.dot()
            seurat.forward(dot_distance)
            #print(a[i][l], end=" ")
            
        l+=1
        seurat.right(90)


    
spiralPrint(5,5)

            
        
    