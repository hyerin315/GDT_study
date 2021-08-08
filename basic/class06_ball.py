import turtle
from turtle import *

class Ball:
    def __init__(self, color, size, speed):
        self.x = 0
        self.y = 0

        self.color = color
        self.xspeed = speed
        self.yspeed = speed

        self.turtle = Turtle()
        self.turtle.shape("circle")
        self.turtle.color(self.color)
        self.turtle.resizemode("user")
        self.turtle.shapesize(size, size, 10)

    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        self.turtle.goto(self.x, self.y)

ball = Ball("red", 2, 3)
for i in range(100):
    ball.move()

turtle.mainloop()