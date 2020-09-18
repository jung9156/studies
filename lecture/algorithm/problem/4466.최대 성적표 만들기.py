tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    s = 0
    for i in range(K):
        s += A.pop(A.index(max(A)))

    print(s)