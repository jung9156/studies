def cou(A):
    global N, M
    cnt = 0
    for i in range(N):
        for j in range(M):
            if A[i][j] == 0:
                cnt += 1
    return cnt

def CCTV(k, n1):
    global N, M, result
    if k == n1:
        ccc = cou(A)
        if result > ccc:
            result = ccc
        return

    d = [0, 4, 2, 4, 4, 1]
    di = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    dir = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]], [[0, 1], [1, 2], [2, 3], [3, 0]], [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]], [[0, 1, 2, 3]]]
    x, y = C[k][0], C[k][1]
    n = A[x][y]
    for i in range(d[n]):
        re = []
        for i2 in dir[n][i]:
            x, y = C[k][0], C[k][1]
            while True:
                x += di[i2][0]
                y += di[i2][1]
                if x < 0 or x >= N or y < 0 or y >= M:
                    break
                if A[x][y] == 0:
                    A[x][y] = 8
                    re.append([x, y])
                elif A[x][y] == 6:
                    break
        CCTV(k + 1, n1)
        for r in re:
            A[r[0]][r[1]] = 0




N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
CTV = [1, 2, 3, 4, 5]
C = []
result = N * M
for i in range(N):
    for j in range(M):
        if A[i][j] in CTV:
            C.append([i, j])

cn = len(C)
CCTV(0, cn)
print(result)