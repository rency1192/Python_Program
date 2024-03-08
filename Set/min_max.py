A = {1,2,3,4,5,44,4,4,4,4}

mylist = list(A)
print(type(mylist))
max, min = 0,0

for i in A:
    if i > max:
        max = i
    if i < min:
        min = i
        
print(f"Minimum is {min}, maximum is {max}")
