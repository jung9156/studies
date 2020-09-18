te_c = int(input())

def find(p, x):
    n = 0
    l = 1
    r = p
    c = 0
    while x != c:
        c = int((l + r) / 2)
        if c > x:
            r = c
        else:
            l = c
        n += 1
    return n
for ir in range(te_c):
    a = list(map(int, input().split()))
    p, pa, pb = a[0], a[1], a[2]
    a = find(p, pa)
    b = find(p, pb)
    print('#{} '.format(ir+1),end='')
    if a > b:
        print('B')
    elif a < b:
        print('A')
    else:
        print(0)