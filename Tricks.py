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
print(c)# We can define 'infinity' in python using float('inf')

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
    
# Define Positive infinity number
ptive_inf = float('inf')

if 99999999999999999 > ptive_inf:
    print('Number is greater than Positive infinity')
else:
    print('Positive infinity is greater')

# Define Negative infinity number
ntive_inf = float('-inf')

if -99999999999999999 > ptive_inf:
    print('Numer is smaller than Negative infinity')
else:
    print('Negative infinity is smaller')
    
#using of *before list_name to showing elements of list 
n=int(input())
matrix=[]
count=0
for row in range(0,n):
    temp=[]
    for col in range(0,n):
        count+=1
        temp.append(count)
    matrix.append(temp)
for r in matrix[:-1]:
    print(r)
    print(*r)
print(matrix[-1], end=" ")   
print(*matrix[-1], end=" ")

#time.time() returns the current time in milli seconds since midnight, jan 1, 1970
import time
print(time.time())


#ord() funciton converts a character into its ASCII notation
print(ord('A'))


#-----#    
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
text1="Welcome to programming. Programming is fun."
text2=" More fun is to program with Python. "
text3="Python is simple yet very vast with multiple functionalities."
text4="So, come enjoy programming with Python."
mytext=text1+text2+text3+text4
print(mytext)
tokens=[t for t in mytext.split()]

sr=stopwords.words('english')

clean_tokens=tokens[:]


freq=nltk.FreqDist(tokens)

freq.plot(20, cumulative=False)

#-----------------------#
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
text1="Welcome to programming . Programming is fun ."
text2=" More fun is to program with Python ."
text3=" Python is simple yet very vast with multiple functionalities ."
text4=" So, come enjoy programming with Python"
mytext=text1+text2+text3+text4
print(mytext)
tokens=[t for t in mytext.split()]

sr=stopwords.words('english')

clean_tokens=tokens[:]


freq=nltk.FreqDist(tokens)

freq.plot(20, cumulative=False)
####------------------####
import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
text1="Welcome to programming. Programming is fun."
text2=" More fun is to program with Python. "
text3="Python is simple yet very vast with multiple functionalities."
text4="So, come enjoy programming with Python."
mytext=text1+text2+text3+text4

tokens=[t for t in mytext.split()]


clean_tokens=tokens[:]

for token in tokens:

    if token in stopwords.words('english'):

        clean_tokens.remove(token)

freq=nltk.FreqDist(clean_tokens)

freq.plot(20, cumulative=False)
        


            
    
                