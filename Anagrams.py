# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 22:39:35 2021

@author: DELL
"""
str1=input('Enter the first string : ')
str2=input(" Enter the second string : ")
if(sorted(str1)==sorted(str2)):
    print("These are Anagrams.")
else:
    print("These are not Anagrams.")