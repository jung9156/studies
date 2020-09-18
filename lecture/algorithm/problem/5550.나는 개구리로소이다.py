tn = int(input())
for ir in range(tn):
    a = list(input())
    mm = 0
    End = 0
    frog = []
    cr = ['c', 'r', 'o', 'a', 'k']
    print('#{} '.format(ir + 1),end='')
    while True:
        for i3 in frog:
            if len(i3) == 5:
                i3.clear()
        if len(a) == 0:
            for i4 in frog:
                if len(i4) != 0:
                    End = 1
                    print(-1)
                    break
            break
        check = a.pop(0)
        if check == 'c':
            for i1 in frog:
                if len(i1) == 0:
                    i1.append('c')
                    break
            else:
                frog.append(['c'])
        else:
            check2 = cr[cr.index(check) -1]
            for i2 in frog:
                if check not in i2:
                    if check2 in i2:
                        i2.append(check)
                        break
            else:
                End = 1
                print(-1)
                break


    if End == 0:
        print('{}'.format(len(frog)))