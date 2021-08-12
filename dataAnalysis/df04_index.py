import seaborn as sns

tips = sns.load_dataset("tips")

#0번째 행 추출
print(tips.iloc[0])

#음수로 마지막 행 추출
print(tips.iloc[-1])

#행과 열 동시에 선택
print(tips.iloc[3:5, 0:2])

#인덱스 기준으로 행과 열 동시에 선택
print(tips.iloc[[1, 2, 4],[0, 2]]) #리스트 안의 리스트를 탐색

#슬라이스 이용하여 행과 열 가져오기
print(tips.iloc[1:3, :])

print("-"*50)

#인덱스가 0인 데이터 추출
print(tips.loc[0])

#1,3,5 인덱스를 한 번에 가져오기
print(tips.loc[[1, 3, 5]])

#인덱스로 특정 열 추출하기
print(tips.loc[0:3, ['sex', 'day']])
print(tips.loc[0, ['sex', 'day']])

print("-"*50)

#범위 지정하여 인덱스 및 행 갖고오기
print(tips[0:3]) #행번호
print(tips.iloc[0:3]) #행번호
print(tips.loc[0:3]) #인덱스

print("-"*50)

#특정 인덱스와 특정 컬럼의 값 가져오기
print(tips.at[0, 'sex'])

#값 하나 가져오기
print(tips.iloc[1, 1])
print(tips.iat[1, 1])