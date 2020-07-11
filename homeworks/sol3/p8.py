def swap(a, b):
    return b, a


x = int(input("enter 1st number: "))
y = int(input("enter 2nd number: "))

x, y = swap(x, y)

print(x, y)
