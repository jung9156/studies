tn = int(input())
for ir in range(tn):
    N = int(input())
    go = [0 for i in range(200)]
    for i3 in range(N):
        A1, A2 = map(int, input().split())

        if A1 % 2 == 1:
            A1 = A1 // 2
        else:
            A1 = (A1 // 2) - 1

        if A2 % 2 == 1:
            A2 = A2 // 2
        else:
            A2 = (A2 // 2) -1
        if A1 > A2:
            A1 , A2 = A2, A1
        for i4 in range(A1, A2 + 1):
            go[i4] += 1

    print('#{} {}'.format(ir+1, max(go)))