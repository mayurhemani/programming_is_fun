from turtle import *
from random import randint


class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        colormode(255)

    def goto(self):
        pu()
        goto(self.x, self.y)
        pd()
        
    def draw(self):
        color((0, 0, 0))
        goto(self.x, self.y)
        dot(10)

    def clear(self):
        color((255, 255, 255))
        goto(self.x, self.y)
        dot(12)
        dot(12)


    def move_left(self):
        self.clear()
        self.x += 10
        self.draw()
        
    def move_right(self):
        self.clear()
        self.x -= 10
        self.draw()


    def move_up(self):
        self.clear()
        self.y += 10
        self.draw()


    def move_down(self):
        self.clear()
        self.y -= 10
        self.draw()



speed(0)

balls = []
for _ in range(20):
    balls.append(Ball(randint(0, 300), randint(0, 300)))


for _ in range(100):
    for ball in balls:
        r = randint(0, 100)
        speed(0)
        if r < 25:
            ball.move_up()
        elif r < 50:
            ball.move_down()
        elif r < 75:
            ball.move_right()
        else:
            ball.move_left()












