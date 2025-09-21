
def infor(name,job='xe om'):
    print(name,job)
def giaithua(n):
    res = 1
    for i in range(1, n + 1):
        res*=i
    return res
def lt(a,b):
    res = 1
    for i in range(b):
        res*=a
    return res
def kt(a):
    if a % 3 ==0 and a % 5 ==0:
        return True
    else: 
        return False
def tonghieu(a,b):
    tong = a + b
    hieu = a - b
    return tong, hieu
if __name__ == '__main__':
    # x,y = map(int,input('nhap x,y: ').split())
    # print('tong x + y =',tong(x,y))
    infor('dat','duc')
    infor('dat')
print(giaithua(5))
print(lt(2,10))
if kt(120):
    print('yes')
else:
    print('No')
print(tonghieu(10,22)) 