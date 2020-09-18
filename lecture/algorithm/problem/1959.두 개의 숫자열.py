tn = int(input())
for ir in range(tn):
    N = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = []
    if len(a) >= len (b):
        a, b = b, a
    resul = 0
    c = []
    d = []
    n = abs(N[0] - N[1]) + 1
    for i in range(n):
        f = b[i:i+len(a)]
        for _, __ in enumerate(a):
            c.append(__ * f[_])
        d.append(sum(c))
        c = []
    resul = max(d)
    print('#{} {}'.format(ir+1, resul))