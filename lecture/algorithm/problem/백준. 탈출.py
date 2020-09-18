def move_mul(mul):
    dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    change_mul = []
    for m in mul:
        i, j = m[0], m[1]
        for dd in dir:
            x = i + dd[0]
            y = j + dd[1]
            if 0 <= x < R and 0 <= y < C and (A[x][y] == '.' or A[x][y] == 'S'):
                if [x, y] not in change_mul:
                    change_mul.append([x, y])
    for c1 in change_mul:
        A[c1[0]][c1[1]] = '*'
    return change_mul


def move_dochi(dochi):
    dir = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    change_dochi = []
    for do in dochi:
        i, j = do[0], do[1]
        visit[i][j] = 1
        for dd in dir:
            x = i + dd[0]
            y = j + dd[1]
            if 0 <= x < R and 0 <= y < C and A[x][y] == '.' and visit[x][y] == 0:
                if [x, y] not in change_dochi:
                    change_dochi.append([x, y])
            elif 0 <= x < R and 0 <= y < C and A[x][y] == 'D':
                return -1
    return change_dochi


def start(dochi, mul, time):
    while True:
        time += 1
        mul = move_mul(mul)
        dochi = move_dochi(dochi)
        if dochi == -1:
            return time
        elif not dochi:
            return 'KAKTUS'


R, C = map(int, input().split())
A = [list(input()) for i in range(R)]
dochi = []
mul = []
biber = []
dol = []
time = 0
visit = [[0 for i in range(C)] for i1 in range(R)]
for i in range(R):
    for j in range(C):
        if A[i][j] == 'S':
            dochi.append([i, j])
        elif A[i][j] == '*':
            mul.append([i, j])
print(start(dochi, mul, 0))