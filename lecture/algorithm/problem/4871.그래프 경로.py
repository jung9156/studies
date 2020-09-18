tn = int(input())
for ir in range(tn):
    V, E = list(map(int, input().split()))
    ilist = []
    jlist = []
    stack = []
    graph = [list(0 for i1 in range(V+1)) for i2 in range(V+1)]
    for i1 in range(E):
        g1, g2 = list(map(int, input().split()))
        ilist.append(g1)
        jlist.append(g2)
    for i3 in range(E):
        graph[ilist[i3]][jlist[i3]] = 1
    n1, n2 = list(map(int, input().split()))
    stack.append(n1)
    visit = [0 for ii1 in range(V+1)]
    print('#{} '.format(ir+1),end='')
    while len(stack) > 0:
        v = stack.pop(-1)
        visit[v] = 1
        if v == n2:
            print(1)
            break
        for i5 in range(V+1):
            if graph[v][i5] == 1:
                stack.append(i5)

    if visit[n2] == 0:
        print(0)