test_num = int(input())
result = []
for i in range(test_num):
    test_case = int(input())

    l = 0
    v = 0
    a = 0
    pm = 0

    for i in range(test_case):

        pma = list(map(int, input().split()))
        if len(pma) == 1:
            l += v
            pm = 0
        else:
            pm = pma[0]
            a = pma[1]

            if pm == 1:
                l += v + a
                v += a
            else:
                if a > v:
                    v = 0
                else:
                    v -= a
                    l += v
    result.append(l)
for i in range(test_num):
    print('#{} {}'.format(i+1, result[i]))