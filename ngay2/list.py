
s = 'datcbvn'
a = list(s)
print(a)
b = list(range(10))
print(b)
print(a[1])
print(a[-1])
for i in range(0,len(a)):
    print(a[i],end=' ')
print('\n')
for item in a:
    print(item, end=' ')
print('\n')
a[2] = 'tuan'
a.append(10)
a.insert(-2,100)
a.pop(-2)
#  append them vao cuoi
# them vao chi so bat ky insert
# pop la xoa 
for bien in a:
    print(bien,end=' ')