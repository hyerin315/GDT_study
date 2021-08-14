import time
import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(5) :
    t.forward(50)
    t.right(144)

t.penup()
t.forward(-100)
t.pendown()

i = 0
while i < 5 :
    t.forward(50)
    t.right(144)
    i += 1

time.sleep(100)

