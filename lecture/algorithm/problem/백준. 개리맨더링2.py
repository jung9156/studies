def plus(x, y, d1, d2):
    global N
    result = [0, 0, 0, 0, 0]
    Q = []

    for i1 in range(d1 + 1):
        for i2 in range(d2 + 1):
            Q.append([x + i1, y - i1])
            Q.append([x + i2, y + i2])
            Q.append([x + i1 + i2, y - i1 + i2])
            Q.append([x + i1 + i2, y + i2 - i1])

    A_f = list(list(0 for _ in range(N)) for ___ in range(N))

    for q in Q:
        qi, qj = q
        A_f[qi][qj] = 5


    for i in range(N):
        if 5 not in A_f[i]:
            continue
        n1 = A_f[i].index(5)
        if 5 not in A_f[i]:
            continue
        for i10 in range(len(A_f[i]) - 1,  -1, -1):
            if A_f[i][i10] == 5:
                n2 = i10
                break
        for j in range(n1, n2 + 1):
            A_f[i][j] = 5


    for i in range(N):
        for j in range(N):
            if A_f[i][j] == 5:
                result[4] += A[i][j]
            elif 0 <= i < x + d1 and 0 <= j <= y:
                result[0] += A[i][j]
            elif 0 <= i <= x + d2 and y < j <= N - 1:
                result[1] += A[i][j]
            elif x + d1 <= i <= N - 1 and 0 <= j < y - d1 + d2:
                result[2] += A[i][j]
            elif x + d2 < i <= N - 1 and y - d1 + d2 <= j <= N - 1:
                result[3] += A[i][j]

    return max(result) - min(result)

def ga(x, y):
    global N, final
    d1, d2 = y, N - y - 1
    for dd1 in range(1, d1 + 1):
        for dd2 in range(1, d2 + 1):
            if x + dd1 + dd2 >= N:
                break
            re = plus(x, y, dd1, dd2)

            if final > re:
                final = re


A = []
N = int(input())
for ir in range(N):
    A.append(list(map(int, input().split())))
final = 40000
for i in range(N - 2):
    for j in range(1, N - 1):
        ga(i, j)
print(final)