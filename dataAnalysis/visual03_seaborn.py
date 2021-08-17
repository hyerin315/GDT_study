import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 데이터 보기
tips = sns.load_dataset("tips")
print(tips)

# 기본 선
#tips.plot()
tips.plot(kind="line")

# 히스토그램
tips.plot(kind="hist")

# 박스 플롯
tips.plot(kind="box")

# 점
sns.set(style = "darkgrid")
sns.relplot(x = "total_bill", y = 'tip', hue = 'smoker', data = tips)

plt.show()