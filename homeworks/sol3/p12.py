n = int(input("enter the number of numbers: "))

s = 0

for _ in range(n):
    x = int(input("enter a number:"))
    s = s + x
    
print(s)