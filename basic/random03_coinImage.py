import random
import turtle
import time

screen = turtle.Screen()
image1 = "./img_coin/coin_f.gif"
image2 = "./img_coin/coin_b.gif"

t1 = turtle.Turtle()
t1.speed(1)

for i in range(10):
    com = random.randrange(2)
    if com == 0:
        screen.addshape(image1)
        t1.shape(image1)
        t1.stamp()
    else :
        screen.addshape(image2)
        t1.shape(image2)
        t1.stamp()


t1.write("게임이 끝났습니다.")

time.sleep(10)