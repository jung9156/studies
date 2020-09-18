tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N = int(input())
    a = list(input().split())
    en = 0
    if N % 2 == 0:
        i = 0
        j = N // 2
    else:
        i = 0
        j = N - (N // 2)
    while True:
        print(a[i],end=' ')
        i += 1
        en += 1
        if en == N:
            break
        print(a[j],end=' ')
        j += 1
        en += 1
        if en == N:
            break
    print()