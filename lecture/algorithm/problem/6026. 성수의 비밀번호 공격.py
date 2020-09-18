tn = int(input())
for ir in range(tn):
    M, N = map(int, input().split())
    qn = 0
    m1 = M
    re = 0
    pm = 1
    while True:
        if m1 == 0:
            break
        A = 1
        B = 1
        for i in range(m1):
            A *= M - i
            B *= (i+1)
        C = A // B
        re += (C * (m1 ** N)) * pm
        pm *= -1
        m1 -= 1
    re %= 1000000007
    print('#{} {}'.format(ir+1, re))