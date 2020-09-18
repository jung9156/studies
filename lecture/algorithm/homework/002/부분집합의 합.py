a = list(range(1, 13))

te_c = int(input())
for ir in range(te_c):
    t = list(map(int, input().split()))


    result = []
    n, k = t[0], t[1]
    for i in range(1, 1<<12):
        ke = []
        for j in range(13):
            if i & (1<<j):
                ke.append(a[j])
        if len(ke) == n and sum(ke) == k:
            result.append(ke)

    print('#{} {}'.format(ir+1,len(result)))