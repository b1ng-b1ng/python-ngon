# a = 10
# b = 25
# print(a,b)
# a,b = b,a
# print(a,b)
# c = a // b
# d = b**2
# # chia nguyen 
# print(c)
# # luy thua x**y
# print(d)
# a = input('nhap so a di bro: ')
# b = int(input('nhap so b di bro: '))
# print(type(a),a,sep='\n')
# print(type(b),b,sep='\n')
s = input('nhap 3 so: ')
a = s.split()
#  Sử dụng map để ép các phần tử trong List sang kiểu mong muốn
x , y, z = map (int ,a)
print('ket qua 1:',x + y + z)
x , y , z = a
print('ket qua 2: ',x + y + z)
print(a)
# combo
m,n,p,q = map(int,input('nhap 4 so nguyen: ').split())
print(type(m),m)
