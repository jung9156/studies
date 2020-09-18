def turn(x):
    xx = [list(0 for i5 in range(100)) for j5 in range(100)]
    for i6 in range(100):
        for j6 in range(100):
            xx[i6][j6] = x[99-j6][i6]
    return xx

# tn = int(input())
for ir in range(10):
    n = int(input())
    a = [list(input()) for ii in range(100)]
    result = 0
    N1 = 0
    for i1 in range(100):
        for j1 in range(100):
            for j2 in range(j1+result, 100):
                if a[i1][j1] == a[i1][j2]:
                    N1 = 1
                    while True:
                        for i7 in range((j2-j1)//2):
                            if a[i1][j1+N1] == a[i1][j2-N1]:
                                N1 += 1
                            else:
                                break
                        else:
                            if result < j2-j1+1:
                                result = j2-j1+1
                        break
    c = turn(a)
    for i1 in range(100):
        for j1 in range(100):
            for j2 in range(j1+result, 100):
                if c[i1][j1] == c[i1][j2]:
                    N1 = 1
                    while True:
                        for i7 in range((j2-j1)//2):
                            if c[i1][j1+N1] == c[i1][j2-N1]:
                                N1 += 1
                            else:
                                break
                        else:
                            if result < j2-j1+1:
                                result = j2-j1+1
                        break
    print('#{} {}'.format(ir+1, result))