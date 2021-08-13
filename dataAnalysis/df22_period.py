import numpy as np
import pandas as pd

# pd.date_range()를 사용해 날짜 값들을 만들어 전달
dates = pd.date_range('20200101', periods=6)

# 컬럼의 이름은 A, B, C, D라는 이름이 담긴 리스트에 추가
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD')) #randn : 가우시안 정규분포 값
print(df)

# 시계열 활용 날짜 데이터 분리 : dt.yearm dt.month, dt.day
df = pd.read_csv("./dataset/timeseries.csv") # 데이터 불러오기
df['new_Date'] = pd.to_datetime(df['Date']) # 시간 변수 추가
print(df)

# 년, 월, 일 추출
df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
print(df)

# to_period() 함수 이용해 표기 변경
df['Date_yr'] = df['new_Date'].dt.to_period(freq= 'A') # 연도까지
df['Date_m'] = df['new_Date'].dt.to_period(freq= 'M') #연월까지
print(df)

# 날짜 인덱스 지정
df.set_index('new_Date', inplace=True)
print(df)

# 날짜 인덱싱
print(df.loc['2015-07']) # 7월에 해당하는 row 인덱싱
print(df['2015-06-25' : '2018-06-20']) # 해당기간 인덱싱

# 오늘 날짜와 차이 열 추가
today = pd.to_datetime('2020-03-18')
df['time_diff'] = today - df.index
print(df)