L = [1,2,3,4,5,6,7,8,9,10,15]
L1 = []

print("enter the M")
M = int(input())

print("enter the N")
N = int(input())

for i in L:
    if (i%M==0 and i%N==0):
        L1.append(i)
        
print("number is divisible by both {M} and {N} is : ", L1)
        

            