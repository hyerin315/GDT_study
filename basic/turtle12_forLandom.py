import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(100):
    t.fd(random.randrange(1, 100))
    t.right(random.randrange(-180, 180))