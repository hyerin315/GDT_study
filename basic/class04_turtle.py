import turtle
from turtle import *

class MyTurtle:
    def __init__(self, shape, radius):
        self.t = turtle.Turtle()
        self.t.shape(shape)
        self.t.up()
        self.t.goto(0, -radius)
        self.t.down()
        self.radius = radius

    def drawTurtle(self):
        self.t.circle(self.radius, 3)


t1 = MyTurtle("circle", 50)
t2 = MyTurtle("turtle", 100)
t3 = MyTurtle("square", 150)

while True:
    t1.drawTurtle()
    t2.drawTurtle()
    t3.drawTurtle()


# t1 = Turtle()
# t1.shape("circle")
# t2 = Turtle()
# t2.shape("turtle")
# t3 = Turtle()
# t3.shape("square")
#
# t1.penup()
# t2.penup()
#
# t1.goto(0, 100)
# t2.goto(0, 50)
#
# t1.pendown()
# t2.pendown()
#
# while True:
#     t1.circle(100)
#     t2.circle(150)
#     t3.circle(200)