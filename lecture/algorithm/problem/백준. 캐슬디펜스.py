import copy

def play(i1, i2, i3):
    global A_2, max_heat, cnt
    while True:
        go = 0
        for __ in range(N):
            for ___ in range(M):
                if A_2[__][___] == 1:
                    go = 1
                    break
        if go == 1:
            target = search(i1, i2, i3)
            shoot(target)
            A_2 = move(A_2)
            if max_heat < cnt:
                max_heat = cnt
        else:
            break

def search(i1, i2, i3):
    global A_2
    arc = [[N, i1], [N, i2], [N, i3]]
    target = []
    dx = [0, -1, 0]
    dy = [-1, 0, 1]
    target2 = []
    for pi in range(3):
        stack = []
        queue = []
        visit = [list(0 for _ in range(M)) for _2 in range(N)]
        visit.append([1 for _3 in range(M)])
        d = 0
        mon = 0
        stack.append([arc[pi][0], arc[pi][1]])
        target2 = [[] for i in range(D)]
        while True:
            if d == D or mon == 1:
                if len(queue) == 0:
                    break
            if not queue:
                queue += stack
                stack = []
                d += 1
            v = queue.pop(0)
            visit[v[0]][v[1]] = 1
            for pi2 in range(3):
                if 0 <= v[0] + dx[pi2] <= N - 1 and 0 <= v[1] + dy[pi2] <= M - 1:
                    if A_2[v[0] + dx[pi2]][v[1] + dy[pi2]] == 1:
                        target2[d-1].append([v[0] + dx[pi2], v[1] + dy[pi2]])
                        mon = 1
                    else:
                        if visit[v[0] + dx[pi2]][v[1] + dy[pi2]] == 0:
                            stack.append([v[0] + dx[pi2], v[1] + dy[pi2]])
        for i in range(D):
            if target2[i]:
                if len(target2[i]) > 1:
                    for ti1 in range(len(target2[i])-1):
                        tmm = ti1
                        for ti2 in range(ti1+1, len(target2[i])):
                            if target2[i][tmm][1] > target2[i][ti2][1]:
                                tmm = ti2
                        target2[i][ti1], target2[i][tmm] = target2[i][tmm], target2[i][ti1]
                target.append(target2[i][0])

    return target


def shoot(xx):
    global cnt
    for si in range(len(xx)):
        if A_2[xx[si][0]][xx[si][1]] == 1:
            cnt += 1
            A_2[xx[si][0]][xx[si][1]] = 0


def move(x):
    x = [[0 for i in range(M)]] + A_2[:N - 1]
    return x



N, M, D = map(int, input().split())
A = [list(map(int, input().split())) for iii in range(N)]
A.append([0 for iii2 in range(M)])
max_heat = 0
for i1 in range(M - 2):
    for i2 in range(i1 + 1, M - 1):
        for i3 in range(i2 + 1, M):
            A_2 = copy.deepcopy(A)
            cnt = 0
            play(i1, i2, i3)
print(max_heat)