for ir in range(int(input())):
    bd = [list(input().split()) for i_i in range(5)]
    mali = []
    for ma in range(5):
        mali.append(len(*bd[ma]))
    n = max(mali)
    k = []

    for i in range(5):
        k.append(list('#' for i in range(n)))
    for i in range(5):

        for j in range(mali[i]):
            k[i][j] = bd[i][0][j]
    print('#{} '.format(ir+1),end='')

    for i2 in range(n):
        for j2 in range(5):
            if k[j2][i2] != '#':
                print(k[j2][i2],end='')
    print()
