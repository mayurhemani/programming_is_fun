from turtle import *

speed(100)

def grow(string):
    newstring = ""
    for ch in string:
        if ch == "X":
            newstring = newstring + "XPYFP"
        elif ch == "Y":
            newstring = newstring + "QFXQY"
        elif ch == "P":
            newstring = newstring + "P"
        elif ch == "Q":
            newstring = newstring + "Q"
        elif ch == "F":
            newstring = newstring + "F"
    return newstring



def drawString(string):
    for ch in string:
        if ch == "F":
            fd(5)
        elif ch == "P":
            rt(45)
        elif ch == "Q":
            lt(45)
            
s = "FX"
for _ in range(10):
    s = grow(s)
drawString(s)

exitonclick()