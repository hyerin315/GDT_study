import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np

# 한글 타이틀
plt.rc("font", family='Malgun Gothic')

# 데이터 준비
iris = sns.load_dataset("iris")        # 붙꽃 데이터
titanic = sns.load_dataset("titanic")  # 타이타닉호 데이터
tips = sns.load_dataset("tips")        # 팁 데이터
lights = sns.load_dataset("flights")   # 여객 운송 데이터

# 기본 배경 설정
sns.set_palette("pastel")

# 시각화
sns.stripplot(x="day", y="total_bill", data=tips)

# 개인화
plt.title("팁데이터")
plt.ylabel("요금")
plt.xlabel("요일")
plt.show()