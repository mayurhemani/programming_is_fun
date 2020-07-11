def power(x, n):    
    ans = 1
    for _ in range(n):
        ans = ans * x
        
    return ans


x = float(input("enter a number:"))
n = int(input("enter a number:"))
print(power(x, n))
    
