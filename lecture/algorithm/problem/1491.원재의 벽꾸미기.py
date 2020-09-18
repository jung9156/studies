tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N, A, B = list(map(int, input().split()))
    n = 0
    num = []
    while True:
        n += 1
        if n*n >= N:
            if n*n != N:
                n -= 1
            break
    num.append([n, n])
    R = n+1
    while True:
        R -= 1
        C = N // R
        num.append([R, C])
        if N % R == 0:
            break
    result = 99999999
    for i1 in num:
        k = A*(abs(i1[0] - i1[1])) + B*(N-(i1[0]*i1[1]))
        if result > k:
            result = k
    print(result)