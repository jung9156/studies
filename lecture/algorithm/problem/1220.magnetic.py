def check(x):
    count = 0
    kyo = 0
    for i1 in range(n):
        kyo = 0
        for j1 in range(n):
            if a[j1][i1] == 1:
                kyo = 1
            if kyo == 1:
                if a[j1][i1] == 2:
                    count += 1
                    kyo = 0
    return count

for ir in range(10):
    n = int(input())
    a = [list(map(int, input().split())) for i2 in range(100)]
    print('#{} {}'.format(ir+1, check(a)))