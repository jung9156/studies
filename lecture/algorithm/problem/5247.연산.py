from collections import deque


def bfs(k, v):
    global M, flag
    cal = [+1, +v, -1, -10]
    for i in range(4):
        q = v + cal[i]
        if q == M:
            visit[q] = k + 1
            stack.append(q)
            flag = 1
            return
        if q < 0 or q > 1000000:
            continue
        if visit[q] == 0:
            visit[q] = k + 1
            stack.append(v + cal[i])


for ir in range(int(input())):
    N, M = map(int, input().split())
    visit = [0 for i in range(1000001)]
    stack = deque()
    stack.append(N)
    k = 0
    visit[N] = 0
    flag = 0
    while True:
        if flag == 1:
            break
        v = stack.popleft()
        k = visit[v]
        bfs(k, v)
        if v == M:
            break
    print('#{} {}'.format(ir+1, visit[M]))