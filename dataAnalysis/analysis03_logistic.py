import pandas as pd
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib as mpl
import matplotlib.pylab as plt
import numpy as np
import seaborn as sns
import statsmodels.api as sm
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# %matplotlib inline

# 로지스틱 회귀함수에 맞는 DataFrame 생성 (0, 1로 이루어짐)
passtest = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
score = [51, 64, 60, 50, 68, 80, 90, 92, 99, 83]
df = pd.DataFrame({"passtest": passtest, "score": score})
print(df.head())

# 상관분석
# - 0, 1로 이루어져 있기 때문에 직선형으로 그래프가 그려지지 않음
# - 계단식 그래프로 서로 이어지지 않기 때문에 시그모이드 함수를 사용해야함
# sns.lmplot(x="score", y="passtest", data=df, logistic=True).set(xlim=(45, 100))
# plt.show()


# 로지스틱 회귀함수 그래프화 - sigmoid 함수 사용
# - y=ax+b에서 a는 1, b는 0으로 가정
# - 여기서는 위의 데이터프레임을 활용하지 않고 그래프만 그림
def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)

plt.plot(x, y, 'g')
plt.plot([0, 0], [1.0, 0.0], ':') # 가운데 점선 추가
plt.title('Sigmoid Function')
plt.show()
