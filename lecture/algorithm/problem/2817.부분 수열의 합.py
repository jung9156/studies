tn = int(input())
for ir in range(tn):
    N, K = list(map(int, input().split()))
    a = list(map(int, input().split()))
    cou = 0
    a.sort()
    for idx, i7 in enumerate(a):
        if i7 > K:
            del a[idx]
    for i1 in range(1, 1 << len(a)):
        sum = 0
        for j1 in range(len(a)):
            if i1 & (1 << j1):
                sum += a[j1]

        if sum == K:
            cou += 1

    print('#{} {}'.format(ir+1, cou))