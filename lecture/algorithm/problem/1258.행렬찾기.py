tn = int(input())
for ir in range(tn):
    n = int(input())
    a = [list(map(int, input().split())) for ii in range(n)]
    ch = 0
    result = []
    pp = list(range(n))
    cou = 0
    di = 0
    dj = 0
    maxsize = 0
    for i1 in range(n):
        for j1 in range(n):
            if a[i1][j1] != 0:
                cou += 1
                qn = 1
                # result.append([i1, j1])
                while True:
                    if qn == 1:
                        if a[i1][j1+dj] == 0:

                            dj -= 1
                            qn = 0
                        else:
                            dj += 1

                    else:
                        if a[i1+di][j1] == 0:
                            di -= 1
                            km = (di + 1) * (dj + 1)
                            if maxsize < km:
                                maxsize = km
                            result.append([km, di+1, dj+1])

                            for i2 in range(di+1):
                                for j2 in range(dj+1):
                                    a[i1+i2][j1+j2] = 0

                            di , dj = 0, 0
                            break
                        else:
                           di += 1
    result2 = [[] for i4 in range(maxsize+1)]
    result3 = []
    def so(x):
        for i7 in range(len(x)-1):
            mama = i7
            for i8 in range(i7, len(x)):
                if x[mama][0] > x[i8][0]:
                    mama = i8
            x[mama], x[i7] = x[i7], x[mama]
        return x
    print('#{} {}'.format(ir+1, cou),end=' ')
    for i5 in result:
        result2[i5[0]].append([i5[1], i5[2]])
    # print(cou, result2)
    for i6 in result2:
        if len(i6) == 1:
            print(i6[0][0], i6[0][1],end=' ')
        elif len(i6) >= 2:
            i6 = so(i6)
            for i9 in range(len(i6)):
                print(i6[i9][0], i6[i9][1],end=' ')
    print()