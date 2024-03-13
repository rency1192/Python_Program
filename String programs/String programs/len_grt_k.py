print("Enter string")
str1 = str(input())
print("enter length to check")
Z = int(input())
Y = list(str1.split(" "))
#print(Y)

for i in Y:
    if len(i)>Z:
        print(i)

