def change(i, j):

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    vl = []
    ch = []
    ch2 = []

    for c_i in range(8):
        if 0 <= i + dx[c_i] <= n-1 and 0 <= j + dy[c_i] <= n-1:
            if bd[i+dx[c_i]][j+dy[c_i]] != bw and bd[i+dx[c_i]][j+dy[c_i]] != 0:
                vl.append(c_i)

    for i_ci in range(len(vl)):
        cii = i
        cjj = j
        while True:
            cii += dx[vl[i_ci]]
            cjj += dy[vl[i_ci]]
            if cii < 0 or cii > n-1 or cjj < 0 or cjj > n-1 or bd[cii][cjj] == 0:
                ch = []
                break
            if bd[cii][cjj] != bw:
                ch.append([cii, cjj])
            elif bd[cii][cjj] == bw:

                ch2 += ch
                ch = []
                break

    while len(ch2) != 0:
        bd[ch2[0][0]][ch2[0][1]] = bw
        del ch2[0]

for ir in range(int(input())):
    n, m = list(map(int, input().split()))
    bd = [[0 for i_i in range(n)] for i_i2 in range(n)]
    bd[(n // 2 - 1)][(n // 2 - 1)] = 2
    bd[(n // 2 - 1) + 1][(n // 2 - 1) + 1] = 2
    bd[(n // 2 - 1)][(n // 2 - 1) + 1] = 1
    bd[(n // 2 - 1) + 1][(n // 2 - 1)] = 1

    for i1 in range(m):
        a = list(map(int, input().split()))
        j, i, bw = a[0]-1, a[1]-1, a[2]

        bd[i][j] = bw
        change(i, j)

    res1 = 0
    res2 = 0
    res0 = 0
    for i6 in range(n):
        res2 += bd[i6].count(2)
        res1 += bd[i6].count(1)

    print('#{} {} {}'.format(ir+1, res1, res2))