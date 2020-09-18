def check(A, i1, i2):
    global N, M
    dx = [-2, 0, 2, 0]
    dy = [0, -2, 0, 2]
    for i in range(4):
        if 0 <= i1 + dx[i] < M and 0 <= i2 + dy[i] < N:
            if A[i1 + dx[i]][i2 + dy[i]] != 0:
                return False
    else:
        return True

tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N, M = map(int, input().split())
    A = [list(0 for ii in range(N)) for iii in range(M)]
    for i1 in range(M):
        for i2 in range(N):
            if check(A, i1, i2) == True:
                A[i1][i2] = 1
    re = 0
    for i in range(len(A)):
        re += A[i].count(1)
    print(re)