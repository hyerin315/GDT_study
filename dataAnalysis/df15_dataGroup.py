import pandas as pd

file_path = './dataset/exam_sample.csv'
df = pd.read_csv(file_path)
print(df)

#반 별로 그룹화 - 반 별 그룹 오브젝트만 생성
df1 = df.groupby(['class']) #[] 대괄호 없어도 됨
print(df1)

#반 중 A반 그룹만 확인
print(df1.get_group('A'))

#반별 그룹 평균 확인
print(df.groupby('class').mean()) #[] 대괄호 없어도 됨

#반별, 성별 그룹 평균 확인
print(df.groupby(['class', 'sex']).mean())

#반별 수학 편귱
print(df['math'].groupby(df['class']).mean())
print(df.groupby(df['class'])['math'].mean()) #결과가 같음

#반별 수학 개수
print(df['math'].groupby(df['class']).count())
print(df.groupby(df['class'])['math'].count()) #결과가 같음

#성별 수학 평균
df_mean = df['math'].groupby(df['sex']).mean()
sexgroup = df.groupby(['sex'])
print(df_mean)
print(sexgroup)
print(sexgroup.groups)

#남학생 수학 평균
male = sexgroup.get_group('m')
subset = male[['sex', 'math']]
print(male)
print(subset.mean())