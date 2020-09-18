tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    n = int(input())
    a = [1, 1, 1, 2, 2]
    if n <= 5:
        print(a[n-1])
    else:
        p = 4
        while True:
            if p == n-1:
                print(a[-1])
                break
            a.append(a[p] + a[p-4])
            p += 1
