# n = 1 
# while n <= 5:
#     print('hi',n)
#     n+=1
# while True:
#     n= int(input('nhap n:'))
#     if n == 20:
#         break
n = 1234
kq = 0
while n != 0:
    kq+= n % 10
    n//=10
print(kq)
a = 1234
lat = 0
while a != 0:
    res = a%10
    lat = lat*10 + res
    a//=10
print(lat)