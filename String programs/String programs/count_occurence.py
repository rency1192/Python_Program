print("enter a string")
hetvi=str(input())

list=list(hetvi.split(" "))
print(list)

set=set(list)
print(set)

for i in set:
    print(i, list.count(i))