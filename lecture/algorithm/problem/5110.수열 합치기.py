for ir in range(int(input())):
    N, M = map(int, input().split())
    A = []
    re = list(map(int, input().split()))
    for i in range(M-1):
        B = list(map(int, input().split()))
        for idx, r in enumerate(re):
            if r > B[0]:
                re[idx:0] = B
                break
        else:
            re += B
    print('#{} '.format(ir + 1), end='')
    print(*re[-1:-11:-1])
