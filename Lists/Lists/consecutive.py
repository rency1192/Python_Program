list=[1,2,3,4,5,5,5,6,7,8]
flag=False
#n=0
for i in range(0,len(list)-1):
    if list[i] == list[i+1] == list[i+2]:
     #   n=i
        flag=True
#print("Consecutive number is :", list[n])       
if flag== True:
    print("Yes")
else:
    print("No")
