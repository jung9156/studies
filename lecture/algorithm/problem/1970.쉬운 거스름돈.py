test_num = int(input())
for ir in range(test_num):
    mon = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    n = int(input())
    n = (n // 10) * 10
    result = [0 for i in range(len(mon))]
    ch = 0
    ch2 = 0
    while True:
        if n - mon[ch] == 0:
            ch2 += 1
            result[ch] = ch2
            break
        elif n - mon[ch] > 0:
            n = n - mon[ch]
            ch2 += 1
        else:
            result[ch] = ch2
            ch2 = 0
            ch += 1
    print('#{}'.format(ir+1))
    for i in result:
        print(i, end = ' ')
    print()