tn = int(input())
for ir in range(tn):
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    t = 0
    bd = {}
    for i1 in a:
        if i1 not in bd.keys():
            bd[i1] = 1
        else:
            bd[i1] += 1
    print('#{} '.format(ir+1),end='')
    b = 0
    qq = 0
    tt = 0
    for i2 in range(len(bd)):
        t += min(bd.keys()) - tt
        tt = min(bd.keys())
        b += (t // m) * k
        t = t % m
        b -= bd[min(bd.keys())]
        if b < 0:
            qq = 1
            print('Impossible')
            break

        del bd[min(bd.keys())]

    if qq == 0:
        print('Possible')