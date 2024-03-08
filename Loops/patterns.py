n=5

for i in range(0, n):
		for j in range(0, i+1):

			print("* ",end="")
	
		print("\r")
		
print("\n")

for i in range(n,0,-1):
		for j in range(0, i):

			print("* ",end="")
	
		print("\r")

for i in range(0, n):
    for j in range(n-1-i):
        print(" ", end="")
    for k in range(0, i+1):
        print("*", end="")
    print("\r")
	

for i in range(1, n + 1):
    m = i
    for j in range(i):
        print(m, end=" ")
        m = m - 1
    print("\r")


for i in range(n,0,-1):
    m = i
    for j in range(i):
        print(m, end=" ")
        m = m - 1
    print("\r")

