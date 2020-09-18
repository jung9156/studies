def go(x, y):
    global re
    if x == y:
        return

    g1 = y[0] - x[0]
    g2 = y[1] - x[1]

    if g1 * g2 > 0:
        q = min(abs(y[0] - x[0]), abs(y[1] - x[1]))
        if y[0] > x[0]:
            x[0] += q
            x[1] += q
        elif y[0] < x[0]:
            x[0] -= q
            x[1] -= q
        re += q

    re += abs(y[0] - x[0]) + abs(y[1] - x[1])


tn = int(input())
for ir in range(tn):
    re = 0
    W, H, N = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))

    for i1 in range(1, len(A)):
        go([A[i1-1][0], A[i1-1][1]], [A[i1][0], A[i1][1]])

    print('#{} {}'.format(ir+1, re))