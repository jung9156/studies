tn = int(input())
for ir in range(tn):
    a = list(map(int, input().split()))
    h = a[0] + a[2]
    m = a[1] + a[3]
    h = (h % 12) + (m // 60)
    m = m % 60
    print('#{} {} {}'.format(ir+1, h, m))