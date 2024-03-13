list=[5,7,3,4]
count=0
for i in list:
    c=0
    for j in range(1,i+1):
        if i%j == 0:
            c=c+1
    if c==2:
        count+=1


#print(count)
if count == len(list):
    print("Yes")
else:
    print('No')