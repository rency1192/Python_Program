def srch(dictionary, key):

    if key in dictionary:
        print(f"value for {key} is :", {dictionary[key]})
    else:
        print("no found")

A = {'Hetvi' : 10, 'Shreya' : 20, 'Rency' : 30}
search_value = input("Enter the key to search ")
result = srch(A, search_value)
