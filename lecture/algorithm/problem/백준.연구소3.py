import copy
from itertools import combinations



def vir_c(A, N):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 0:
                return False
    else:
        return True


def test(x, y, A_copy):
    dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for d in dd:
        x1, y1 = x + d[0], y + d[1]
        if 0 <= x1 < N and 0 <= y1 < N:
            if A_copy[x1][y1] == 0:
                return True
    else:
        return False


N, M = map(int, input().split())
A = list(list(map(int, input().split())) for i in range(N))
dir = []
visit = list(list(0 for i in range(N)) for ii in range(N))
for i in range(N):
    for j in range(N):
        if A[i][j] == 2:
            dir.append([i, j])
dd = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 20000000
for i in combinations(dir, M):
    re = 0
    queue = list(i)
    stack = []
    A_copy = copy.deepcopy(A)
    v_copy = copy.deepcopy(visit)
    while True:
        if not stack and not queue:
            if vir_c(A_copy, N) == True:
                if re < result:
                    result = re
            break
        if not stack:
            stack = queue
            queue = []
            re += 1
            if re > result:
                break
        s1 = stack.pop(-1)
        for d in dd:
            vx, vy = s1[0] + d[0], s1[1] + d[1]
            if 0 <= vx < N and 0 <= vy < N and v_copy[vx][vy] == 0:
                if A_copy[vx][vy] == 0:
                    v_copy[vx][vy] = 1
                    A_copy[vx][vy] = 3
                    queue.append([vx, vy])
                elif A_copy[vx][vy] == 2:
                    if test(vx, vy, A_copy) == True:
                        v_copy[vx][vy] = 1
                        A_copy[vx][vy] = 3
                        queue.append([vx, vy])
if result == 20000000:
    print(-1)
else:
    print(result-1)