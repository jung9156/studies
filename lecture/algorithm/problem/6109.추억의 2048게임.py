def turn(x):
    xl = [list(0 for ix in range(n)) for jx in range(n)]
    for it in range(n):
        for jt in range(n):
            xl[jt][(n-1)-it] = x[it][jt]
    return xl

def push(y):
    pu_l = []
    resu = []
    for iy in range(n):
        pu_l2 = []
        for jy in range(n):
            if jy == n-1:
                if y[iy][jy] != 0:
                    pu_l2.append(y[iy][jy])
                break
            if y[iy][jy] != 0:
                dp = 0
                while True: #주의
                    dp += 1
                    if y[iy][jy] == y[iy][jy+dp]:
                        pu_l2.append(y[iy][jy]*2)
                        y[iy][jy+dp] = 0
                        break
                    if y[iy][jy] != y[iy][jy+dp]:
                        if jy + dp == n-1:
                            pu_l2.append(y[iy][jy])
                            break
                        if y[iy][jy+dp] != 0:
                            pu_l2.append(y[iy][jy])
                            break
        pu_l.append(pu_l2)

    for iy2 in range(n):
        if len(pu_l[iy2]) != n:
            while len(pu_l[iy2]) != n:
                pu_l[iy2].append(0)
    for iy3 in range(n):
        resu.append(pu_l[iy3])
    return resu
def end(x):#“left”, “right”, “up”, “down”
    if v == 'right':
        return turn(turn(push(turn(turn(x)))))
    elif  v == 'up':
        return turn(push(turn(turn(turn(x)))))
    elif v == 'left':
        return push(x)
    elif v == 'down':
        return turn(turn(turn(push(turn(x)))))


tn = int(input())
for ir in range(tn):
    ipli = list(input().split())
    n, v = int(ipli[0]), ipli[1]
    bd = [list(map(int, input().split())) for i10 in range(n)]
    print('#{}'.format(ir+1),end='')
    bd2 = end(bd)
    for irr in range(n):
        print()
        for jrr in range(n):
            print(bd2[irr][jrr], end=' ')
    print()