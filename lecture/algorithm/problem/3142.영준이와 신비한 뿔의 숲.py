tn = int(input())
for ir in range(tn):
    n, m = list(map(int, input().split()))
    a = n - m
    b = m - a
    print('#{} {} {}'.format(ir+1, b, a))