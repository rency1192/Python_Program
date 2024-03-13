li=[2,6,3,1,8,5,9,4]
max=li[0]
for i in range(1,len(li)):
    if max<li[i]:
        max=li[i]
    
print("Max:",max)


li=[2,6,3,1,8,5,9,4]
min=li[0]
for i in range(1,len(li)):
    if min>li[i]:
        min=li[i]
    
print("Max:",min)