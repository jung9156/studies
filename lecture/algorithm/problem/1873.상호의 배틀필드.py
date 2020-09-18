def order(x):
    mlist = ['U', 'D', 'L', 'R']
    global now
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    ix = now[0]
    iy = now[1]
    if x in mlist:
        nn = mlist.index(x)
        a[ix][iy] = cha[nn]
        if 0 <= ix + dx[nn] < H and 0 <= iy + dy[nn] < W:
            if a[ix+dx[nn]][iy+dy[nn]] == '.':
                a[ix][iy], a[ix+dx[nn]][iy+dy[nn]] = a[ix+dx[nn]][iy+dy[nn]], a[ix][iy]
                now = [ix + dx[nn], iy + dy[nn]]
    else:
        nn = cha.index(a[ix][iy])
        while True:
            ix += dx[nn]
            iy += dy[nn]
            if H <= ix or ix < 0 or W <= iy or iy < 0 or a[ix][iy] == '#':
                break
            if a[ix][iy] == '*':
                a[ix][iy] = '.'
                break
tn = int(input())
for ir in range(tn):
    H, W = list(map(int, input().split()))
    a = [list(input()) for ii in range(H)]
    odn = int(input())
    od = list(input())
    cha = ['^', 'v', '<', '>']
    now = []
    for i1 in range(H):
        for j1 in range(W):
            if a[i1][j1] in cha:
                now.append(i1)
                now.append(j1)

    for i in od:
        order(i)
    print('#{} '.format(ir+1),end='')
    for i5 in range(H):
        for j5 in range(W):
            print(a[i5][j5],end='')
        print()