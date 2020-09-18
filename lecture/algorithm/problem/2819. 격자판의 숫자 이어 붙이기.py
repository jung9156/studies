def dfs(x, k, n, s):
    if k == n:
        result.add(s)
        return
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        if 0 <= x[0] + dx[i] < 4 and 0 <= x[1] + dy[i] < 4:
            dfs([x[0] + dx[i], x[1] + dy[i]], k+1, n, s + A[x[0]][x[1]])


tn = int(input())
for ir in range(tn):
    A = [list(map(str, input().split())) for ii in range(4)]
    result = set()
    for i1 in range(4):
        for j1 in range(4):
            dfs([i1, j1], 0, 7, '')
    print('#{} {}'.format(ir+1, len(result)))