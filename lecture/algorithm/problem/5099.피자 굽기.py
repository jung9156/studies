for tn in range(int(input())):
    print('#{} '.format(tn+1),end='')
    N, M = map(int, input().split())
    C = [0]
    C += list(map(int, input().split()))
    A = [0 for i in range(N)]
    ch = -1
    Cn = 1
    while True:
        C[A[ch]] //= 2
        if C.count(0) == M:
            break
        ch = (ch + 1) % N
        if C[A[ch]] == 0:
            if C[Cn] != 0:
                A[ch] = Cn
                Cn += 1
                if Cn > M:
                    Cn = 0
            else:
                A[ch] = 0
    for i in range(M+1):
        if C[i] != 0:
            print(i)