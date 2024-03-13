first_list = [4, 9, 2, 0, 3]
second_list = [4, 0, 1]

difference_result = []
for item in first_list:
    if item not in second_list:
        difference_result.append(item)

print(difference_result)