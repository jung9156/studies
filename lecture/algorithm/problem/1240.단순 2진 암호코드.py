tn = int(input())
for ir in range(tn):
    numl = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]
    alist = []
    b = ''
    print('#{} '.format(ir+1), end='')
    for il in range(n):
        if len(str(a[il])) != 3:
            b = str(a[il])[1:57]
            while True:
                if b[-1] == '1':
                    break
                if b[-1] == '0':
                    b = '0' + b
                    b = b[:56]

            break
    a = []
    an = []
    for i2 in range(8):
        a.append(b[7*i2:7*(i2+1)])
        an.append(int(numl.index(a[i2])))
    check = 0
    result = 0
    for idx, i5 in enumerate(an):
        result += i5
        if idx % 2 == 0:
            check += i5 * 3
        else:
            check += i5
    if check % 10 == 0:
        print(result)
    else:
        print(0)