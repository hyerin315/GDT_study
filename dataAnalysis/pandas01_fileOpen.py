from tabulate import tabulate
import pandas as pd

df1 = pd.read_csv("./dataset/bicycle.csv", engine="python", encoding="cp949")
print(tabulate(df1, headers='keys', tablefmt='psql'))

df2 = pd.read_excel("./dataset/bicycle.xlsx", engine='openpyxl')
print(tabulate(df2, headers='keys', tablefmt='psql'))

df3 = pd.read_json("./dataset/read.json", orient="str")
print(df3)

df1.to_csv("./dataset/bicycle02.csv")
df4 = pd.read_csv("dataset/bicycle02.csv")
print(df4)

df2.to_excel("./dataset/bicycle02.xlsx")
df5 = pd.read_excel("./dataset/bicycle02.xlsx", engine='openpyxl')
print(df5)

df3.to_json("./dataset/read02.json")
df6 = pd.read_json("dataset/read02.json", orient="str")
print(df6)