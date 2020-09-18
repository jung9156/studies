tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    a = list(map(int, input()))
    check = 0
    cou = 0
    for i1 in a:
        if i1 != check:
            check = i1
            cou += 1

    print(cou)
