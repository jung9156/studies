def dfs(graphs, ver, s, f):
    # graphs = 인접행렬, ver = 정점 개수, s = 시작점, f = 도착점
    visited = [0] * (ver+1)
    stack = []
    stack.append(s)
    while len(stack) > 0:
        v = stack.pop(-1)
        visited[v] = 1
        for w in range(1, ver + 1):
            if graphs[v][w] == 1:
                stack.append(w)
            if w == f:
                return 1
    return 0

T = int(input())
for tc in range(1, T+1):
    vertex, edge = map(int, input().split())
    graph = [[0]*(vertex+1) for _ in range(vertex+1)]

    for i in range(edge):
        r, c = map(int, input().split())
        graph[r][c] = 1

    start, finish = map(int, input().split())
    result = dfs(graph, vertex, start, finish)
    print("#{0} {1}".format(tc, result))