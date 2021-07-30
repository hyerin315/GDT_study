import turtle

t = turtle.Turtle()
t.fillcolor("green")


def draw_s(x, y):
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    #t.fillcolor(random.choice(["green","yellow","orange"])
    #t.circle(random.randint(1,50))
    for i in range(4):
        t.forward(100)
        t.left(90)
    t.end_fill()


s = turtle.Screen()
s.onscreenclick(draw_s)

turtle.mainloop()
