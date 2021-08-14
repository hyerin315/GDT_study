import time
import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(3):
    t.fd(100)
    t.left(360/3)


t.penup()
t.fd(200)
t.pendown()

for i in range(4):
    t.fd(100)
    t.left(360/4)

time.sleep(100)