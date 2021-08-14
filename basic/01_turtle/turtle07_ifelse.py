import turtle

t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(100, 100)
t.write("거북이가 여기로 오면 음수입니다.")

t.goto(100, 0)
t.write("거북이가 여기로 오면 0입니다.")

t.goto(100, -100)
t.write("거북이가 여기로 오면 음수입니다.")
t.goto(0, 0)

t.down()

n = int(turtle.textinput("", "정수를 입력하세요"))

if n > 0 :
    t.goto(100, 100)
if n == 0 :
    t.goto(100, 0)
if n < 0 :
    t.goto(100, -100)


