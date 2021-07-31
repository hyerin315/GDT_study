store = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

item = input("물건의 이름을 입력하시오: ")
print(store[item])

num = int(input("물건의 갯수를 입력하시오: "))
for key, value in store.items():
    if num == value:
        print(key)

