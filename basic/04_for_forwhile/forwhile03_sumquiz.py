import random

while True :
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    answer = int(input(str(x)+"+"+str(y)+"= "))
    if (x + y) == answer :
        print("잘했어요!")
    else :
        print("다음 번에 잘할 수 있죠?")
