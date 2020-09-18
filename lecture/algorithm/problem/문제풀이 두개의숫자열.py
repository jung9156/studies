tn = int(input())
for ir in range(tn):
    m, n = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if m > n:
        a, b, m, n = b, a, n, m

    suml = []
    sumax = -9999999999999999
    for i in range(n - (m-1)):
        su = 0
        for j in range(m):
            su += a[j]*b[i+j]
        if sumax < su:
            sumax = su
    print('#{} {}'.format(ir+1,sumax))