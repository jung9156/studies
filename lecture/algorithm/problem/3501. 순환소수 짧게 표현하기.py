result = []
tn = int(input())
for ir in range(tn):
    p, q = map(int, input().split())
    A1 = []
    ch = [-1 for i in range(q)]
    qq = -1
    re = '0'
    A = []
    n = 0
    if p >= q:
        A = p // q
        p %= q
        re = '{}'.format(A)

    while p != 0:
        if ch[p] == -1:
            ch[p] = n
            n += 1
        else:
            qq = ch[p]
            break
        p *= 10
        A1.append(p // q)
        p %= q

    if A1 != []:
        if qq != -1:
            re += '.' + ''.join(map(str, A1[:qq])) + '(' + ''.join(map(str, A1[qq:])) + ')'
        else:
            re += '.' + ''.join(map(str, A1))
    # print('#{} {}'.format(ir+1, re))
    result.append(re)
for iir in range(tn):
    print('#{} {}'.format(iir+1, result[iir]))
