n=int(input())
i=1
q=1
for i in range(1, n+1):
    for j in range(1, i+1):
        print(q*q, end=" ")
        q=q+1
    print()