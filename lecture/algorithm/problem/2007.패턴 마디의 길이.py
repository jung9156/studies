tn = int(input())
for ir in range(tn):
    a = input()
    n = 1
    while True:
        if a[0:0+n] != a[n:n+n]:
            n += 1
        else:
            break
    print('#{} {}'.format(ir+1, n))