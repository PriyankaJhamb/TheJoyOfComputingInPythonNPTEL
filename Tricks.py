# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:29:50 2021

@author: DELL
"""
# There is actually a poem on python which can be read by just writing import this 
import this 
'''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


a="Priyanka"
print(a*4)# You can print a string stored in a variable x n times using command 

b=['1','2','3','4','5','6']
print("".join(b))#It will create a single list from all teh eleemnts in list b

c=float("inf")
print(c+4)# We can define 'infinity' in python using float('inf')

dict={'flavour': 'strawberry'}
print(dict)
dict.clear()#It removes all the elements of dictionary dict
print(dict)

e=3
f=34
e,f=f,e# swap the numbers
print(e, f)


#compare the two lists
list1 = ["fg","fg", "rt", "fg", "lllf"]  
list2 = ["fg","fg", "rt", "fg", "lf"]  
  
a = set(list1)  
b = set(list2)  
  
print(a)
print(b)

if a == b:  
    print("The list1 and list2 are equal")  
else:  
    print("The list1 and list2 are not equal")  