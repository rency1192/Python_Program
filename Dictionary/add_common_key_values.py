
dict1 = {'a': 12, 'for': 25, 'c': 9}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300}


# adding the values with common key
for key in dict2:
	if key in dict1:
		dict2[key] = dict2[key] + dict1[key]
	else:
		pass
		
print(dict2)
