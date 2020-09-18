tn = int(input())
for ir in range(tn):
    d, n = list(input().split())
    n = int(n)
    a = list(map(int, d))
    b = []
    for i in range(len(a)):
        ma = max(a)
        b.append(ma)
        del a[a.index(ma)]
    a = list(map(int, d))
    while True:
        c = []
        if n == 0:
            break
        for i1 in range(len(a)):
            if b[i1] != a[i1]:
                c.append(i1)
        if len(c) == 0:
            if len(a) != len(set(a)):
                break
            else:
                if n % 2 == 1:
                    a[-1], a[-2] = a[-2], a[-1]
                break
        for i2 in c:
            if b[c[0]] == a[i2]:
                mm = i2
                break
        a[mm], a[c[0]] = a[c[0]], a[mm]
        n -= 1
    print('#{} '.format(ir+1),end='')
    for i in range(len(a)):
        print(a[i],end ='')
    print()