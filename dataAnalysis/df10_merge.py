import pandas as pd

df1 = pd.DataFrame({'고객번호' : [1001, 1002, 1003, 1004, 1005, 1006, 1007],
                    '이름' : ['강감찬', '홍길동', '이순신', '장보고', '유관순', '신사임당', '세종대왕']},
                   columns=['고객번호', '이름'])
print(df1)

df2 = pd.DataFrame({'고객번호' : [1001, 1001, 1005, 1006, 1008, 1001],
                    '금액' : [10000, 20000, 15000, 5000, 100000, 30000]},
                   columns=['고객번호', '금액'])
print(df2)

print("-"*50)

#inner join
print(pd.merge(df1, df2, on = '고객번호')) #how 명시 안할 경우, inner join이 디폴트값
print(pd.merge(df1, df2, how='inner', on = '고객번호'))

print("-"*50)

#full join 방식은 키 값이 한 쪽에만 있어도 데이터 출력 (NaN으로 결측값 표시)
print(pd.merge(df1, df2, how='outer', on='고객번호'))

print("-"*50)

#left join (첫번째 데이터 프레임의 키값 중심으로 출력)
print(pd.merge(df1, df2, how='left', on='고객번호'))

print("-"*50)

#right join (두번째 데이터 프레임의 키값 중심으로 출력)
print(pd.merge(df1, df2, how='right', on='고객번호'))
