tn = int(input())
for ir in range(tn):
    N = int(input())
    s = 0
    for i in range(N):
        p , x = map(float, input().split())
        s += p * x
    print('#{} {}'.format(ir+1, s))