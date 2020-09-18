def check_Y(Y):
    global result
    if result > Y:
        result = Y


def check_M3(M3, k, n, s):
    global result
    if k >= 10:
        if 10 <= k <= 11:
            if sum(ppay[k:]) > M3:
                s += M3
            else:
                s += sum(ppay[k:])

        if result > s:
            result = s
        return

    for i1 in range(k, 10):
        if ppay[i1] != 0 and sum(ppay[i1:i1+3]) > M3:
            check_M3(M3, i1 + 3, n, s + M3)
        s += ppay[i1]

    if sum(ppay[10:]) > M3:
        s += M3
    else:
        s += sum(ppay[10:])
    if result > s:
        result = s



def check_M(plan, D, M1):
    global result
    for i in range(12):
        if plan[i] * D > M1:
            ppay.append(M1)
        else:
            ppay.append(D * plan[i])
    q = sum(ppay)
    if q > result:
        result = q



tn = int(input())
for ir in range(tn):
    D, M1, M3, Y = map(int, input().split())
    plan = list(map(int, input().split()))
    ppay = []
    result = 0
    check_M(plan, D, M1)
    check_M3(M3, 0, 11, 0)
    check_Y(Y)
    print('#{} {}'.format(ir+1,result))
