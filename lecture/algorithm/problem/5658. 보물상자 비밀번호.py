tn = int(input())
for ir in range(tn):
    N, K = map(int, input().split())
    A = list(input())
    A = A + A[:(N//4)-1]
    key = set()
    for i in range(N//4):
        q = ''
        n = 0
        for i1 in range(N):
            n += 1
            q += A[i+i1]
            if n == (N//4):
                n = 0
                key.add(int(q, base=16))
                q = ''

    wo = sorted(key,reverse=True)
    print('#{} {}'.format(ir+1, wo[K-1]))