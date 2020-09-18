for ir in range(int(input())):
    N, M = map(int, input().split())
    A = list([] for i in range(N + 1))
    result = []
    for i in range(M):
        a, b = map(int, input().split())
        A[b].append(a)
        A[a].append(b)

    stack = A[1]
    for i in stack:
        result += [i]
        result += A[i]
    re = []
    for i in result:
        if i != 1 and i not in re:
            re.append(i)

    print('#{} {}'.format(ir+1, len(re)))