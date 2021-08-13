import seaborn as sns

tips = sns.load_dataset("tips")

#데이터 프레임 개수 확인
print(tips.count())
print(len(tips))

print("-"*50)

#인덱스 확인
print(tips.index)

#변수(컬럼) 확인
print(tips.columns)

#데이터 확인(행, 열, 구조확인)
print(tips.values)

print("-"*50)

#열 이름을 알파벳 순서로 정렬
print(tips.sort_index(axis=0))

print("-"*50)

#지급액 열을 기준으로 오름차순 정렬
print(tips.sort_values(by=['total_bill'], axis=0))

#지급액 열을 기준으로 내림차순 정렬
print(tips.sort_values(by=['total_bill'], axis=0, ascending=False))

