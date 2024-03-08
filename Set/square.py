list=[1,2,3,4,5]
set={}
for i in list:
    set.update(i*i)

print(set)
