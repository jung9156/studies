tn = int(input())
result = []
for ir in range(tn):
    N, M = map(int, input().split())
    graph = [[0 for i in range(N+1)] for i1 in range(N+1)]
    for i in range(M):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1
    test = 0
    for i2 in range(1, N+1):
        for j in range(i2+1, N+1):
            for j2 in range(j+1, N+1):
                if graph[i2][j] == graph[j][j2] == graph[j2][i2] == 1:
                    test += 1
    result.append(test)

for ir in range(tn):
    print('#{} {}'.format(ir+1, result[ir]))