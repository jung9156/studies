for ir in range(int(input())):
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    A = A[:L]
    for i in range(M):
        w, v = map(int, input().split())
        if w <= L:
            A.insert(w, v)

    print('#{} {}'.format(ir+1, A[L]))