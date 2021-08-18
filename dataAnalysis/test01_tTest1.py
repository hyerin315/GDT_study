import numpy                # 표본 집단을 랜덤 값으로 생성하기 위해 사용
from scipy import stats     # t 검정 수행을 위한 패키지 (내장)

# 학생 키에 대한 리스트 구성
height_list = numpy.array([169, 167, 175, 166, 162, 180, 172, 162, 173, 162, 181, 175, 181, 181, 162, 165, 172, 176, 167, 165])
print(height_list)


# 단일표본 T-검정 수행 (one-sample T-Test)
# 1. 하나의 집단으로부터 얻은 표본이(단일표본) 있다
# 2. 그 중 관심있는 연속형 변수의 모평균이 어떤 특정값과 같은지 알아보고자 할 때 사

# - 20개의 샘플 데이터를 통해, 평균 키가 설정 값과 차이가 있는지 비교한다.
# - 귀무가설 : 학생들의 평균 키가 170cm와 차이가 없다. → 평균 키는 170cm이다. (P > 0.05)
# - 대립가설 : 학생들의 평균 키가 170cm와 차이가 있다.
tTestResult = stats.ttest_1samp(height_list, 170)
print(tTestResult)

# 결과출력
# - 귀무가설이 맞거나 틀린 것을 증명하려면 어떠한 증거가 있어야 한다.
#   이 증거에 해당하는 숫자를 '검정 통계량(test statistics)라고 한다.
print("t검정 통계량 = %.3f, pvalue = %.3f"%(tTestResult))

# t검정 통계량 = 0.423, pvalue = 0.677 : 값 비교를 통해 어떤 가설이 타당한지 증거 제시