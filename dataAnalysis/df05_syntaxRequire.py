import seaborn as sns

tips = sns.load_dataset("tips")

#전체 데이터 중 조건 값 이상 (>)
print(tips[tips.tip > 5])

print("-"*50)

#and 조건
print(tips[(tips['sex'] == 'Male') & (tips['smoker'] == 'No')])

print("-"*50)

#특정조건 검색 (True / False == isin)
print(tips['day'].isin(['Sun'])) #조건을 만족하는 값 출력

print(tips[tips['tip'].isin([1])]) #조건을 만족하는 값을 포함한 tips 테이블 출력
