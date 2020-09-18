nl = list(range(2, 1000000))
n = 2
nn = 0

for idx, i in enumerate(nl):
    if i != 0:
        n = i
        nn = 2 * n - 2
        while True:
            if nn > 999997:
                break
            nl[nn] = 0
            nn += n
check_l = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
for i in nl:
    if i != 0:
        i2 = set((str(i)))
        for i3 in i2:
            if i3 != '0':
                check_l[i3] += 1

result = []
tn = int(input())
for ir in range(tn):
    D, A, B = list(map(int, input().split()))
    re = 0
    if A <= 2 and B >= 999983:
        result.append(check_l[str(D)])
    else:
        for i in nl:
            if A <= i <= B:
                if i != 0:
                    i2 = set((str(i)))
                    for i3 in i2:
                        if str(D) in i3:
                            re += 1
            if i > B:
                break
        result.append(re)

    print('#{} {}'.format(ir+1, result[ir]))