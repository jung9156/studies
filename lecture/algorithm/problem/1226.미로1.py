def check(ix, jx):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i1 in range(4):
        if a[ix + dx[i1]][jx + dy[i1]] != 1:
            if visit[ix + dx[i1]][jx + dy[i1]] != 1:
                stack.append(ix + dx[i1])
                stack.append(jx + dy[i1])
# tn = int(input())
for ir in range(10):
    n = int(input())
    a = [list(map(int, input())) for ii in range(16)]
    sp = []
    for st in range(16):
        for st2 in range(16):
            if a[st][st2] == 2:
                sp.append(st)
                sp.append(st2)
                break
    print('#{} '.format(ir+1),end='')

    stack = [sp[0], sp[1]]
    visit = [list(0 for iii in range(16)) for jjj in range(16)]

    while len(stack) > 0:
        if a[stack[-2]][stack[-1]] == 3:
            print(1)
            break
        visit[stack[-2]][stack[-1]] = 1
        check(stack[-2], stack[-1])
        if visit[stack[-2]][stack[-1]] != 0:
            stack.pop(-1)
            stack.pop(-1)
    if len(stack) == 0:
        print(0)