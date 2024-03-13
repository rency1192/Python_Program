str = "Python is a programming language"
words = list(str.split(" "))

print("list converted string: ", words)

print("EVEN length words:")
for W in words:
    if len(W) % 2 == 0:
        print(W, len(W))




#Multiple copies of string using multiplication operator 

X = "Hetvi"
Y = 5
Z = X*5
print(Z)

