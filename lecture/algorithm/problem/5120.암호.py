for ir in range(int(input())):
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    n = 0
    for i in range(K):
        N = len(A)
        n = n + M
        if n < N:
            A[n:0] = [A[n] + A[n-1]]
        elif n == N:
            A.extend([A[0] + A[-1]])
        else:
            n %= N
            A[n:0] = [A[n] + A[n - 1]]

    k = len(A) - 1
    print('#{} '.format(ir+1), end='')
    print(*A[-1:-11:-1])