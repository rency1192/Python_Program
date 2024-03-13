#using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
print("count ", i)

#for loop
X = ["A","B", "C", "D"]

for i in X:
  print(i)

#Using comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "b" in x:
    newlist.append(x)

print(newlist)

############
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


