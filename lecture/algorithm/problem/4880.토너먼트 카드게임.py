def div(x):
    xn = len(x)
    a = []
    b = []
    if xn > 2:
        if xn % 2 == 0:
            a = x[: xn // 2]
            b = x[xn // 2 :]
        else:
            a = x[: xn//2+1]
            b = x[xn//2+1:]
        a = div(a)
        b = div(b)
    else:
        return rcp(x)
    q = [a, b]
    return rcp(q)


def rcp(i):
    rcp2 = 0
    if len(i) == 1:
        rcp2 = i[0]
    else:
        if Ad[i[0]] == Ad[i[1]]:
            rcp2 = i[0]
        elif Ad[i[0]] == 1:
            if Ad[i[1]] == 2:
                rcp2 = i[1]
            else:
                rcp2 = i[0]
        elif Ad[i[0]] == 2:
            if Ad[i[1]] == 1:
                rcp2 = i[0]
            else:
                rcp2 = i[1]
        else:
            if Ad[i[1]] == 1:
                rcp2 = i[1]
            else:
                rcp2 = i[0]
    return rcp2

tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N = int(input())
    A = list(map(int, input().split()))
    Ad = {}
    for idx, val in enumerate(A):
        Ad[idx+1] = val
    B = list(range(1, N+1))
    moodae = []
    print(div(B))