# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 10:36:01 2021

@author: DELL
"""

import random
#Monte Hall: 3 doors and a twist02.py
#2 goat doors 
# 1 BMW door

doors=[]
doors=[0]*3
goatdoor=[0]*2
swap=0
not_swap=0
x=random.randint(0,2)
doors[x]="BMW"
for i in range(0,3):
    if i==x:
        continue
    else:
        doors[i]="Goat"
        goatdoor.append(i)
        
i=0
while (i<5):        
    choice=int(input("Enter your choice: "))
    door_open=random.choice(goatdoor)
    want_swap=input("Do you want to swap? y/n : ")
    while door_open==choice:
        door_open=random.choice(goatdoor)
        
    if want_swap=="y":
        if doors[choice]=="Goat":
            print("Player wins")
            swap=swap+1
        else:
            print("Player lost")
            
            
    else:
        if doors[choice]=="Goat":
            print("Player lost")
            
        else:
            print("Player wins")
            not_swap=not_swap+1
    i=i+1
        
print(swap)
print(not_swap)
       