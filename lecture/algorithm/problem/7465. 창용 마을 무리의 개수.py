tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N, M = map(int, input().split())
    graph = [list(0 for ii in range(N+1)) for jj in range(N+1)]
    for i1 in range(M):
        g1, g2 = map(int, input().split())
        graph[g1][g2] = 1
        graph[g2][g1] = 1
    visit1 = [0 for i in range(N+1)]
    visit2 = [0 for i in range(N+1)]
    re = 0
    stack = []
    while visit1.count(0) != 1:
        for idx, i in enumerate(visit1):
            if idx != 0:
                if i == 0:
                    stack.append(idx)
                    re += 1
                    break
        while stack:
            v = stack.pop(-1)
            visit1[v] = 1
            for i2 in range(1, N+1):
                if graph[v][i2] == 1 and visit1[i2] == 0:
                    stack.append(i2)
    print(re)