def root(x):
    if not A[x]:
        if (x * 2) + 1 <= N:
            q1 = root(x * 2)
            q2 = root((x * 2) + 1)
            A[x].append(q1 + q2)
        else:
            A[x].append(A[x * 2][0])
        return A[x][0]
    else:
        return A[x][0]

for ir in range(int(input())):
    N, M, L = map(int, input().split())
    A = [[] for i in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        A[a].append(b)

    root(L)
    print('#{} {}'.format(ir+1, *A[L]))