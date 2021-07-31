import turtle

t = turtle.Turtle()

position = [[0, 0, "blue"], [-120, 0, "purple"], [60, 60, "red"],
            [-60, 60, "yellow"], [-180, 60, "green"]]

def draw_flag():
    #방법 1
    # for i in range(len(position)):
    #     x, y, z = position[i]

    #방법 2
    # for i in position:
    #     x, y, z = i #i 역시 리스트이기 때문에 i 자체를 가져와도 됨

    for x, y, z in position: #방법 2의 축약본
        t.up()
        t.goto(x, y)
        t.down()
        t.color(z, z)
        t.begin_fill()
        t.circle(30)
        t.end_fill()

draw_flag()
turtle.mainloop()