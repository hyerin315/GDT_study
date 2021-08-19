import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
import seaborn as sns
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# 데이터 불러오기
file_path = "./dataset/exam_sample_cor.csv"

# read_csv()로 데이터 프레임 변환
df = pd.read_csv(file_path)
print(df.info())
print(df.describe())

# 두 연속형 변수 스캐터 플롯 그리기
plt.scatter(df.science, df.math)
plt.xlabel('science')
plt.ylabel('math')
plt.show()

print("-" * 50)

# 상관계수 확인
corr = df.corr() # method = 'person'
print(corr)


# 히트맵 1. 히트맵으로 상관도 시각화 (학생 번호는 각 컬럼과 상관이 없음)
sns.heatmap(data=df.corr(), annot=True, fmt=".2f", linewidths=.5, cmap="Blues")
plt.show()


# 히트맵 2. 대칭 부분 중 한 부분만 그리기 (삼각형으로 그리기)
fig, ax = plt.subplots(figsize=(7,7))  # 그림 사이즈 지정

# 삼각형 마스크 작성 (위 삼각형 True, 아래 삼각형 False)
mask = np.zeros_like(corr, dtype=np.bool_)
mask[np.triu_indices_from(mask)] = True

# df 히트맵 그리기
sns.heatmap(corr, cmap="RdYlBu_r",       # Red, Yellow, Blue 색상으로 표시
            annot=True,                 # 실제값 표시
            mask=mask,                  # 표시하지 않을 마스크 부분을 지정
            linewidths=.5,              # 경계면 실선으로 구분하기
            cbar_kws={"shrink": .5},    # 컬러바 크기 절반으로 줄이기
            vmin=-1, vmax=1)            # 컬러바 범위 -1~1

# corr 히트맵 그리기
sns.clustermap(corr, annot=True,        # 실제값 표시
               cmap="RdYlBu_r",         # Red, Yellow, Blue 색상으로 표시
               vmin=-1, vmax=1)         # 컬러바 범위 -1~1
plt.show()

