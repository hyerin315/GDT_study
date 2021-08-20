import numpy as np

# 최소 제곱법(method of least squares)
# 1. 평균 계산
# 2. 기울기 계산

# x값, y값
X = [2, 4, 6, 8]        # 각 축의 값들을 리스트로 설정
Y = [81, 93, 91, 97]


# moduCorrelation과 다르게 간결하게 구현하기

# X와 Y의 평균값
x_mean = np.mean(X)
y_mean = np.mean(Y)

# 기울기 공식의 분자 계산을 위한 함수 선언
def top(x, x_mean, y, y_mean):
    res = 0
    for i in range(len(x)):
        res += (x[i] - x_mean)*(y[i]-y_mean)
    return res

numerator = top(X, x_mean, Y, y_mean)  # 기울기 공식의 분자 계산

# 기울시 공식의 분모 계산
denominator = sum([(i - x_mean)**2 for i in X])

# 기울기와 y절편 출력
a = numerator/denominator

