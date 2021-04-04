import numpy as np
node=int(input())
count = 0
a=[int(x) for x in input().split()]
matrix = np.array(a).reshape(node,node)
print(matrix)
for row in matrix:
 temp=np.array(row).tolist()
 print(temp)
 if temp.count(1) == node-1:
  count = count+1
  print('hi')
 
if count == node:
 print('yes')
else:
 print('no')