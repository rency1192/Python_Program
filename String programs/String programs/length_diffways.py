print("Enter String")
X = str(input())
print("Length =", len(X))


#Another way using counter
print("Enter String")
hetvi = str(input())
count = 0

for i in hetvi:
    count = count + 1

print("Length of string =", count)



#using 1 for i
def findLen(string):
	return sum( 1 for i in string);

string = 'hetvi'
print(findLen(string))
