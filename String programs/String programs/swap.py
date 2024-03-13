print("enter string")
str1 = str(input())

def swap_string(str1):
    if len(str1) <= 1:
        return str1

    mid = str1[1:len(str1) - 1]
    return str1[len(str1) - 1] + mid + str1[0]


print (swap_string(str1))


