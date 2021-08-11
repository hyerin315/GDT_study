import pickle
import pandas as pd

temp = pd.DataFrame({'a':[1], 'b':[2]})

#데이터 저장
temp.to_pickle("./dataset/temp01.pkl")

#데이터 로드
data = pd.read_pickle("./dataset/temp01.pkl")
print(data)