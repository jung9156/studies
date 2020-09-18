tn = int(input())
for ir in range(tn):
    A, B = input().split()
    A1, B1 = list(A), list(B)
    bd = [list(0 for i1 in range(len(B1)+1)) for j1 in range(len(A1)+1)]
    dx = -1
    dy = -1
    mm = 0
    for i in range(1, len(A1)+1):
        for j in range(1, len(B1)+1):
            if A1[i-1] == B1[j-1]:
                bd[i][j] = bd[i+dx][j+dy] + 1
                if mm < bd[i][j]:
                    mm = bd[i][j]
            else:
                if bd[i+dx][j] <= bd[i][j+dy]:
                    bd[i][j] = bd[i][j+dy]
                else:
                    bd[i][j] = bd[i+dx][j]
    print('#{} '.format(ir + 1), end='')
    print(mm)