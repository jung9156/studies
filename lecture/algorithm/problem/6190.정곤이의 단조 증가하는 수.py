def dan(x):
    c = str(x)
    for i in range(len(c) - 1):
        if c[i] > c[i + 1]:
            return -1
    return int(c)

tn = int(input())
for ir in range(tn):
    result = []
    nnn = int(input())
    a = list(map(int, input().split()))
    for i2 in range(len(a) - 1, -1, -1):
        for j2 in range(i2 - 1, -1, -1):
            ch = a[i2] * a[j2]
            if dan(ch) > 0:
                result.append(dan(ch))
    if len(result) == 0:
        ans = -1
    else:
        ans = max(result)
    print('#{} {}'.format(ir + 1, ans))