money = int(input("투입한돈 : "))
total = int(input("물건값 : "))
change = money-total
print("거스름돈 :", change)
print("500원 동전 개수 :", int(change/500))
print("100원 동전 개수 :", int((change%500)/100))
