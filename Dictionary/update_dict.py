# Python program to replace dictionary value 
# for the given keys in another dictionary

myDict = {'Scala': 2, 'Javascript': 1, 'Python': 8, 'C++': 1, 'Java': 4}
updateDict = {"Scala"  : 10, "Python" : 17}

print("Dictionary = ", end = " ")
print(myDict)

for sub in myDict:
    if sub in updateDict:
        myDict[sub]  = updateDict[sub]
  
# Printing the dictionary
print("Updated dictionary = ", end = " ")
print(myDict)
