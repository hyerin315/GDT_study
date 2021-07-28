import time
import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(4):
    t.forward(100)
    t.right(90)

t.penup()
t.forward(200)
t.pendown()

i = 0
while i < 4:
    t.forward(100)
    t.right(90)
    i += 1

time.sleep(100)