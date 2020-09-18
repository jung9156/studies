def cross(i, j, N):
    dir = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
    flag = 0
    for dd in dir:
        x1, y1 = i, j
        while True:
            x1 += dd[0]
            y1 += dd[1]
            if x1 < 0 or x1 >= N or y1 < 0 or y1 >= N:
                break
            elif A[x1][y1] == 2:
                flag = 1
                break
        if flag == 1:
            return False
    return True

def check(k, Y, N, A):
    global result
    if k == N:
        result += 1
        return

    for i in range(N):
        if Y[i] != 1 and cross(k, i, N) == True:
            Y[i] = 1
            A[k][i] = 2
            check(k+1, Y, N, A)
            A[k][i] = 0
            Y[i] = 0

tn = int(input())
for ir in range(tn):
    N = int(input())
    A = [list(0 for i in range(N)) for i1 in range(N)]
    Y = [0 for i in range(N)]
    result = 0
    check(0, Y, N, A)
    print('#{} {}'.format(ir+1, result))