A = {"Hetvii", "Rency", "A"}
C = 0 
B = set("aeiouAEIOU")

for i in A:
    for j in i:
        if j in B:
            C+=1
        
print("total number of vowels in set", C)
