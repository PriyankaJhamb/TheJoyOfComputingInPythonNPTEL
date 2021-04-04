# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 10:32:19 2021

@author: DELL
"""

#numpy(numerical python)

import numpy as np

a=np.array([1,2,3])
print('a:',a)
print('type(a):', type(a))
print('a.shape:', a.shape)
print('a[0],a[1],a[2]:',a[0],a[1],a[2])

b=np.array([[1,2,3],[4,5,6]])
print('b:',b)
print('b.shape: ', b.shape)

c=np.zeros((2,3))
print('\n c: \n',c)

d=np.ones((3,2))
print('\n d: \n',d)

e=np.full((4,5),8)
print('\n e: \n', e)

f=np.random.random((3,4))#random number from 0 to 1
print('\n f: \n',f)

#to know the datatype of array 
l=[1,23,4]
#print('l.datatype:',l.dtype)#it will create error as list is not an array
g=np.array(l)
print('\ng.datatype:\n',g.dtype)

#type casting the dtype of array
h=np.array([1,2],dtype=np.int64)
print('\nh.datatype:\n',h.dtype)

i=np.array([[1,2],[3,4]], dtype=np.float64)
j=np.array([[5,6],[7,8]], dtype=np.float64)
print('\n i+j:\n',i+j)
print('\n np.add(i,j):\n',np.add(i,j))

print('\n i-j:\n',i-j)
print('\n np.subtract(i,j):\n',np.subtract(i,j))

print('\n i*j:\n',i*j)
print('\n np.multiply(i,j):\n', np.multiply(i,j))

print('\n i/j:\n',i/j)
print('\n np.divide(i,j):\n',np.divide(i,j))

#print('\n i^j:\n',i^j)#not allowed 
#print('\n np.sqrt(i,j):\n',np.sqrt(i,j))#it will alter the matrix of i

#transpose of a matrix
print('\n i.T: \n',i.T)
print('\n j.T: \n',j.T)

print('\n np.sum(i); \n',np.sum(i))
print('\n np.sum(j); \n',np.sum(j))

print('\n np.sum(i,axis=0); \n',np.sum(i,axis=0))#column wise sum
print('\n np.sum(j,axis=0); \n',np.sum(j,axis=0))

print('\n np.sum(i,axis=1); \n',np.sum(i,axis=1))#row wise sum
print('\n np.sum(j,axis=1); \n',np.sum(j,axis=1))


