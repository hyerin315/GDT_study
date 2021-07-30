import turtle

t = turtle.Turtle()
t.color("blue")
t.fillcolor("red")

value = [120, 56, 309, 220, 156, 23, 98]

def draw():
    for i in value :
        t.begin_fill()
        t.left(90)
        t.fd(i)
        t.right(90)
        t.write(str(i), font = ('Times New Roman', 16, 'bold'))
        t.fd(40)
        t.right(90)
        t.fd(i)
        t.left(90)
        t.end_fill()

draw()
turtle.mainloop()