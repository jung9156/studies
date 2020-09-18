def change(q, i1, j1):
    for i in q:
        x, y = i[0], i[1]
        NB[i1 + x][j1 + y] = 1


def check(q, i1, j1):
    global N, M
    for i in q:
        x, y = i[0], i[1]
        if i1 + x >= N or j1 + y >= M or NB[i1 + x][j1 + y] == 1:
            return False


def turn(S, r, c):
    global R, C
    S2 = []
    for j in range(c):
        s = []
        for i in range(r-1, -1, -1):
            s.append(S[i][j])
        S2.append(s)
    R, C = C, R
    return S2


def sti(S, r, c):
    st_list = []
    for i in range(r):
        for j in range(c):
            if S[i][j] == 1:
                st_list.append([i, j])
    return st_list


N, M, K = map(int, input().split())
NB = [list(0 for i in range(M)) for i1 in range(N)]
result = 0
for i in range(K):
    R, C = map(int, input().split())
    S = [list(map(int, input().split())) for i1 in range(R)]
    turn_num = 0
    while True:
        if turn_num == 4:
            break
        q = sti(S, R, C)
        flag = 0
        for i1 in range(N):
            for j1 in range(M):
                if check(q, i1, j1) != False:

                    flag = 1
                    change(q, i1, j1)
                    result += len(q)
                    break
            if flag == 1:
                break
        if flag == 0:
            S = turn(S, R, C)
            turn_num += 1
        else:
            break
print(result)
