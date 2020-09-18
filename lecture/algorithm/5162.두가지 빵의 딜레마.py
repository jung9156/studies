tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    A, B, C = map(int, input().split())
    if A < B:
        print(C // A)
    else:
        print(C//B)