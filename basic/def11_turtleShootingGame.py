import random
import turtle

player = turtle.Turtle()
player.shape("turtle")
player.color("orange")
player.up()

planet1 = turtle.Turtle()
planet2 = turtle.Turtle()

planet1.shape("circle")
planet1.color(random.choice(["yellow", "green", "pink"]))
planet1.up()
planet2.shape("circle")
planet2.color(random.choice(["yellow", "green", "pink"]))
planet2.up()


planet1.goto((random.randint(-300, 300)), (random.randint(-300, 300)))
planet1.left((random.randint(1, 360)))
planet2.goto((random.randint(-300, 300)), (random.randint(-300, 300)))
planet2.left((random.randint(1, 360)))

def turnLeft():
    player.left(30)

def turnRight():
    player.right(30)


screen = player.getscreen()
screen.onkeypress(turnLeft, "Left")
screen.onkeypress(turnRight, "Right")
screen.listen()


def play():
    player.forward(2)
    planet1.forward(2)
    planet2.forward(2)
    screen.ontimer(play, 10) #10초마다 함수 play 실행
screen.ontimer(play, 10)


turtle.mainloop()