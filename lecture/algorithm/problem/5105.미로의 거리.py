def check(x):
    global q
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        if A[x[0]+dx[i]][x[1]+dy[i]] == 0 and visit[x[0]+dx[i]][x[1]+dy[i]] == 0:
            stack.append([x[0]+dx[i], x[1]+dy[i]])
        elif A[x[0]+dx[i]][x[1]+dy[i]] == 3:
            q = 3
            return

for tn in range(int(input())):
    N = int(input())
    A = []
    A.append([1 for i in range(N+2)])
    for i in range(N):
        A1 = [1] + list(map(int, input())) + [1]
        A.append(A1)
    A.append([1 for i in range(N+2)])
    st = []
    visit = [list(0 for i in range(N+2)) for i1 in range(N+2)]
    cnt = -1
    en = 1
    for i in range(1, N+1):
        for j in range(1, N+1):
            if A[i][j] == 2:
                st.append(i)
                st.append(j)
    stack = []
    queue = []
    stack.append(st)
    q = 0
    while True:
        if not stack and not queue:
            break
        if not queue:
            cnt += 1
            queue += stack
            stack.clear()
        v = queue.pop(0)
        visit[v[0]][v[1]] = 1
        check(v)
        if q == 3:
            en = 0
            break
    if en == 1:
        cnt = 0
    print('#{} {}'.format(tn+1, cnt))