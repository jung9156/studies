def checkcan(x, y):
    for i in range(4, -1, -1):
        flag = 0
        for i1 in range(i, -1, -1):
            if x + i1 >= 10:
                break
            for j in range(i, -1, -1):
                if y + j >= 10:
                    flag = 1
                    break
                if AA[x + i1][y + j] == 0:
                    flag = 1
                    break
            if flag == 1:
                break
        else:
            return i+1


def whereisone():
    for i in range(10):
        for j in range(10):
            if AA[i][j] == 1:
                return [i, j]


def ch_s(cnt, fu):
    global result, visit
    if cnt > result:
        return
    if fu == 0:
        result = min(result, cnt)

    if fu > 0:
        X = whereisone()
        x0, x1 = X[0], X[1]
        sz = checkcan(x0, x1)
        for s in range(sz, 0, -1):
            if S3[s-1] == 0:
                continue
            S3[s-1] -= 1
            for u1 in range(x0, x0+s):
                for u2 in range(x1, x1+s):
                    AA[u1][u2] = 0
            ch_s(cnt+1, fu - s*s)
            for u3 in range(x0, x0+s):
                for u4 in range(x1, x1+s):
                    AA[u3][u4] = 1
            S3[s-1] += 1


AA = [list(map(int, input().split())) for ii in range(10)]
S3 = [5, 5, 5, 5, 5]
result = 30

visit = [list(0 for i in range(10)) for i1 in range(10)]
fu = 0
for i in range(10):
    for j in range(10):
        if AA[i][j] == 1:
            fu += 1



if fu != 0:
    ch_s(0, fu)
    if result == 30:
        print(-1)
    else:
        print(result)
else:
    print(0)