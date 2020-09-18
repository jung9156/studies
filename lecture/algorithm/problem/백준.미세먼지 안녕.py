def push(y1, y2):
    global R, C
    pi1, pj1 = y1[0], y1[1]
    pi2, pj2 = y2[0], y2[1]
    #공기청정기1, 2의 방향
    dx1 = [-1, 0, 1, 0]
    dy1 = [0, 1, 0, -1]
    dx2 = [1, 0, -1, 0]
    dy2 = [0, 1, 0, -1]
    # 방향 바꾸는 기준
    jgx1 = [0, -2, y1[0], -2]
    jgy1 = [-2, C-1, -2, 0]
    jgx2 = [R-1, -2, y2[0], -2]

    dn = 0
    while True:
        pi1 += dx1[dn]
        pj1 += dy1[dn]
        if pi1 == jgx1[dn] or pj1 == jgy1[dn]:
            dn += 1
            if dn == 4:
                break
            A[pi1][pj1] = A[pi1 + dx1[dn]][pj1 + dy1[dn]]

        else:
            A[pi1][pj1] = A[pi1 + dx1[dn]][pj1 + dy1[dn]]

    A[y1[0]][y1[1]] = -1        #공기 청정기
    A[y1[0]][y1[1] + 1] = 0     #공기 청정기 옆


    dn2 = 0
    while True:
        pi2 += dx2[dn2]
        pj2 += dy2[dn2]
        if pi2 == jgx2[dn2] or pj2 == jgy1[dn2]:
            dn2 += 1
            if dn2 == 4:
                break
            A[pi2][pj2] = A[pi2 + dx2[dn2]][pj2 + dy2[dn2]]
        else:
            A[pi2][pj2] = A[pi2 + dx2[dn2]][pj2 + dy2[dn2]]
    A[y2[0]][y2[1]] = -1        #공기 청정기
    A[y2[0]][y2[1] + 1] = 0     #공기 청정기 옆


def spread(x):
    ms = x[2] // 5
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    mcn = 0
    for i in range(4):
        if x[0] + dx[i] >= 0 and x[0] + dx[i] < R and x[1] + dy[i] >= 0 and x[1] + dy[i] < C:
            if A[x[0] + dx[i]][x[1] + dy[i]] != -1:
                A[x[0] + dx[i]][x[1] + dy[i]] += ms
                mcn += 1
    A[x[0]][x[1]] += (x[2] - (ms * mcn))


R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for ii in range(R)]
fr = []
mm = []
for i1 in range(R):
    for j1 in range(C):
        if A[i1][j1] == -1:
            fr.append([i1, j1])

for i5 in range(T):
    for i1 in range(R):
        for j1 in range(C):
            if A[i1][j1] != 0 and A[i1][j1] != -1:
                mm.append([i1, j1, A[i1][j1]])
                A[i1][j1] = 0

    for i2 in range(len(mm)):
        spread(mm[i2])
    if fr[0][0] > fr[1][0]:
        fr[0], fr[1] = fr[1], fr[0]
    push(fr[0], fr[1])
    mm.clear()

result = 0

for i in range(R):
    for j in range(C):
        if A[i][j] != -1:
            result += A[i][j]
print(result)
