import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "이름을 입력하시오: ")

for i in range(4):
    t.fd(100)
    t.rt(90)

t.write("안녕하세요?" + s + "인사드립니다.")

a = turtle.textinput("", "이름을 입력하시오: ")