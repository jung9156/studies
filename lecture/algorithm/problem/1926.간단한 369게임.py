def sam(x):
    k = str(x)
    kk = ''
    for i in k:
        if int(i) in rull:
           kk += '-'
    if kk == '':
        return x
    else:
        return kk
n = int(input())
p = 1
rull = [3, 6, 9]
while p != n+1:
    print(sam(p),end=' ')
    p += 1