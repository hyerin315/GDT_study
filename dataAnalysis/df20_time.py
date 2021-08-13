# Period 객체
# Period 객체는 to_period(freq = '기간인수')로
# datetime 변수에 어떤 기간에 따른 자료형을 생성하고자 할 때 주로 활용

# 시간 정의
import pandas as pd

dates = ['2020-01-01', '2020-03-01', '2021-09-01']
print(dates)

# 시간 자료형 생성
ts_dates = pd.to_datetime(dates)
print(ts_dates)

# Timestamp를 Period 변환
pr_day = ts_dates.to_period(freq="D") #1일 기간
print(pr_day)

pr_month = ts_dates.to_period(freq="M") #1개월 기간
print(pr_month)

pr_year = ts_dates.to_period(freq="A") #1년 기간
print(pr_year)