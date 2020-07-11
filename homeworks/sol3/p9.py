def max5(a, b, c, d, e):
    m = a
    for o in [b, c, d, e]:
        if o > m:
            m = o
    return m


x1 = int(input("Enter 1st number: "))
x2 = int(input("Enter 2nd number: "))
x3 = int(input("Enter 3rd number: "))
x4 = int(input("Enter 4th number: "))
x5 = int(input("Enter 5th number: "))

print(max5(x1, x2, x3, x4, x5))
