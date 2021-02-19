# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:42:12 2021

@author: Priyanka Jhamb
"""
def magicSquare(n):       
    #magic_square=[[0 for i in range(3)]for j in range(3)]
    
    magic_square=[]
    for i in range(n):
          l=[]
          for j in range(n):
              l.append(0)
          magic_square.append(l)
          
    for i in range(n):
          for j in range(n):
              print(magic_square[i][j], end=" ")
          print()
    print()
    print("magic square ")
    
    i=n//2
    j=n-1
    count=1
    num=n*n
    
    while (count<=num):
      if (i==-1 and j==n):#condition 4
          i=0
          j=n-2
      else:
          if (j==n):#column value is exceeding
              j=0
              
          if (i<0):#row si becoming -1
              i=n-1
          
      if(magic_square[i][j]!=0):
         i=i+1
         j=j-2
         continue
      else:
         magic_square[i][j] = count
         count+=1
         i=i-1
         j=j+1#condition 1
      
     
    for i in range(n):
          for j in range(n):
              print(magic_square[i][j], end=" ")
          print()
    print()
    print("The sum of each row/column/diagonal is:" ,(n*((n*n)+1)/2)) # n*n=n**2=n^2
    print()
    
magicSquare(1)
magicSquare(3)
magicSquare(5)
magicSquare(7)
magicSquare(9)
magicSquare(11)
