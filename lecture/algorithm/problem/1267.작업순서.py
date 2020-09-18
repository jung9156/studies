for ir in range(10):
    V, E = list(map(int, input().split()))
    e = list(map(int, input().split()))
    graph = [list(0 for ii2 in range(V+1)) for jj2 in range(V+1)]
    print('#{} '.format(ir+1),end='')
    for ii in range(E):
        graph[e.pop(1)][e.pop(0)] = 1
    op = []
    ov = [0 for ii3 in range(V+1)]
    for ii4 in range(V+1):
        op.append(sum(graph[ii4]))
    stack = []
    for idx1, ii5 in enumerate(op):
        if ii5 == 0:
            stack.append(idx1)
    del stack[0]
    while len(stack) > 0:
        v = stack.pop(-1)
        print(v,end=' ')
        for w in range(V+1):
            if graph[w][v] == 1:
                ov[w] += 1
                if ov[w] == op[w]:
                    stack.append(w)
    print()