
total = 0
s = 'yes'

while s == 'yes' :
    num = int(input("숫자를 입력하시오 : "))
    total += num
    s = input("계속?(yes/no) : ")

print("합계는 : ", total)

