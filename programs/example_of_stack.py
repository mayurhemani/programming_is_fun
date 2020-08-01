from turtle import *

speed(1000)


stack = []

def push(x, y, angle):
    global stack
    stack.append( (x, y, angle) )
    
    
def pop():
    global stack
    lastItemPos = len(stack) - 1
    lastItem = stack[lastItemPos]
    stack = stack[:lastItemPos]
    return lastItem


def grow(string):
    newstring = ""
    for ch in string:
        if ch == "0":
            newstring = newstring + "1[0]0"
        elif ch == "1":
            newstring = newstring + "11"
        elif ch == "[":
            newstring = newstring + "["
        elif ch == "]":
            newstring = newstring + "]"
    return newstring

colormode(255)

def drawString(string):
    speed(100)
    for ch in string:
        if ch == "0":
            colormode(255)
            pencolor((0, 255 ,0))
            fd(1)
            pencolor((0, 0 ,0))
        elif ch == "1":
            fd(1)
        elif ch == "[":
            xpos = xcor()
            ypos = ycor()
            angle = heading()
            push(xpos, ypos, angle)
            lt(45)
        elif ch == "]":
            xpos, ypos, angle = pop()
            pu()
            goto(xpos, ypos)
            setheading(angle)
            pd()
            rt(45)
            
            
            
s = "0"
for _ in range(10):
    s = grow(s)
    
lt(90)
pu()
bk(200)
pd()
drawString(s)

exitonclick()