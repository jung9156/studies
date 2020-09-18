for ir in range(int(input())):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))
    result = 0
    for i in range(N-1):
        wm = i
        for j in range(i, N):
            if W[wm] < W[j]:
                wm = j
        W[wm], W[i] = W[i], W[wm]

    for i in range(M-1):
        wm = i
        for j in range(i, M):
            if T[wm] < T[j]:
                wm = j
        T[wm], T[i] = T[i], T[wm]

    for i in T:
        for idx, j in enumerate(W):
            if i >= j:
                W.pop(idx)
                result += j
                break
    print('#{} {}'.format(ir+1, result))