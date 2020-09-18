def boo(a, b, k, n, s1, s2):
    global re
    if a.count(1) == n//2:
        if re > abs(s1 - s2):
            re = abs(s1 - s2)
        return

    for i in range(k, N):
        if a[i] == 0:
            a[i] = 1
            b[i] = 0
            ss = 0
            sss = 0
            for ii2 in range(i):
                sss += A[i][ii2]
            for ii3 in range(i+1, N):
                ss += A[i][ii3]
            boo(a, b, i+1, n, s1 + sss, s2 - ss)
            a[i] = 0
            b[i] = 1



tn = int(input())
for ir in range(tn):
    N = int(input())
    AA = [list(map(int, input().split())) for ii in range(N)]
    A = [list([] for i in range(N)) for i2 in range(N)]
    for p1 in range(N):
        for p2 in range(N):
            A[p1][p2] = AA[p1][p2] + AA[p2][p1]
    s1, s2 = 0, 0
    for i7 in range(N):
        for i8 in range(i7+1, N):
            s2 += A[i7][i8]
    a = [0] * N
    b = [1] * N
    re = 160000
    boo(a, b, 0, N, s1, s2)
    print('#{} {}'.format(ir+1, re))