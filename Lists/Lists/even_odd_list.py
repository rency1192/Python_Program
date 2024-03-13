L = [1,2,3,4,5,6,7,8,9,10]

even = 0 
odd = 0

even_l = []
odd_l = []

for i in L:
    if i%2==0:  
        even_l.append(i)
        even+=1
    else:
        odd_l.append(i)
        odd+=1
    
print("even element list", even_l)
print("odd element list", odd_l)
print("total number of element in even list", even)
print("total number of element in odd list", odd)