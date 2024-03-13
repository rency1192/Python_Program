# L = ["A", "B", "C", "D", "E"]
# print(L)
# L.insert(2, "H")
# print(L)

# print("enter index")
# X = int(input())


#Without using in built function 

L = [1,2,3,4,5]
l1 = []
index = 3
value = 5
print(L)

for i in range(index):
        l1.append(L[i])
l1.append(value)
for i in range(index+1, len(L)+1):
    l1.append(i)
print(l1)