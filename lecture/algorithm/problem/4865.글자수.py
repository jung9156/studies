tn = int(input())
for ir in range(tn):
    a = list(input())
    b = list(input())
    ad = {}

    for i1 in a:
        ad[i1] = 0

    for i2 in b:
        if i2 in a:
            ad[i2] += 1


    print('#{} {}'.format(ir+1, max(ad.values())))
