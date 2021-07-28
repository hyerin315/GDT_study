import random

print("주사위 던지기 게임을 시작합니다!")
for i in range(int(input("몇 번 던지겠습니까? "))):
    com = random.randrange(6)
    if com == 0:
        print("1 입니다")
    elif com == 1:
        print("2 입니다")
    elif com == 2:
        print("3 입니다")
    elif com == 3:
        print("4 입니다")
    elif com == 4:
        print("5 입니다")
    elif com == 5:
        print("6 입니다")
    else:
        print("오류입니다")
print("게임이 끝났습니다.")
