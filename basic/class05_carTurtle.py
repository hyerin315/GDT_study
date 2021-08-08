from turtle import *
import turtle
import random

class Car:
    def __init__(self, speed, color, model):
        self.speed = speed
        self.color = color
        self.model = model
        self.turtle = Turtle()
        self.turtle.shape("./img_car/car.gif")

    def drive(self):
        self.turtle.forward(self.speed)

    def left_turn(self):
        self.turtle.left(90)

    def right_turn(self):
        self.turtle.right(90)

register_shape("./img_car/car.gif")
myCar = Car(200, "red", "E-class")
for i in range(100):
    myCar.random = random.choice([myCar.left_turn(), myCar.right_turn()])
    myCar.drive()

turtle.mainloop()