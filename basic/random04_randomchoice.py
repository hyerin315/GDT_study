import random

time = random.randint(1, 24)
sunny = random.choice([True, False])

print("좋은 아침입니다. 지금 시각은",time, "시 입니다.")

if (((6 <= time) and (time <= 9)) or ((14 <= time) and (time <= 16))) and (sunny == True) :
    print("날씨가 화창합니다. \n종달새가 노래를 부릅니다. '랄랄라~'")
else :
    print("날씨가 화창하지 않습니다. \n종달새가 노래를 하지 않습니다.")
