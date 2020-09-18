for ir in range(10):
    n = int(input())
    a = list(map(int, input().split()))
    ch = []
    for i2 in range(8):
        for j2 in range(5):
            ch.append(j2+1)
    ch2 = 0
    ch3 = 0
    print('#{} '.format(ir+1),end='')
    while True:
        ch2 = ch2 % 8
        ch3 = ch3 % 40
        a[ch2] -= ch[ch3]
        if a[ch2] <= 0:
            a[ch2] = 0
            break
        ch2 += 1
        ch3 += 1

    for i5 in range(ch2+1, ch2+9):
        i6 = i5 % 8
        print(a[i6], end=' ')
    print()