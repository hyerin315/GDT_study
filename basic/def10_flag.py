import turtle

t = turtle.Turtle()

def draw_f(radius, color):
    t.left(270)
    t.width(3)
    t.color("black", color)
    t.begin_fill()
    t.circle(radius/2.0, -180)
    t.circle(radius, 180)
    t.left(180)
    t.circle(-radius / 2.0, -180)
    t.end_fill()

draw_f(200, "red")
t.setheading(180)
draw_f(200, "blue")