def search(i, j):
    if A[i][j] == 3:
        return 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for _ in range(4):
        if A[i+dx[_]][j+dy[_]] != 1 and vis[i+dx[_]][j+dy[_]] == 0:
            vis[i+dx[_]][j+dy[_]] = 1
            if search(i + dx[_], j + dy[_]) == 1:
                return 1
    return 0

tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N = int(input())
    a = [1]#1 ~ N+1 까지
    A =[[1 for ii in range(N+2)]] + [(a + list(map(int, input())) + a) for ii in range(N)] + [[1 for ii in range(N+2)]]
    vis = [[0 for _ in range(N+2)] for _ in range(N+2)]
    st2 = -1
    st = 0
    for ii1 in range(N+2):
        for i1 in range(N+2):
            if A[ii1][i1] == 2:
                st2 = ii1
                st = i1
                break
        if st2 != -1:
            break
    q = search(st2, st)
    print(q)