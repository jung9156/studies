for ir in range(int(input())):
    E, N = map(int, input().split())
    re = [[] for i in range(E + 2)]
    A = list(map(int, input().split()))
    for i in range(E):
        t1, t2 = A[i * 2], A[(i * 2) + 1]
        re[t1].append(t2)
    stack = [N]
    result = []
    while stack:
        v = stack.pop()
        result.append(v)
        stack.extend(re[v])
    print('#{} {}'.format(ir+1, len(result)))