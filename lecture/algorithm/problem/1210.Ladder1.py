for ir in range(10):
    n = int(input())
    a = [list(map(int, input().split()))for iii in range(100)]
    a2 = a[-1]
    ed = a2.index(2)
    i = 98
    j = ed

    while True:
        if i == 0:
            print('#{} {}'.format(n, j))
            break
        if j-1 >= 0 and a[i][j-1] == 1:
            while True:
                j -= 1
                if j <= -1 or a[i][j] == 0:
                    j += 1
                    break

        elif j+1 <= 99 and a[i][j+1] == 1:
            while True:
                j += 1
                if j >= 100 or a[i][j] == 0:
                    j -= 1
                    break

        i -= 1