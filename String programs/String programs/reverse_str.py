print("enter string")
str1 = str(input())
hetvi = ""
for i in str1:
    hetvi = i + hetvi
    
print(hetvi)


str2="hello123hii"
str2= str2[::-1]   
print(str2)

s1="hii12hello"
s2=""
s3=s2.join(reversed(s1))
print(s3)

