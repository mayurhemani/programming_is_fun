def my_round_func(num):
    inum = int(num)
    fnum = num - inum
    if fnum < 0.5:
        return inum
    return (inum+1)



num = float(input("enter a number:"))
print(my_round_func(num))