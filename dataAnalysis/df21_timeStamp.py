import pandas as pd
import matplotlib

file_path = "./dataset/timeseries.csv"
df = pd.read_csv(file_path)
print(df.info())

#Date 컬럼 시계열 객체(Timestamp로 변환
df['new_Date'] = pd.to_datetime(df['Date'])
print(df.info())

#데이터 프레임 확인
print(df.head())

print(type(df['new_Date'][0]))

#기존 Date열 삭제
df.drop('Date', axis=1, inplace=True)

#new_Date를 인덱스로 지정
df.set_index('new_Date', inplace=True)
print(df)

#간단한 시계열 시각화
df.plot.line()
matplotlib.pyplot.show()