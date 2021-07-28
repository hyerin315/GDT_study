import time
now = time.time()
print(now)
thisYear = int(1970 + now//(365*24*3600))
print("올해는 {}년 입니다.".format(thisYear))

age = int(input("몇 살이신가요? "))
print("2050년에는 {}살 이시군요.".format(age + 2050-thisYear))
