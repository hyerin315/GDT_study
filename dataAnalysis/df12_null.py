import pandas as pd

file_path = "./dataset/bicycle.csv"
df = pd.read_csv(file_path, encoding="cp949")

#결측 데이터 확인
print(df.isnull())

#결측 데이터 확인(반대 값)
print(df.notnull())

print("-"*50)

#열 단위 결측 데이터 개수
print(df.isnull().sum())

#행 단위 결측 데이터 개수
print(df.isnull().sum(1))

print("-"*50)

#열 단위 실제값 개수
print(df.notnull().sum(0))

#행 단위 실제값 개수
print(df.notnull().sum(1))

#결측 데이터가 있는 전체 행 제거
df_drop_allrow = df.dropna(axis=0) #아래로
print(df_drop_allrow)

#결측 데이터가 있는 전체 열 제거
df_drop_allcolumn = df.dropna(axis=1) #옆으로
print(df_drop_allcolumn)

#특정 행 또는 열 결측치 제거, 대여소 번호 컬럼 제거(비교 확인)
print(df['대여소번호'].dropna())

#결측값이 들어있는 행 전체 삭제
df_drop_all = df[['대여소번호', '대여거치대', '이용시간']].dropna()
print(df_drop_all)

#결측값이 들어있는 열 전체 삭제
df_drop_all2 = df[['대여소번호', '대여거치대', '이용시간']].dropna(axis=1)
print(df_drop_all2)

#결측값을 측정 값(0)으로 대체
df_1 = df.fillna(0)
print(df_1)

#특정 컬럼 결측값을 특정 값(0)으로 대체
df_2 = df.대여소번호.fillna(0) #df_2 = df['대여소번호'].fillna(0)
print(df_2)

#결측값을 문자열 'missing'으로 대체
df_3 = df.fillna('missing')
print(df_3)

#각 컬럼의 평균을 구해, 대응하는 컬럼의 결측값을 대체
df_4 = df.fillna(df.mean())
print(df_4)

#특정 항목 평균구하기(이용거리 평균)
df_5 = df.mean()['이용거리']
print("이용거리 평균 :", df_5)

#특정 항목 평균으로 대체
df_6 = df.fillna(df.mean()['이용거리']) #결측값을 이용거리 평균으로 대체
print(df_6)

#특정 항목 평균으로 대체
df_7 = df.이용거리.fillna(df.mean()['이용거리']) #df_2 = df['이용거리'].fillna(df.mean()['이용거리'])
print(df_7)