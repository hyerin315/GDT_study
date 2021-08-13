import seaborn as sns

tips = sns.load_dataset("tips")

#axis = 0 : 행 지정(아래로)
#axis = 1 : 열지정(옆으로)

#행 합계 구하기
print(tips.sum(axis=1)) #옆으로 합산

#열 합계 구하기
print(tips.sum()) #아래로 합산(=디폴트 값)

print("-"*50)

#행 평균 구하기
print(tips.mean(axis=1))

#열 평균 구하기
print(tips.mean())

print("-"*50)

#순위구하기 상세 설정(https://hogni.tistory.com/48)
#행 순위 구하기
print(tips.rank(axis=1))

#열 순위 구하기
print(tips.rank())