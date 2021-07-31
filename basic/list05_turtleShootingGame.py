import random
import turtle

player = turtle.Turtle()
player.shape("turtle")
player.color("orange")
player.up()

asteroids = []
for i in range(10):
    planet = turtle.Turtle()
    planet.shape("circle")
    planet.color(random.choice(["yellow", "green", "pink"]))
    planet.up()
    planet.goto((random.randint(-300, 300)), (random.randint(-300, 300)))
    planet.left((random.randint(1, 360)))
    asteroids.append(planet)

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
    for planet in asteroids:
        planet.forward(2)
    screen.ontimer(play, 10) #10초마다 함수 play 실행

screen.ontimer(play, 10)
turtle.mainloop()