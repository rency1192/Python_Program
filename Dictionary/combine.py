A = ["A", "B", "C", "D"]
B = [10, 20, 30, 40]

C = dict(zip(A,B))
print(C)




#another way
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

B = dict()

for i in range(len(keys)):
    B.update({keys[i]: values[i]})
print(B)
