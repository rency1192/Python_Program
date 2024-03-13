print("enter string")
X = input()
print(X)

lower, upper = 0,0

for i in X:
    if(i>='a' and i<='z'):
        lower = lower + 1
    
    if (i>='A' and i<='Z'):
        upper = upper + 1

print("Total number of lower cases are :", lower)
print("Total number of upper cases are :", upper)