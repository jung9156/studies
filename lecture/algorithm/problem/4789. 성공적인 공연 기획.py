tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    A = list(input())
    pn = 0
    rn = 0
    for idx, i1 in enumerate(A):
        if pn >= idx:
            pn += int(i1)
        else:
            while pn < idx:
                pn += 1
                rn += 1
            pn += int(i1)
    print(rn)