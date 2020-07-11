def ulta(sp):
    s = ""
    for i in range(sp, 0, -1):
        s = s + str(i)
    return s

def seedha(sp):
    s = ""
    for i in range(1, sp+1):
        s = s + str(i)
    return s



for i in range(10):
    t =  ulta(i) + "0"  + seedha(i)
    print(" " * (9 - i) + t)