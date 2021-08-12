import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")

#시리즈를 새로우 ㄴ행으로 연결
s1 = pd.Series([0, 1], index=['A', 'B'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
print(s1)
print(s2)

#연결
print(pd.concat([s1, s2]))

print("-"*50)

#옆으로 데이터 연결시 axis = 1 설정
df1 = pd.DataFrame([['Dog', '3'], ['Bird', '10'], ['Tiger', '6'],
                    ['Moose', '3']], index= ['0', '1', '2', '3'],
                   columns= ['동물', '나이'])
print(df1)

df2 = pd.DataFrame([['집', '0'], ['초원', '0'], ['수풀', '0'],
                    ['초원', '1']], index= ['0', '1', '2', '3'],
                   columns= ['사는곳', '뿔의 개수'])

print(df2)

print(pd.concat([df1, df2], axis=1)) #우측으로 연결
