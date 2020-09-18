tn = int(input())
for ir in range(tn):
    n, k = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    h2 = []
    hh2 = []
    for i in range(n):
        h = k
        for j in range(n):
            if a[i][j] == 0:
                if h != k:
                    h2.append(abs(k-h))
                h = k
            else:
                h -= a[i][j]
        if h != k:
            h2.append(abs(k - h))

    for i in range(n):
        hh = k
        for j in range(n):
            if a[j][i] == 0:
                if hh != k:
                    hh2.append(abs(k-hh))
                    hh = k
            else:
                hh -= a[j][i]
        hh2.append(abs(k - hh))


    ans = h2.count(k) + hh2.count(k)
    print('#{} '.format(ir+1),end='')
    print(ans)