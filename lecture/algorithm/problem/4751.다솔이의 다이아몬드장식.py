tn = int(input())
for ir in range(tn):
    a = input()
    ke = []
    result = []
    for il in range(len(a)):
        result = [list('.' for i in range(5)) for i2 in range(5)]
        for i in range(5):
            for j in range(5):
                if abs(2-i) + abs(2-j) == 2:
                    result[i][j] = '#'
        if len(a) == 1:
            result[2][2] = a
        else:
            result[2][2] = a[il]

        ke.append(result)
    if len(a) == 1:
        for i5 in range(5):
            for j5 in range(5):
                print(ke[0][i5][j5],end='')
            print()
    else:
        for i in range(5):
                for i5 in range(len(a)):
                    if i5 != len(a)-1:
                        for j5 in range(4):
                            print(ke[i5][i][j5], end='')
                    else:
                        for j5 in range(5):
                            print(ke[i5][i][j5], end='')
                print()