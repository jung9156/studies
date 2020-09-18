tn = int(input())
result = []
for ir in range(tn):
    N = int(input())
    n = 1
    t = 0
    while True:
        t = n ** 3
        if t < N:
            n += 1
        else:
            break
    if N % t == 0:
        result.append(n)
    else:
        result.append(-1)


for i2 in range(tn):
    print('#{} {}'.format(i2+1, result[i2]))