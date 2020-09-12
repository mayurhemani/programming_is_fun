s = "this is a sentence"
w = []
cs = ""
i = 0
j = len(s)

while i < j:
	if (s[i] == " ") and (i > 0) and (s[i-1] != " "):
		w.append(cs)
		cs = ""
	else:
		cs = cs + s[i]
	i = i + 1

w.append(cs)


print(w)
