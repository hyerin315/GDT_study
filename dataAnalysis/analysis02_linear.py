import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 데이터 불러오기
file_path = "./dataset/exam_sample_cor.csv"

# read_csv()로 데이터 프레임 변환
df = pd.read_csv(file_path)

# 시본으로 과학, 수학, 점수 상관분석
sns.lmplot(x='science', y='math', data=df).set(xlim=(60, 95))
plt.show()

# 회귀분석을 위해 종속(y=수학), 독립(x=과학)하는 모델 생성
# - 과학점수를 알면 수학점수 예상 가능

# 단순선형회귀 모형
lin_reg = sm.OLS.from_formula("math ~ science", df).fit()
print(lin_reg.summary())


