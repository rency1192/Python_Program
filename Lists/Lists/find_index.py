L = [1,2,3,4,5]

print("enter the element to find the index")
X = int(input())

index = 0
for i in L:
    if i == X:
        print(f"the {X} is on index {index}")
        break
    index+=1


#Find total number of elemets in list
L = [1,2,3,4,5,5,5,6,7,8]
c = 0

for i in L:
    c = c + 1
    
print("total numbers of elements are :", c)
    



            