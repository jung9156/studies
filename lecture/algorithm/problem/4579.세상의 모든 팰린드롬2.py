tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    B = list(input())
    c = []
    fl = 0

    if '*' not in B:
        if B != B[::-1]:
            print('Not exist')
            fl = 1
        else:
            print('Exist')
            fl = 1

    for i in range(len(B)):
        if B[i] == '*':
            c += B[:i]
            break

    if fl != 1:
        d = []
        for i in range(len(B)-1, -1, -1):
            if B[i] == '*':
                break
            d.append(B[i])

        if len(c) < len(d):
            c, d = d, c

        for i in range(len(d)):
            if d[i] != c[i]:
                print('Not exist')
                break
        else:
            print('Exist')
