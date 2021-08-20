import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# x값, y값
X = [2, 4, 6, 8]        # 각 축의 값들을 리스트로 설정
Y = [81, 93, 91, 97]

# 그래프로 나타내기
plt.figure(figsize=(8,5))
plt.scatter(X, Y)
plt.show()

# X, Y 리스트를 넘파이 배열로 변경 (인덱스로 하나씩 불러와 계산이 가능)
x, y = np.array(X), np.array(Y)

# 기울기(a)와 절편(b) 값 초기화
a, b = 0, 0

# 경사 하강법 (gradient descent) = 오차 줄이기 (수정하기)
# 1. 미분 기울기를 이용해 오차 비교 후, 가장 작은 방향으로 이동
#    - 이동시 잘못 이동시키면 위로 치솟으므로, 얼만큼 이동시킬지 신중해야함
#    - 이를 위해, 학습률을 통해 최적화(최적의 학습률 찾기) 과정을 거침
#    * y절편인 b 값이 너무 크면 오차도 함께 커지고, 너무 작아도 오차가 커짐
#      그래서 최적의 b값을 구할 때도 경사하강법 사용
# 2. 미분 값이 0인 지점 (가장 오차가 작을 때) 찾기

# 학습률 설정
lr = 0.05

# 반복횟수 설정 (0부터 시작하므로 +1 해줘야함)
epochs = 2001

# 경사 하강법 시작
for i in range(epochs):       # 에폭 수만큼 반복
    # a와 b 편미분에 대한 코드 (우리가 궁금한 것 = a, b)
    pred_y = a * x + b        # y를 구하는 식 세우기
    error = y - pred_y   # 오차를 구하는 식

    # 오차 함수를 a로 미분한 결과
    diff_a = -(1/len(x))*sum(x * (error))

    # 오차 함수를 b로 미분한 결과
    diff_b = -(1/len(x))*sum(y - pred_y)

    # 학습률을 곱해 기존값 업데이트
    a = a - lr * diff_a
    b = b - lr * diff_b

    # 100번 반복될 때마다 현재의 a값, b값 출력
    if i % 100 == 0 :
        print("epoch=%.f, 기울기는 %.04f, 절편=%.04f"%(i, a, b))

# 앞서 구한 기울기와 절편을 이용해 다시 그래프 생성
pred_y = a * x + b
plt.scatter(X, Y)              # 이전 값 그리기
plt.plot([min(x), max(x)], [min(pred_y), max(pred_y)])
plt.show()