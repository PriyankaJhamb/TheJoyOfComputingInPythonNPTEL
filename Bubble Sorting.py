# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:00:41 2021

@author: DELL
"""

#bubble sorting
try: 
    list_numbers=[]
    
    while True:
        list_numbers.append(int(input()))
# if the input is not-integer, just print the list 
except:
    print("List : " ,list_numbers)
        
length=len(list_numbers)
for i in range(length):
    for j in range(length-i-1):
        if list_numbers[j]>list_numbers[j+1]:
            temp=list_numbers[j]
            list_numbers[j]=list_numbers[j+1]
            list_numbers[j+1]=temp
        
         
print("Sorted List: " ,list_numbers)