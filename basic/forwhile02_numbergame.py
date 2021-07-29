import random

print("1부터 100사이의 숫자를 맞추시오. \n게임 시작!")
answer = random.randint(1, 100)
count = 0
num = 0

while (answer != num) and (count < 10) :
    num = int(input("숫자를 입력하시오 : "))
    if num > answer :
        print("높음!")
    elif num < answer :
        print("낮음!")
    count += 1

if answer == num:
    print("축하합니다. 맞췄습니다! 시도횟수 :", count)
else:
    print("정답은 : ", answer)


