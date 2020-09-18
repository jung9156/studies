def find(x, y):
    global result
    dir = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    r = 0
    for d in dir:
        x1, y1 = x + d[0], y + d[1]
        if 0 <= x1 < 10 and 0 <= y1 < 10 and A[x1][y1] == 1:
            A[x1][y1] = 3
            r = find(x1, y1)





for ir in range(int(input())):
    A = [list(map(int, input().split())) for i in range(10)]
    result = 0
    for i in range(10):
        for j in range(10):
            if A[i][j] == 1:
                A[i][j] = 3
                find(i, j)
                result += 1
    print('#{} {}'.format(ir+1, result))