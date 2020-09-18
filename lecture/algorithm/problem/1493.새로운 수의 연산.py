def find(x):
    n = 0
    nm = 0
    while True:
        nm += 1
        n += nm
        if n >= x:
            break
    k = n - x
    i = nm - k
    j = 1 + k
    return (i, j)

def tran(y):
    n2 = (y[0] + y[1])
    num = 0
    for i in range(1, n2):
        num += i
    return num - (n2 - y[0] - 1)
tn = int(input())
for ir in range(tn):
    a, b = list(map(int, input().split()))
    ijli = []
    for i in range(2):
        ijli.append(find(a)[i] + find(b)[i])

    print('#{} {}'.format(ir+1, tran(ijli)))