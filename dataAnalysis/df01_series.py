import pandas as pd

#리스트로 시리즈 생성
sd1 = pd.Series(['Dog', 'Cat', 'Tiger', 'Lion', 'Monkey'], index=['0', '1', '2', '3', '4']) #인데스 생략 가능
print(sd1)

#딕셔너리로 시리즈 생성
dict_data = {'a': 1, 'b': 2, 'c': 3}
sd2 = pd.Series(dict_data)
print(sd2)

#튜플로 시리즈 생성
tup_data = ('이순신', '1991-03-15', '남')
sd3 = pd.Series(tup_data, index=['이름', '생년월일', '성별'])
print(sd3)