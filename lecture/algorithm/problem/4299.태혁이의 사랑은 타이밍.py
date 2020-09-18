tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    D, H, M = map(int, input().split())
    a = 16511
    q = (((D * 24) + H) * 60 + M) - a
    if q < 0:
        print(-1)
    else:
        print(q)