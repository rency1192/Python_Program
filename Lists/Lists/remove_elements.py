def remove_elements_in_range(list, start, end):
    result = []

    for i in range(len(list)):   #9 
        if not (start <= i <= end):
            result.append(list[i])
    list.clear()
    list.extend(result)
    
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
remove_elements_in_range(my_list, 0,1)
print(my_list)