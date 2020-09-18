test_case = int(input())
for ir in range(test_case):
    a = [[0 for i in range(10)] for i in range(10)]
    te_n = int(input())
    result = 0
    for i in range(te_n):
        fill = list(map(int, input().split()))

        fs, fe, fc = (fill[0], fill[1]), (fill[2], fill[3]), fill[4]

        for x in range(fs[0], fe[0]+1):
            for y in range(fs[1], fe[1]+1):
                if fc == 1:
                    if a[x][y] == 0 or a[x][y] == 2:
                        a[x][y] += fc
                if fc == 2:
                    if a[x][y] ==0 or a[x][y] == 1:
                        a[x][y] += fc
                if a[x][y] == 3:
                    result += 1

    print('#{} {}'.format(ir+1, result))