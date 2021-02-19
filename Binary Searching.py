# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 21:27:23 2021

@author: DELL
"""

list_numbers=[]
try: 
    list_numbers=[]
    
    while True:
        list_numbers.append(int(input()))
# if the input is not-integer, just print the list 
except:
    print("List : " ,list_numbers)
    
searched_number=int(input())
first_pos=0
last_pos=len(list_numbers)-1
flag=0
count=1
list_numbers.sort()
while(first_pos<=last_pos and flag==0):
    count+=1
    mid=(first_pos+last_pos)//2
    if searched_number==list_numbers[mid]:
        print('The element is present at pos:  '+str(mid))
        print("The number of iterations are: "+str(count))
        flag=1
    else:
        if(searched_number<list_numbers[mid]):
            last_pos=mid-1
        else:
            first_pos=mid+1
if flag==0:          
    print("The number is not present.")
        