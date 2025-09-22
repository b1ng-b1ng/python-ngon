import pandas as pd

df = pd.read_csv("C:\\du-an-python\\ngay2\\data.csv",index_col='Name')

# # selection col
# print(df['Name'].to_string())
# print(df['Height'])
# print(df[['Name','Type1']].to_string())
# # select by row
# print(df.loc['Kakuna':'Spearow',['Height','Weight']])
# print(df.iloc[0:11,0:3])
# [0:11] lấy 11 con đầu , step mặc định là 1 [0,11,1]
# [0:3] lấy 3 cột đầu tiên
pokemon = input('Nhap vao ten pokemon may muon tim:')
try:
    print(df.loc[pokemon])
except KeyError:
    print(f'{pokemon} not found')