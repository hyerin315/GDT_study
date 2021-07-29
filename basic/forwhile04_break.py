import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("red")
t.stamp()

for i in range(12):
    t.penup()
    t.forward(50)
    t.pendown()

    t.forward(25)

    t.penup()
    t.forward(15)

    t.stamp()

    t.home()
    t.pendown()

    t.right((30*(i+1))) #360/12 = 30


