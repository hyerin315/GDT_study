import turtle

t = turtle.Turtle()
t.shape("turtle")
wn = turtle.Screen()

while True:
    s = input("명령을 입력하시오: ")
    if s == "l":
        t.lt(90)
        t.fd(100)
    else:
        t.rt(90)
        t.fd(100)

