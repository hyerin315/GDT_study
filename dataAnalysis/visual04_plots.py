import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import seaborn as sns
import numpy as np

tips = sns.load_dataset("tips")

# 선 그래프
plt.plot(tips.total_bill)
plt.show()

# 막대 그래프
plt.bar(tips.sex, tips.total_bill) # x축 범주형, y축 연속형
plt.show()

# 산점도
plt.scatter(tips.total_bill, tips.tip) # x축 범주형, y축 연속형
plt.show()

# 히스토그램
plt.hist(tips.total_bill)
plt.show()
plt.hist(tips.time)
plt.show()