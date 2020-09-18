for ir in range(10):
    n = int(input())
    n_l = []
    for i in range(100):
        n_l.append(list(map(int, input().split())))
    result = []
    sx, sy, cr1, cr2 = 0, 0, 0, 0
    sumcr = []
    sumx = []
    sumy = []

    for i in range(100):
        cr1 += n_l[i][i]
        cr2 += n_l[i][99-i]

        for j in range(100):
            sx += n_l[i][j]
            sy += n_l[j][i]

        sumx.append(sx)
        sumy.append(sy)
        sx, sy = 0, 0
    sumcr.append(cr1)
    sumcr.append(cr2)
    an = max(max(sumx), max(sumy), max(sumcr))
    print('#{} {}'.format(ir+1, an))