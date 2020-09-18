for ir in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A)
    re = 0
    C = []
    for i1 in B:
        if i1 in A:
            C.append(i1)
    l, r = 0, N - 1
    for i in C:
        l, r = 0, N - 1
        k = (l + r) // 2
        stack = 'o'
        while True:
            k = (l + r) // 2
            if i == A[k]:
                re += 1
                break
            if i > A[k]:
                l = k + 1
                if stack == 'm':
                    break
                stack = 'm'
            else:
                r = k - 1
                if stack == 'l':
                    break
                stack = 'l'
    print('#{} {}'.format(ir+1, re))