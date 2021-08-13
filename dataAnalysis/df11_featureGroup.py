import pandas as pd
import seaborn as sns

#데이텆 준비
tips = sns.load_dataset("tips")
print(tips)

#데이터 유형 확인
print(tips.dtypes)

print("-"*50)

#성별 범주형 변수 빈도분석
print(tips['sex'].value_counts())

#요일별 범주형 변수 빈도분석
print(tips['day'].value_counts())

print("-"*50)

#성별, 요일별 교차분석
print(pd.crosstab(tips['sex'], tips['day']))

print("-"*50)

#여백 또는 누적값(누적도수, cumulatives), 합계(?)
print(pd.crosstab(tips['sex'], tips['day'], margins=True))

print("-"*50)

#전체 빈도 비율 확인
print(pd.crosstab(tips['sex'], tips['day']).apply(lambda r : r/len(tips), axis=1)) #len(tips) : 행 개수

print("-"*50)

#연속형 변수 기술통계량 확인
print(tips.describe())