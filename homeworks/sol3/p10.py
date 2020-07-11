def min3(a, b, c):
    m = a
    for o in [b, c]:
        if o < m:
            m = o
    return m


x1 = int(input("Enter 1st number: "))
x2 = int(input("Enter 2nd number: "))
x3 = int(input("Enter 3rd number: "))


print(min3(x1, x2, x3))
