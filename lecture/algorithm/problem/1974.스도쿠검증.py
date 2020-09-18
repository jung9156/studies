test_num = int(input())
for ir in range(test_num):
    a = [list(map(int, input().split())) for i in range(9)]
    key = {}
    check = []
    check2 = []
    check3 = []
    result = []
    for i in range(9):
        ro = []
        co = []
        for j in range(9):
            ro.append(a[i][j])
            co.append(a[j][i])
        check.append(ro)
        check2.append(co)
    cross = [-1, 0, 1]
    for i3 in range(1, 8, 3):
        for i4 in range(1, 8, 3):
            cr = []
            for i in cross:
                for j in cross:
                    cr.append(a[i3+i][i4+j])
            check3.append(cr)

    for i in check:
        if len(set(i)) != 9:
            result.append(1)
    for ii in check2:
        if len(set(ii)) != 9:
            result.append(1)
    for iii in check3:
        if len(set(iii)) != 9:
            result.append(1)
    print('#{} '.format(ir+1), end='')
    if len(result) == 0:
        print(1)
    else:
        print(0)