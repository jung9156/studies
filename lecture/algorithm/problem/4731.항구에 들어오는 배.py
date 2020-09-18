tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir + 1), end='')
    n = int(input())
    a = []
    a += [int(input()) for ii in range(n)]
    A = set()
    ma = a[-1]
    A.add(1)
    if len(a) == 1:
        cnt = 1
    else:
        cnt = 0

    for i in a:
        if i not in A:
            A.add(i)
            cnt += 1
            gab = i - 1
            while True:
                i += gab
                if i > ma:
                    break
                A.add(i)

        if a == list(A):
            break
    print(cnt)