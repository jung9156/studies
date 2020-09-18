tn = int(input())
result = []
for ir in range(tn):
    D, A, B, F = map(int, input().split())
    Af = A + F
    Bf = B + F
    Ft = 0
    train = [Af, Bf]
    tr2 = A + B
    n = 0
    while True:
        if -0.0000006 <= D <= 0.0000006:
            break
        n %= 2
        t = D / train[n]
        Ft += t
        D -= t * tr2
        n += 1
    result.append(Ft*F)



for ir in range(tn):
    print('#{} {}'.format(ir+1, result[ir]))