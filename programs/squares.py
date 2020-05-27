def showSquare(n):
    i = 0
    while (i < n):
        newString = " " * (2*n+1) + "*" * (2*n)
        print(newString)
        i = i + 1
        
j = 1
while j < 10:
    showSquare(j)
    print(" ")
    j = j + 2