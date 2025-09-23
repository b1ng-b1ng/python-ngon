import pandas as pd

# data = [1,2,3,4]
# data = pd.Series(data,index=['a','b','c','d'])
# print(data.loc['a'])
df = pd.read_csv("C:\\du-an-python\\ngay2\\data.csv",index_col='Name')
#  duyet theo cot
#  tim theo ten
name_pokemon = input('nhap ten pokemon can tim: ')
try:
    print(df.loc[name_pokemon])
except KeyError:
    print(f'{name_pokemon} not found')
print(df.iloc[0:11])