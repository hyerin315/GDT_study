import time
import turtle

t = turtle.Turtle()
t.shape("turtle")

a = int(turtle.textinput("", "몇 각형을 그리겠습니까?"))
len = int(turtle.textinput("", "변의 길이를 입력하시오."))

for i in range(a):
    t.fd(len)
    t.right(360/a)

time.sleep(100)