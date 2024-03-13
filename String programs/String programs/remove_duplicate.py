print("Enter String")
str1=str(input())

l=list(str1.split(" "))
l1=[]
for i in l:
    if l.count(i)>=1 and (i not in l1):
        l1.append(i)
print(l1)


#Another way
print(set(l))