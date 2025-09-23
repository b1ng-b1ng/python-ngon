import pandas as pd

df = pd.read_csv("C:\\du-an-python\\ngay2\\data-test.csv")

# df = df.drop(columns=['Legendary','Type1'])

# df = df.dropna(subset=['Type2'])
# 2.Thay thế những chỗ không có của cột X bằng từ {'Y'}
# df = df.fillna({'Type2':'None'})
# 3.Sửa Giá trị trong cột
# df['Type1'] = df['Type1'].replace({'Grass' : 'GRASS',
#                                    'Fire' : 'FIRE'
#                                    })
# df['Name'] = df['Name'].str.lower()
#  5. Fix data types
df['Legendary'] = df['Legendary'].astype(bool)
# 6 xoa du lieu giong nhau
df = df.drop_duplicates()
print(df.to_string())