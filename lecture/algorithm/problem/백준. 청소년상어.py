import copy


dir = [[-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1]]


def shark(si, sj, s_re, s_d, Afake):#물고기 움직이고 상어 이동 가능 경우 찾고 백트래킹
    global result
    if s_re > result:
        result = s_re
    si2, sj2 = si, sj

    s_d = s_d % 8
    Afake = move(Afake)

    shark_load = []
    dx, dy = dir[s_d]
    while True:
        if si2 < 0 or si2 > 3 or sj2 < 0 or sj2 > 3:
            break
        si2, sj2 = si2 + dx, sj2 + dy
        if 0 <= si2 <= 3 and 0 <= sj2 <= 3 and 1 <= Afake[si2][sj2][0] <= 16:
            shark_load.append([si2, sj2])

    for sl in shark_load:
        Afake[si][sj][0] = 0
        AA = copy.deepcopy(Afake)
        x, y = sl
        fish = AA[x][y][0]
        AA[x][y][0] = 100
        shark(x, y, s_re + fish, AA[x][y][1], AA)
        Afake[si][sj][0] = 100



def is_wall(fi, fj, d_n, Afake):#물고기 방향 정하고 이동하기
    d_n = d_n % 8
    cnt = 0
    while True:
        if cnt >= 8:
            return
        di, dj = dir[d_n]
        ni, nj = fi + di, fj + dj
        if 0 <= ni <= 3 and 0 <= nj <= 3:
            if Afake[ni][nj][0] <= 16:
                Afake[fi][fj][1] = d_n
                Afake[fi][fj], Afake[ni][nj] = Afake[ni][nj], Afake[fi][fj]
                return
        d_n = (d_n + 1) % 8
        cnt += 1

def move(Afake):#물고기 번호 찾기 1~ 16
    k = 1
    while k <= 16:
        flag = 0
        for i in range(4):
            for j in range(4):
                if Afake[i][j][0] == k:
                    d_n = Afake[i][j][1]
                    is_wall(i, j, d_n, Afake)
                    flag = 1
                    break
            if flag == 1:
                break
        k += 1
    return Afake


A = []
for i in range(4):
    aa = []
    a = list(map(int, input().split()))
    for i1 in range(0, 8, 2):
        aa.append([a[i1], a[i1+1]])
    A.append(aa)
result = 0

s_re = 0
s_d = A[0][0][1]
s_re += A[0][0][0]
A[0][0][0] = 100
shark(0, 0, s_re, s_d, A)

print(result)