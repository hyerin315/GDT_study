import random

options = ["왼쪽", "중앙", "오른쪽"]
com_choice = random.choice(options)
user_choice = input("어디를 수비하시겠습니까? \n왼쪽, 중앙, 오른쪽\n")

if com_choice == user_choice:
    print("컴퓨터 수비 성공!")
else:
    print("컴퓨터 수비 :", com_choice)
    print("패널티 킥 성공!")
