def doo(x, y, k, N):
    global result
    if k >= result:
        return
    if x == N-1 and y == N-1:
        if k < result:
            result = k
        return
    i, j = x, y
    dir = [[0, 1], [1, 0]]
    for d in dir:
        i1, j1 = i + d[0], j + d[1]
        if i1 <= N-1 and j1 <= N-1:
            doo(i1, j1, k + A[i1][j1], N)


for ir in range(int(input())):
    N = int(input())
    A = list(list(map(int, input().split())) for i in range(N))
    result = 2000
    doo(0, 0, A[0][0], N)
    print('#{} {}'.format(ir+1, result))