for ir in range(10):
    N, st = map(int, input().split())
    A = list(map(int, input().split()))
    G = [list(0 for i in range(101)) for ii in range(101)]
    for i in range(0, N, 2):
        G[A[i]][A[i+1]] = 1
    result = []
    visit = list(0 for i in range(101))

    stack = [st]
    queue = []
    visit[st] = 1
    while True:
        if not stack and not queue:
            break
        if not queue:
            queue = stack[:]
            stack = []

        v = queue.pop(0)
        for i in range(101):
            if G[v][i] == 1 and visit[i] == 0:
                visit[i] = 1
                if not stack:
                    result = []
                stack.append(i)
                result.append(i)
    print('#{} {}'.format(ir+1, max(result)))