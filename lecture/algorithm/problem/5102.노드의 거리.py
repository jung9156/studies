tn = int(input())
result = []
for ir in range(tn):
    V, E = map(int, input().split())
    graph = [list(0 for i1 in range(V+1)) for i2 in range(V+1)]
    for i in range(E):
        g1, g2 = map(int, input().split())
        graph[g1][g2] = 1
        graph[g2][g1] = 1
    S, G = map(int, input().split())
    cnt = -1
    stack = []
    queue = []
    en = 0
    visit = list(0 for i in range(V+1))
    stack.append(S)
    while True:
        if not stack and not queue:
            break

        if not queue:
            cnt += 1
            queue += stack
            stack.clear()
        v = queue.pop(0)
        if v == G:
            en = 1
            break

        visit[v] = 1
        for i in range(1, V + 1):
            if graph[v][i] == 1 and visit[i] == 0:
                stack.append(i)
    if en == 0:
        cnt = 0
    result.append(cnt)

for i in range(tn):
    print('#{} {}'.format(i+1, result[i]))