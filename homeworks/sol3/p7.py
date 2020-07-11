def sqr(x):
    return x * x

def cube(x):
    return x * x * x

def power12(x):
    return cube( sqr( sqr ( x ) ) )



num = int(input("enter a num: "))

print( power12(num) )