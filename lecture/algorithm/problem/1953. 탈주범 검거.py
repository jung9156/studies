def back(x, y):
    dx = [[], [-1, 1, 0, 0], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
    dy = [[], [0, 0, -1, 1], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]
    bi, bj = x[0], x[1]
    b = A[bi][bj]
    for i in range(len(dx[b])):
        if y[0] == bi + dx[b][i] and y[1] == bj + dy[b][i]:
            return True
    else:
        return False


def move(x):
    dx = [[], [-1, 1, 0, 0], [-1, 1], [0, 0], [-1, 0], [1, 0], [1, 0], [-1, 0]]
    dy = [[], [0, 0, -1, 1], [0, 0], [-1, 1], [0, 1], [0, 1], [0, -1], [0, -1]]

    qi, qj = x[0], x[1]
    q = A[qi][qj]
    for i in range(len(dx[q])):
        qi2 = qi + dx[q][i]
        qj2 = qj + dy[q][i]
        if 0 <= qi2 < N and 0 <= qj2 < M and A[qi2][qj2] != 0 and visit[qi2][qj2] == 0:
            if back([qi2, qj2], [qi, qj]) == True:
                stack.append([qi + dx[q][i], qj + dy[q][i]])

tn = int(input())
for ir in range(tn):
    N, M, R, C, L = map(int, input().split())
    A = [list(map(int, input().split())) for iii in range(N)]
    stack = [[R, C]]
    queue = []
    visit = [list(0 for i in range(M)) for ii in range(N)]
    T = 0
    cnt = 0
    while True:
        flag = 0
        if not stack and not queue:
            break
        if T == L and len(queue) == 0:
            break
        if not queue:
            queue += stack
            stack = []
            T += 1
        while queue:
            qv = queue.pop(-1)
            if visit[qv[0]][qv[1]] == 0:
                flag = 1
                v = qv
                break
        if flag == 1:
            cnt += 1
            visit[v[0]][v[1]] = 1
            move(v)
    print('#{} {}'.format(ir+1, cnt))