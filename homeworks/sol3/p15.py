def reverse_digits(num):
    x = 0
    while num > 0:
        rem = num % 10
        num = (num - rem) // 10
        x = x * 10 + rem
    return x
    


a = int(input("enter a number:"))
print(reverse_digits(a))