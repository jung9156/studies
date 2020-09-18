def check(n, re, visit):
    global result, N
    for i in range(N + 1):
        if G[n][i] == 1 and visit[i] == 0:
            visit[n] = 1
            check(i, re + 1, visit)
            visit[n] = 0
    if re > result:
        result = re


tn = int(input())
for ir in range(tn):
    N, M = map(int, input().split())
    result = 0
    G = [list(0 for i in range(N + 1)) for i1 in range(N + 1)]
    visit = [0 for i in range(N + 1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a][b] = 1
        G[b][a] = 1

    for i in range(1, N+1):
        check(i, 1, visit)
        visit = [0 for i in range(N + 1)]
    print('#{} {}'.format(ir+1, result))