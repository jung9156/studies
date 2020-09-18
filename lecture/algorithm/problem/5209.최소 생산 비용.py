def back(a, A, k, N, re):
    global result
    if re > result:
        return
    if k == N:
        if re < result:
            result = re
        return
    for p in range(N):
        if p not in a:
            a[k] = p
            back(a, A, k+1, N, re + A[k][p])
            a[k] = -1

for ir in range(int(input())):
    N = int(input())
    A = list(list(map(int, input().split())) for i in range(N))
    result = 100 * N
    a = list(-1 for i in range(N))
    back(a, A, 0, N, 0)
    print('#{} {}'.format(ir + 1, result))
