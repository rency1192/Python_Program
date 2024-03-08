def is_heterogram(string):
	sorted_string = sorted(string.lower())
	for i in range(1, len(sorted_string)):
		
		if sorted_string[i] == sorted_string[i-1] and sorted_string[i].isalpha():
			return 'No'
	return 'Yes'
string='the big dwarf only jumps'
print(is_heterogram(string))
