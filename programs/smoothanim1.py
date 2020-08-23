from turtle import *

class stick_figure:
    def __init__(self, x, y):
        register_shape("stickperson.gif")
        shape("stickperson.gif")
        pu()
        goto(x, y)
        pd()
        self.s = stamp()
        ht()


    def move_to(self, x, y):
        pu()
        goto(x, y)
        pd()
        clearstamp(self.s)
        self.s = stamp()



sfigure = stick_figure(-100, 0)

for i in range(-100, 100, 10):
    sfigure.move_to(i, 0)


exitonclick()
        

