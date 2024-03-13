L=[1,5,3,2,6]
n=len(L)

for i in range(n):
    for j in range(n-1-i):
        if L[j]>L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]

print(L)

for i in range(n):
    for j in range(n-1-i):
        if L[j]<L[j+1]:
            L[j],L[j+1]=L[j+1],L[j]

print(L)
