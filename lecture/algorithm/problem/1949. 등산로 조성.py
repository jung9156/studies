def backt(x, n, Am, k, visit):
    global result
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in range(4):
        fi, fj = x[0] + dir[i][0], x[1] + dir[i][1]
        if 0 <= fi < N and 0 <= fj < N and visit[fi][fj] != 1:
            if A[fi][fj] >= Am:
                if A[fi][fj] - k < Am:
                    visit[fi][fj] = 1
                    backt([fi, fj], n + 1, Am - 1, 0, visit)
                    visit[fi][fj] = 0
            else:
                visit[fi][fj] = 1
                backt([fi, fj], n + 1, A[fi][fj], k, visit)
                visit[fi][fj] = 0
    if result < n:
        result = n
    return



tn = int(input())
for ir in range(tn):
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for ii in range(N)]
    stp = []
    Am = 0
    result = 0
    for i1 in range(N):
        for j1 in range(N):
            if A[i1][j1] > Am:
                stp.clear()
                Am = A[i1][j1]
                stp.append([i1, j1])
            elif A[i1][j1] == Am:
                stp.append([i1, j1])

    rec = []
    stack = []
    for i in range(len(stp)):
        visit = [list(0 for i in range(N)) for ii in range(N)]
        visit[stp[i][0]][stp[i][1]] = 1
        backt(stp[i], 1, Am, K, visit)
    print('#{} {}'.format(ir+1, result))