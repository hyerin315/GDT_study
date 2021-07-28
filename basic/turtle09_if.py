import time
import turtle

t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하세요 : ")

if s == "사각형" :
    x = int(turtle.textinput("", "가로변의 길이를 입력하세요 :"))
    y = int(turtle.textinput("", "세로변의 길이를 입력하세요 :"))
    for i in range(2):
        t.forward(x)
        t.right(90)
        t.forward(y)
        t.right(90)
elif s == "삼각형" :
    for i in range(3):
        x = int(turtle.textinput("", "변의 길이를 입력하세요 :"))
        t.forward(x)
        t.left(60)
elif s == "원" :
    x = int(turtle.textinput("", "반지름의 길이를 입력하세요 :"))
    t.circle(x)

time.sleep(100)