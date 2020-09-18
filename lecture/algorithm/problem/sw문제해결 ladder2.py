for ii in range(10):
    tn = int(input())
    a = [list(map(int, input().split())) for k in range(100)]
    dx = [0, 0, 1]
    dy = [-1, 1, 0]
    st = []
    nl = []
    for s in range(100):
        if a[0][s] == 1:
            st.append(s)
    for j in st:
        n = 0
        x = 0
        y = j
        while True:
            if x == 99:
                break
            if y != 0 and a[x][y-1] == 1:
                while a[x][y-1] == 1 and y != 0:
                    n += 1
                    y -= 1
                n += 1
                x += 1
            elif y != 99 and a[x][y+1] == 1:
                while y != 99 and a[x][y+1] == 1:
                    n += 1
                    y += 1
                n += 1
                x += 1

            else:
                n += 1
                x += 1
        nl.append(n)

    print('#{} {}'.format(tn, st[nl.index(min(nl))]))