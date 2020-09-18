def fi(fl, k, N, s):
    global sm
    if k != 0:
        s += A[k-1][fl[k-1]]
    if s > sm:
        return
    if k == N:

        if sm > s:
            sm = s
        return

    for i in range(k, N):
        fl[k], fl[i] = fl[i], fl[k]
        fi(fl, k+1, N, s)
        fl[i], fl[k] = fl[k], fl[i]

tn = int(input())
for ir in range(tn):
    sm = 99999
    print('#{} '.format(ir+1),end='')
    N = int(input())
    A = [list(map(int, input().split())) for ii in range(N)]
    fl = list(range(N))
    fi(fl, 0, N, 0)
    print(sm)