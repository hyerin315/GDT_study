import seaborn as sns

tips = sns.load_dataset("tips")

#변수 값 추출
print(tips.tip)
print(tips['size'])

print("-"*50)

#여러 개 변수열 한 번에 추출
print(tips[['total_bill', 'tip', 'day']])

print("-"*50)

#파생변수 만들기
tips['total'] = tips['total_bill'] + tips['tip']
print(tips['total'])

print("-"*50)

#자료형 확인 및 변환
print(tips.dtypes)

#데이터 프레임 열 자료형 확인
print(type(tips.total_bill))

#데이터 프레임 자료형 변환
tips['smoker_str'] = tips['smoker'].astype(str) #카테고리형(범주형 데이터는 카테고리가 효율적)
print(tips['smoker_str'].dtypes) #오브젝트형