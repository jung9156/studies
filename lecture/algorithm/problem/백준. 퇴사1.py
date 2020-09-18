def back(re, k, N):
    global result
    if k == N:
        if A[k][0] == 1:
            re += A[k][1]
        if result < re:
            result = re
        return
    elif k > N:
        if result < re:
            result = re
        return
    elif k < N:
        if k + A[k][0] == N + 1:
            re += A[k][1]
            if result < re:
                result = re
            re -= A[k][1]
        elif k + A[k][0] <= N:
            re += A[k][1]
            back(re, k + A[k][0], N)
            re -= A[k][1]
        elif k + A[k][0] > N + 1:
            back(re, k + 1, N)
        back(re, k + 1, N)


N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
A.insert(0, [0, 0])
result = 0
back(0, 1, N)
print(result)