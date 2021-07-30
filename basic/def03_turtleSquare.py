import time
import turtle

t = turtle.Turtle()
t.shape("turtle")
colors = ["yellow", "skyblue", "green", "orange"]
t.pencolor("purple")

def draw(length, num, type):
    j = 0
    while j < num:
        t.fillcolor(colors[j%4])
        t.begin_fill()
        for i in range(type):
            if type == 1:
                t.circle(length)
                type += 1
            else :
                t.forward(length)
                t.left(360//type)
        type += 1
        t.end_fill()
        t.penup()
        t.forward(length+100)
        t.pendown()
        j += 1

draw(50, 4, 1)
time.sleep(100)
