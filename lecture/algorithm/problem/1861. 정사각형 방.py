def find_load(x):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        if 0 <= x[0] + dx[i] < N and 0 <= x[1] + dy[i] < N and A[x[0] + dx[i]][x[1] + dy[i]] == A[x[0]][x[1]] + 1 and visit[x[0] + dx[i]][x[1] + dy[i]] == 0:
            return [x[0] + dx[i], x[1] + dy[i]]


tn = int(input())
for ir in range(tn):
    N = int(input())
    A = [list(map(int, input().split())) for ii in range(N)]
    re = [0, 0]
    stp = [[] for i in range(N**2+1)]
    for i1 in range(N):
        for i2 in range(N):
            stp[A[i1][i2]] += [i1, i2]
    stack = []
    visit = [list(0 for i in range(N)) for i1 in range(N)]
    for go in range(1, len(stp)):
        if visit[stp[go][0]][stp[go][1]] == 0:
            stack.append(stp[go]) #길 찾기
        cnt = 0
        while stack:
            v = stack.pop(-1)
            visit[v[0]][v[1]] = 1
            cnt += 1
            w = find_load(v)
            if w:
                stack.append(w)
            else:
                if re[1] < cnt:
                    re = [go, cnt]
    re2 = ' '.join(map(str, re))
    print('#{} {}'.format(ir+1, re2))