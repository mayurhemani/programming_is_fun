x = [1, 17, 3, 5, 6, 8, 34, 32, 121, 11, 9, 13]
print("before", x)

numElems = len(x)

i = 0
while i < numElems:
	j = i + 1
	while j < numElems:
		if x[i] > x[j]:
			t = x[i]
			x[i] = x[j]
			x[j] = t
		j += 1
	i += 1

print("after", x)
