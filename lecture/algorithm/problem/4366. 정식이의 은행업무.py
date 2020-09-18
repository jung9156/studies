tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    n_2 = list(input())
    n_3 = list(input())

    result = []
    for i1 in range(1, len(n_2)):
        k = ''
        for i2 in range(len(n_2)):
            if i2 != i1:
                k += n_2[i2]
            else:
                if n_2[i2] == '0':
                    k += '1'
                else:
                    k += '0'
        result.append(int(k,base=2))
    three = ['0', '1', '2']
    three2 = ['1', '2']
    flag = 0

    for ii1 in range(1, len(n_3)):
        nn_3 = list(n_3)
        for ii2 in range(3):
            k = ''
            if nn_3[ii1] != three[ii2]:
                nn_3[ii1] = str(three[ii2])
            if int(k.join(nn_3), base=3) in result:
                print(int(k.join(nn_3), base=3))
                flag = 1
                break
        if flag == 1:
            break
    if flag == 0:
        k = ''
        for i in range(2):
            if three2[i] != n_3[0]:
                n_3[0] = three2[i]
                print(int(k.join(n_3), base=3))
                break
