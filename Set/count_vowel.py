def CheckString(s):
    s = s.lower()
    vowels = {"a", "e", "i", "o", "u"}
    for char in s:
        if char in vowels:
            vowels.remove(char)
    if len(vowels) == 0:
        print("Accepted")
    else:
        print("Not accepted")


s1= "AeBIdeffoBUw"
print(s1)
CheckString(s1)
