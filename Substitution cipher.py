import string
file=open('best.txt', 'w')
dict={}

for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
        
for i in range(10):
    dict[str(i)]=int(i-1)
    
    
print(dict)

with open("indian.txt") as f:
    while(True):
       c=f.read(1)
       if not c:
           print("End of file")
           break
       if c in dict:
           data=dict[c]
       if c not in dict:
           data=c
      
       file.write(str(data))
       print(data, end="")

file.close()