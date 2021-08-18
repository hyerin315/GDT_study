import numpy                # 표본 집단을 랜덤 값으로 생성하기 위해 사용
from scipy import stats     # t 검정 수행을 위한 패키지 (내장)

# 집단 1, 2 비교
group1Heights = numpy.array([162, 168, 169, 165, 166, 168, 162, 172, 157, 173, 158, 169, 164, 170, 163, 175, 177, 162, 175, 177])
group2Heights = numpy.array([180, 181, 163, 164, 174, 169, 164, 172, 162, 171, 180, 168, 164, 169, 169, 178, 177, 167, 179, 172])
print(group1Heights.mean())
print(group2Heights.mean())

# 독립표본 T-검정 수행 (independent two-sample T-Test)
# 1. 대응 데이터가 없다
# 2. 독립된 두 표본 모집단에 정규 분포를 가정할 수 있는 경우
# 3. 평균값 차이에 대한 검정

# - 집단 1과 2에서 각각 20명을 추려, 각 집단의 키가 같은지 다른지 확인한다.
# - 귀무가설 : 두 집단의 평균 키는 차이가 없다 → 두 집단의 평균은 같다
# - 대립가설 : 두 집단의 평균 키는 차이가 있다
tTestResult = stats.ttest_ind(group1Heights, group2Heights)
print(tTestResult)

# t검정 통계량 = -1.825, pvalue = 0.075 / 평균 키는 차이가 없다