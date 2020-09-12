x = [1, 17, 3, 5, 6, 8, 34, 32, 121, 11, 9, 13]

q = int(input("enter the number to find: "))

numElems = len(x)

pos = 0

while (pos < numElems) and (x[pos] != q):
	pos = pos + 1

if pos == numElems:
	print("does not exist")
else:
	print(pos)

