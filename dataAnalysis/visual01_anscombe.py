import matplotlib.pyplot as plt
import seaborn as sns
import ssl # https : s = secure
ssl._create_default_https_context = ssl._create_unverified_context # https 기반으로 송신하기 위해 작성 (seaborn이 옛날에 https로 송신함)

# 앤스콤 데이터셋 로드 (seaborn 내장 데이터)
ans = sns.load_dataset('anscombe')
print(ans)

# 데이터 타입 보기
print(ans.dtypes)

# 기초 통계량이 같더라도 데이터 분포는 다를 수 있음
# dataset의 기초 통계량
print(ans.describe()) # 수치연산 가능한 int형만 보여줌

print(ans.groupby(['dataset']).describe())

# dataset 1 추출하여 그래프로 표현
data1 = ans[ans['dataset'] == 'I']
print(data1)

plt.plot(data1['x'], data1['y']) # 꺾은선
plt.plot(data1['x'], data1['y'], 'o') # 점모양
#plt.show()

# matplotlib로 그래프 그리기
# 1. 기본 틀 만들기 (figure)
# 2. 내부에 격자를 만들고 서브 플롯 생성 (add_subplot)
# 3. 각 격자에 플롯을 그린다
# 4. 타이틀 기본의 제목 등 부가적 작업을 수행

data2 = ans[ans['dataset'] == 'II']
data3 = ans[ans['dataset'] == 'III']
data4 = ans[ans['dataset'] == 'IV']
fig = plt.figure()

# 2*2 격자를 만들고 각 격자에 () 데이터셋의 플롯 그리기
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
print(fig)

# 각 격자에 개별 데이터셋의 플롯 그리기
ax1.plot(data1['x'], data1['y'], 'o')
ax2.plot(data2['x'], data2['y'], 'o')
ax3.plot(data3['x'], data3['y'], 'o')
ax4.plot(data4['x'], data4['y'], 'o')

# 각 서브플롯의 타이틀 추가
ax1.set_title('data1')
ax2.set_title('data2')
ax3.set_title('data3')
ax4.set_title('data4')
#plt.show()

# 레이아웃 조절
fig.tight_layout(pad=1.4, w_pad=2.5, h_pad=1.0)
plt.show()