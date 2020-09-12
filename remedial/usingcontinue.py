i = 0
while i < 50:
	if (i%5) == 0:
		i += 1
		continue

	print("*"*i)
	i += 1
print("program end")
