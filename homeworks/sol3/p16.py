num = int(input("enter a number:"))

isPrime = True
for n in range(2, num):
    if (num % n) == 0:
        isPrime = False
        break


if isPrime == True:
    print("yes")
else:
    print("no")