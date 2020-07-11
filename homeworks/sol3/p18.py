num1 = int(input("enter a number:"))
num2 = int(input("enter a number:"))

smaller = min(num1, num2)

hcf = 0
for i in range(smaller, 0, -1):
    if (num1 % i == 0) and (num2 % i == 0):
        hcf = i
        break

print("LCM= " + str( (num1 * num2) / hcf ))
    
