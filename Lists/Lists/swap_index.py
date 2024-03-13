list=[1,2,3,4,5]

a = list[0]

b = list[len(list)-1]

list[0] = b

list[len(list)-1] = a

print(list)