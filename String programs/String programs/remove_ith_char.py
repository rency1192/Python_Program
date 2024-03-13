print("Enter String")
str=input()
print("Remove index to be removed")
n=int(input())
a = ""

for i in range(len(str)):
    if i!=n:
       a=a+str[i]

print(a)