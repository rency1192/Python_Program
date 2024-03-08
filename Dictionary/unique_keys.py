
def UniqueKeys(arr):


	res = list(set(val for dic in arr for val in dic.keys()))

	print(str(res))


arr = [{'my': 1, 'name': 2}, 
	{'is': 1, 'my': 3},
	{'ria': 2}]

UniqueKeys(arr)
