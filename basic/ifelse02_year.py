year = int(input("연도 입력 : "))

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print(str(year) + "년은 윤년입니다.")
else:
    print(str(year) + "년은 윤년이 아닙니다.")