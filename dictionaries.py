# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:00:53 2021

@author: DELL
"""
#factor=[] #list
conv_factor={} #dictionary
print(conv_factor)

conv_factor['Dollar']=45# adding a key and its value in dictionary conv_factor
print(conv_factor)

conv_factor['Euro']=45# adding a key and its value in dictionary conv_factor
print(conv_factor)


conv_factor['Yum']=5# adding a key and its value in dictionary conv_factor
print(conv_factor)

conv_factor['Dollar']=98#updating value of key
print(conv_factor)

del conv_factor['Dollar']
print(conv_factor)

print(conv_factor.items())
print(conv_factor.keys())
print(conv_factor.values())


conv_factor.pop("Euro")
print(conv_factor)

e=30
r=e*conv_factor["Yum"]
print(r)


