import pandas as pd

df = pd.read_csv('C:\\du-an-python\\ngay2\\data.csv')
# mean tinh trung binh
# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.count())

# single col
# print(df['Height'].mean())
# print(df['Weight'].mean())
# print(df['Height'].min())
# print(df['Height'].max())

group = df.groupby('Type1')
# print(group['Height'].mean())
# print(group['Height'].sum())
# print(group['Height'].min())
print(group['Height'].count())