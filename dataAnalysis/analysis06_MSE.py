import numpy as np

# x값, y값
X = [2, 4, 6, 8]        # 각 축의 값들을 리스트로 설정
Y = [81, 93, 91, 97]

# 평균 제곱 오차 (mean square error)
# 1. 임의의 직선 그리기
# 2. 이에 대한 평균 제곱 오차 구하기

# 가설을 위한 함수 (y = ax + b)
arbitrary_a, arbitrary_b = 3, 76
def predict(x):
    return arbitrary_a*x + arbitrary_b

# 평균 제곱 오차 (Mean Squared Error) 공식
def mse(y2, y1):
    return (((y2-y1)**2).mean())

# MSE 함수를 각 y 값에 대입해서 최종값을 구하는 함수
def mse_val(predictedValue, Y):
    result = sum([(Y[i]-predictedValue[i])**2 for i in range(len(Y))])
    return result/len(Y)

# 예측값이 들어갈 빈 리스트
predictedValue = []

# 모든 x값을 한 번씩 대입하여
for i in range(len(X)):
    # 그 결과에 해당하는 predict_result 리스트를 환성
    predictedValue.append(predict(X[i]))
    print("공부시간 = %.f, 성적 = %.f, 예측값 = %.f"%(X[i], Y[i], predict(Y[i])))

# 최종 MSE 출력
print("MSE : ", mse_val(predictedValue, Y))