def back(A, k, N, time, result):
    global re
    if k == N:
        if result > re:
            re = result
        return

    q1, q2 = A[k][0], A[k][1]
    for t1 in range(q1, q2):
        if time[t1] != 0:
            back(A, k + 1, N, time, result)
            break
    else:
        for t2 in range(q1, q2):
            time[t2] = 1
        back(A, k + 1, N, time, result + 1)
        for t2 in range(q1, q2):
            time[t2] = 0
        back(A, k + 1, N, time, result)

for ir in range(int(input())):
    N = int(input())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    for i in range(N-1):
        am = i
        for j in range(i, N):
            if A[am][0] >A[j][0]:
                am = j
        A[i], A[am] = A[am], A[i]
    time = list(0 for i in range(25))
    re = 0
    back(A, 0, N, time, 0)
    print('#{} {}'.format(ir+1, re))