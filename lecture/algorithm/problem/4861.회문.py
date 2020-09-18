def find(x):
    xn = len(x)
    if xn % 2 == 0:
        if x[:xn//2] == x[xn-1:(xn//2)-1:-1]:
            return x
    else:
        if x[:xn//2] == x[xn-1:(xn//2):-1]:
            return x
def turn(y):
    a2 = [[0 for i6 in range(n)] for ii in range(n)]
    for i5 in range(n):
        for j5 in range(n):
            a2[i5][j5] = y[n-1 - j5][i5]
    return a2


tn = int(input())
for ir in range(tn):
    n, m = list(map(int, input().split()))
    a = [list(input()) for ii in range(n)]

    result = []
    for i1 in range(n):
        for i2 in range(n - m + 1):
            re = []
            for j2 in range(m):
                re.append(a[i1][i2+j2])
            if re == find(re):
                result.append(find(re))
    b = turn(a)
    for i2 in range(n):
        for i3 in range(n - m + 1):
            re = []
            for j3 in range(m):
                re.append(b[i2][i3+j3])
            if find(re) == re:
                result.append(find(re))
    print('#{} '.format(ir+1),end='')
    res = result[0]
    for iii in range(m):
        print(res[iii],end='')
    print()