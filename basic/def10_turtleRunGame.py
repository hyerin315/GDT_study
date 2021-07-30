import random
import turtle

t1 = turtle.Turtle()
t2 = turtle.Turtle()


def position(a, b, ):
    a.shape("turtle")
    a.shapesize(2)
    a.up()
    a.goto(-200, b)
    a.down()


t1.color("blue")
position(t1, 200)

t2.color("orange")
position(t2, 0)


for i in range(30):
    t1.fd(random.randrange(1, 10))
    t2.fd(random.randint(1, 10))


turtle.mainloop()