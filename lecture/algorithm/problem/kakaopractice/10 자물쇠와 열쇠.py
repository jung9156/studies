def solution(key, lock):
    answer = False
    N = len(lock)
    M = len(key)
    qqq = 0
    for i10 in range(N):
        for i11 in range(N):
            if lock[i10][i11] == 0:
                qqq = 1
                break
        if qqq == 1:
            break
    else:
        answer = True
        return answer

    def check(A, N, M):
        for i7 in range(0, M + (2 * (N - 1) - (N - 1))):
            for j7 in range(0, M + (2 * (N - 1) - (N - 1))):
                for i8 in range(N):
                    flag = 0
                    for i9 in range(N):
                        if A[i8 + i7][i9 + j7] == lock[i8][i9]:
                            flag = 1
                            break
                    if flag == 1:
                        break
                else:
                    return True
        return False
    def turn(A, N, M):
        B = []
        for t1 in range(M + (2 * (N - 1))):
            b = []
            for t2 in range(M + (2 * (N - 1)) - 1, -1, -1):
                b.append(A[t2][t1])
            B.append(b)
        return B


    Q = []
    for i4 in range(M):
        for i5 in range(M):
            Q.append(key[i4][i5])
    A = list([0] * (M + (2 * (N - 1))) for i in range((M + (2 * (N - 1)))))
    for i1 in range(N - 1, N - 1 + M):
        for i2 in range(N - 1, N - 1 + M):
            A[i1][i2] = Q.pop(0)

    answer = check(A, N, M)
    if answer == True:
        return answer
    for i in range(3):
        A = turn(A, N, M)
        answer = check(A, N, M)
        if answer == True:
            return answer

    return answer