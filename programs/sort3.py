a = 120
b = 30
c = 521

s = m = l = 0

if a > b:
    l = a
    s = b
else:
    s = a
    l = b
    
if c > l:
    m = l
    l = c
elif c < s:
    m = s
    s = c
else:
    m = c

    
print(s, m, l)

