import turtle

color_lsit = ["yellow", "red", "blue", "green"]

t = turtle.Turtle()
t.shape("turtle")

i = 0

for i in range(4):
    t.fillcolor(color_lsit[i])
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.fd(100)

