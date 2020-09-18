tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    L, U, X = map(int, input().split())
    if X < L:
        print(L - X)
    else:
        if X > U:
            print(-1)
        else:
            print(0)