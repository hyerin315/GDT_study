import pandas as pd

#딕셔너리로 데이터프레임 생성
dict_data = {'동물':['Dog', 'Cat', 'Tiger', 'Lion', 'Monkey'], '나이':[7, 9, 2, 3, 1]}
df1 = pd.DataFrame(dict_data)

#타입확인
print(type(df1))

#데이터확인
print(df1)


#리스트로 데잍터프레임 생성
dict_data2 = [['Dog', '7'], ['Cat', '9'], ['Tiger', '2'], ['Lion', '3'], ['Monkey', '1']]
df2 = pd.DataFrame(dict_data2, index=[0, 1, 2, 3, 4], columns=['동물', '나이']) #index 생략가능

#타입확인
print(type(df2))

#데이터확인
print(df2)


