def check(check_num):
    global x, y
    if check_num % 4 == 0:
        y += 1
        return y
    if check_num % 4 == 1:
        x += 1
        return x
    if check_num % 4 == 2:
        y -= 1
        return y
    if check_num % 4 == 3:
        x -= 1
        return x
t = 1
test_num = int(input())
for i in range(test_num):
    numnum = 1
    num = 1
    snail_num = int(input())

    snail = list([0 for i in range(snail_num)] for j in range(snail_num))
    check_list = [snail_num]
    for iii in range(snail_num-1):
        check_list.append(snail_num - 1 - iii)
        check_list.append(snail_num - 1 - iii)

    x = 0
    y = 0
    around = 0
    check_num = 0
    for ii in check_list:
        for jj in range(ii):
            if numnum == ii:
                snail[x][y] = num
                check_num += 1
                numnum = 0
            snail[x][y] = num
            num += 1
            numnum += 1
            check(check_num)
    print('#{}'.format(t))
    t += 1
    for i in range(snail_num):
        for i2 in range(snail_num):
            print(snail[i][i2],end=' ')
        print()
