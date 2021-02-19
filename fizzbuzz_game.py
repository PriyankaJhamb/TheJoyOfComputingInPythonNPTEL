# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:29:11 2021

@author: DELL
"""
def FizzBuzz(r):
    for i in range(1,r):
        if(i%3==0 and i%5==0):
             print("fizzbuzz")
        if(i%3==0 and i%5!=0): 
            print("fizz")
        if(i%5==0 and i%3!=0):
           print("buzz")
        if(i%3!=0 and i%5!=0):
          print(str(i)+" ")#print(i," same")
          
def fizzbuzz(r):
    for i in range(r):
        if(i%3==0 and i%5==0):
            print("FizzBuzz")
        else:
            if(i%3==0):
                print("Fizz")
            else:
                if(i%5==0):
                    print("Buzz")
                else:
                    print(i)
        
FizzBuzz(511)#Call Function
fizzbuzz(20)
