'''
import string
string1=input()
string2=input()
list=[]
count=0
for i in string.ascii_uppercase:
    list.append(i)
    

req=[]
for i in string1:
    p2=list.index(i)
    p1=int((p2+5)%26)
    req.append(list[p1])
     
if sorted(string2)==sorted(req):
    print("Yes",end="")
else:
    print("No",end="")
'''

from itertools import permutations
s1 = input()
s2 = input()
# s = s[::-1]
t = ''
for c in s1:
    t += chr((ord(c)+5)%26)

L = [''.join(p) for p in permutations(t)]
s = set(L)
count = 0
for elem in s:
    if elem == s2:
        count+=1
if count==1:
    print("Yes")
else:
    print("No")