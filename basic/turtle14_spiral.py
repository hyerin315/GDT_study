import turtle

color = ["red", "purple", "blue", "green", "yellow", "orange"]

t = turtle.Turtle()
turtle.bgcolor("black")
t.width(3)

i = 10

for i in range(500):
    t.forward(i*5)
    t.pencolor(color[i%6])
    t.right(89)

# while i < 500:
#     t.forward(i)
#     t.pencolor(color[i%6])
#     t.right(89)
#     i += 5