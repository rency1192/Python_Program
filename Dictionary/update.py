A = {'A' : 10, 'B' : 20} 
B = {'C' : 10, 'D' : 20} 

C = dict(**A, **B)
print(C)


#another way


A = {'A' : 10, 'B' : 20} 
B = {'C' : 10, 'D' : 20} 

C = A.copy()
C.update(B)

print(C)

