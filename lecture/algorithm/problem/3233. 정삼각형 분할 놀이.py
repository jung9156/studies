tn = int(input())
for ir in range(tn):
    A, B = list(map(int, input().split()))
    n = (A // B)
    c = []
    k = 1
    while True:
        c.append(k)
        if len(c) == n:
            break
        k += 2
    cc = sum(c)
    print('#{} {}'.format(ir+1, cc))