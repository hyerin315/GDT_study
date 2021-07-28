
saved_id = "ilovepython"
id = input("아이디를 입력하세요 : ")

saved_pw = "1234"

if saved_id == id :
    for i in range(5):
        pw = input("패스워드를 입력하세요 : ")
        if saved_pw == pw :
            print("환영합니다.")
            break
        elif i < 5:
            print("패스워드를 다시 입력하세요.")
        else :
            print("패스워드가 5번 잘못입력되었습니다.")
else:
    print("아이디가 일치하지 않습니다.")