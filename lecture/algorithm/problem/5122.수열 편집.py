for ir in range(int(input())):
    N, M, L = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(M):
        order = list(input().split())
        if len(order) == 2:
            A.pop(int(order[1]))
        else:
            o, v, w = order[0], int(order[1]), int(order[2])
            if o == 'I':
                A.insert(v, w)
            elif o == 'C':
                A[v] = w
    if len(A) < L:
        re = -1
    else:
        re = A[L]
    print('#{} {}'.format(ir+1, re))