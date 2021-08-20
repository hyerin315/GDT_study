import matplotlib as mpl
import matplotlib.pyplot as plt

X = [2, 4, 6, 8]
Y = [81, 93, 91, 97]

# 그래프 그리기
mpl.style.use('seaborn-whitegrid')  # 그래프 눈금표시
plt.xlabel('$x$', fontsize=25)      # 축 이름, font 사이즈
plt.ylabel('$y$', fontsize=25)
plt.xlim(xmin=0, xmax=10)           # 각 축별 최소값, 최대값
plt.ylim(ymin=0, ymax=100)

plt.plot(X, Y, 'k')      # 선 그리기
plt.plot(X, Y, 'or')     # 점 그리기
# plt.show()             # 화면에 그래프 그리기

# 최소 제곱법(method of least squares)
# 1. 평균 계산
# 2. 기울기 계산

# X축의 평균값 계산
x_total = 0
for x in X:
    x_total += x

x_mean = x_total/len(X)
print("Mean of X : ", x_mean)

# Y축의 평균값 계산
y_total = 0
for y in Y:
    y_total += y

y_mean = y_total/len(Y)
print("Mean of Y : ", y_mean)

# 기울기 계산
numerator, denominator = 0, 0
for i in range(len(X)):
    numerator += (X[i] - x_mean)*(Y[i] - y_mean)
    denominator += (X[i] - x_mean)**2       # 제곱을 하면 양수의 값만 나옴

a = numerator/denominator                   # a : 기울기
print("Lean : ", a)

b = y_mean - (x_mean*a)                     # b : 절편
print("Intercept of Y : ", b)

# 예측값 계산
predictedValue = []
for x in [2, 4, 6, 8]:
    value = a * x + b                       # y = ax + b
    print(value, end="")
    predictedValue.append(value)
print()

mpl.style.use('seaborn-whitegrid')     # 그래프 눈금 표시
plt.xlabel('$x$', fontsize=25)         # 축 이름, font 사이즈
plt.ylabel('$y$', fontsize=25)

plt.xlim(xmin=0, xmax=10)              # 각 축별 최소값, 최대값
plt.ylim(ymin=0, ymax=100)

plt.plot(X, Y, color='blue', marker='o')                 # 점 그리기
plt.plot(X, predictedValue, color='red', marker='o')     # 점 그리기
plt.show()

