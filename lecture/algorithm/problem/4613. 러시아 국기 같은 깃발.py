def backt(a, b, k, s, n):
    global ma
    if k == n:
        if s != 0:
            cou = 0
            for idx, i7 in enumerate(b):
                cou += M - Rd[idx][color[i7]]
            if cou < ma:
                ma = cou
        return

    if s == 0:
        for i in a[:2]:
            b[k] = i
            backt(a, b, k+1, i, n)

    elif s == 1:
        for i in a[1:]:
            b[k] = i
            backt(a, b, k + 1, i, n)
    else:
        b[k] = s
        backt(a, b, k + 1, 2, n)





tn = int(input())
for ir in range(tn):
    N, M = map(int, input().split())
    Rd = [{} for iii in range(N)]
    graph = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
    color = ['W', 'B', 'R']
    for ii in range(N):
        A = list(input())
        Rd[ii]['W'] = A.count('W')
        Rd[ii]['B'] = A.count('B')
        Rd[ii]['R'] = A.count('R')

    ma = N * M + 1
    a = [0, 1, 2]
    b = [0] + [0 for i in range(N-2)] + [2]
    backt(a, b, 1, 0, N-1)
    print('#{} {}'.format(ir+1, ma))