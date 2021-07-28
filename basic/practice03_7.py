import time

now = time.time()//60
hour = now//60%24
minute = now%60

#time : GMT시간
print("현재 시간(영국 그리니치 시각):", int(hour), "시", int(minute), "분")


