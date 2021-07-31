dic = {"one" : "하나", "two" : "둘"}
dic["three"] = "셋"
dic["four"] = "넷"

word = input("단어를 입력하시오 : ")

if word in dic.keys():
    print(dic[word])
else :
    print("사전에 등록되지 않았습니다.")
