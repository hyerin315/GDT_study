import random

print("동전 던지기 게임을 시작합니다!")
for i in range(10):
    com = random.randrange(2)
    if com == 0:
        print("앞면입니다")
    else :
        print("뒷면입니다")
    print("게임이 끝났습니다.")