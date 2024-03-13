def find_substrings(s):
    substrings = []
    length = len(s)  

    for i in range(length):
        for j in range(i + 1, length + 1):
            substrings.append(s[i:j])  

    return substrings  

input_string = "Hetvi"  
result = find_substrings(input_string)  

print("All possible substrings of '{}' are: {}".format(input_string, result))


X = "Hetvi"
Y = []

