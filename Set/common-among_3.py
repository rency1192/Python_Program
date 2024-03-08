def find_common(list1, list2, list3):
	common = set()
	for elem in list1:
		if elem in list2 and elem in list3:
			common.add(elem)
	return common

list1 = [1, 5, 10, 20, 40, 80]
list2 = [6, 7, 20, 80, 100]
list3 = [3, 4, 15, 20, 30, 70, 80, 120]

common = find_common(list1, list2, list3)
print(common)
