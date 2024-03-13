#without using length function

X = "Hello world"
print("The string is :", X)

counter = 0

for i in X:
    print(i, counter)
    counter = counter + 1 

print("The length of a string is :", counter)



#total num of words
Y = list(X.split(" "))
print(Y)

count = 0 
for i in Y:
    print(i)
    count = count + 1 
    
print("Total Number of words are :", count)


