dic = {}

#딕셔너리에 값 넣기
dic["a"] = "apple"
dic["b"] = "banana"
dic["c"] = "coconut"
print(dic)

#딕셔너리 생성
dic = {"a": "apple", "b": "banana", "c": "coconut"}
dic["d"] = "donut"
print(dic)

#Key로 탐색
print(dic["a"])

#모든 Key 탐색
print(dic.keys())

#모든 Value 탐색
print(dic.values())

#값 정렬
dic = {"b": "banana", "a": "apple", "c": "coconut"}

#sorted로 전체정렬은 안됨
print(sorted(dic.values()))
print(sorted(dic.keys()))
print(sorted(dic))

print("모두 정렬")
for key in sorted(dic.keys()):
    print(key, dic[key])

#정렬해서 원래 파일에 넣기 (빈 리스트 생성 후, 정렬된 key + 그 key의 value 넣기
dic2 = {}
for key in sorted(dic.keys()):
    value = dic[key]
    dic2[key] = value

dic = dic2
print(dic)

#항목 삭제
del dic["a"]
print(dic)

#모든 항목 삭제
dic.clear()
print(dic)

