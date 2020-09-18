tn = int(input())
for ir in range(tn):
    n = int(input())
    n = n // 10
    rn = n // 2
    result = 0
    for i1 in range(1, 1+rn):
        k = (n - (i1*2)) + i1
        t = i1
        re = 1
        while True:
            if t== 0:
                re *= (2**i1)
                result += re
                break
            re *= k / t
            k -= 1
            t -= 1
    print('#{} {}'.format(ir+1, int(result+1)))
