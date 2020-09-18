for ir in range(int(input())):
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for k in range(n)]
    na = []
    na2 = []
    nb = []
    nb2 = []
    for i in range(n):
        for j in range(n-(m-1)):
            kk = 0

            for mm in range(m):
                kk += a[i][j+mm]
            na.append(kk)
        na2.append(na)
        na = []
    for i2 in range(n-(m-1)):
        for j2 in range(n-(m-1)):
            k = 0
            for m2 in range(m):
                k += na2[j2+m2][i2]
            nb.append(k)

    print('#{} {}'.format(ir+1, max(nb)))