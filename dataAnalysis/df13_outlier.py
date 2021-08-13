import matplotlib.pyplot as plt
import pandas as pd

#파일 경로를 찾아 변수에 저장
file_path = "./dataset/bicycle.csv"
df = pd.read_csv(file_path, encoding="cp949")
print(df)

#이상값이 있는 4번째 행 제거
df1 = df.drop(4, 0)
print(df1)

print("-"*50)

#이용시간 이상치 시각화
file_path2 = "./dataset/bicycle_out.csv"
df2 = pd.read_csv(file_path2, encoding="cp949")
print(df2)

plt.boxplot(df2['나이'])
plt.show()