import pandas as pd
import seaborn as sns
from tabulate import tabulate

tips = sns.load_dataset("tips")
print(tabulate(tips, headers='keys', tablefmt='psql'))

#기본정보 출력
tips.info()

#상위 - 하위 정보 출력
print(tips.head())
print(tips.tail())

#행 삭제
tips1 = tips.drop([2])
print(tips1)

#행으로 세번째 데이터 읽기
print(tips1.iloc[2])

#인덱스로 데이터 읽기
print(tips1.loc[2])