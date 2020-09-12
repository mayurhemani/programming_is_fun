x = [1, 17, 3, 5, 6, 8, 34, 32, 121, 11, 9, 13]

numElems = len(x)

largest = x[0]

pos = 1
while (pos < numElems):
	if (x[pos] > largest):
		largest = x[pos]
	pos = pos + 1

print(largest)
