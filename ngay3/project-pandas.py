import pandas as pd

df = pd.read_csv("C:\\du-an-python\\ngay3\\sales.csv")

df['Doanh thu'] = df['quantity'] * df['price']
print(df)
doanhthu_sanpham = df.groupby('product')['Doanh thu'].sum()
print('Tong Doanh thu',doanhthu_sanpham.sum())
doanhthu_apple = doanhthu_sanpham['Apple']
print('Doanh thu tao:', doanhthu_apple)
doanhthu_banana = doanhthu_sanpham['Banana']
print('Doanh thu chuoi:', doanhthu_banana)