import copy

def move(A1):
    for i1 in range(W):
        downwall = []
        for i2 in range(H):
            if A1[i2][i1] != 0:
                downwall.append(A1[i2][i1])
                A1[i2][i1] = 0
        for ii1 in range(H-1, H-1-len(downwall), -1):
            A1[ii1][i1] = downwall.pop(-1)


def boom(x, A1, b_list, visit):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        bn = x[0]
        bi = dx[i]
        bj = dy[i]
        pi = x[1]
        pj = x[2]
        bn -= 1
        while bn != 0:
            bn -= 1
            if pi + bi < 0 or pi + bi >= H or pj + bj < 0 or pj + bj >= W:
                break
            else:
                pi += bi
                pj += bj
                if A1[pi][pj] > 1 and [pi, pj] not in b_list and visit[pi][pj] == 0:
                    b_list.append([A1[pi][pj], pi, pj])
                A1[pi][pj] = 0



def shoot(x, A1, H, W):#슛 하기 전에 밑에 남은 블록이 없으면 슛 X하는 코드 넣기.
    for i in x:
        n = 0
        b_list = []
        visit = []
        if A1[H-1][i] == 0:
            break
        for iii in range(H):
            visit.append(list(0 for i in range(W)))
        while A1[n][i] == 0:
            if n >= H - 1:
                break
            n += 1
        b_list.append([A1[n][i], n, i])
        A1[n][i] = 0

        while b_list:
            v = b_list.pop(-1)
            visit[v[1]][v[2]] = 1
            boom([v[0], v[1], v[2]], A1, b_list, visit)
        move(A1)
    q = 0
    for fi in range(H):
        q += A1[fi].count(0)
    return q


def goo(a, H, W, k, n):
    global result
    if result == 0:
        return
    if k == n:
        A1 = copy.deepcopy(A)
        num = shoot(a, A1, H, W)
        if result > (H * W) - num:
            result = (H * W) - num
        return
    else:
        for i in range(W):
            if A[H-1][i] != 0:
                a.append(i)
                goo(a, H, W, k + 1, n)
                a.pop(-1)


tn = int(input())
for ir in range(tn):
    N, W, H = map(int, input().split())
    A = [list(map(int, input().split())) for ii in range(H)]
    result = (H * W) + 1
    a = []
    goo(a, H, W, 0, N)

    print('#{} {}'.format(ir+1, result))