N = int(input())
for ir in range(N):
    n = int(input())
    a = []
    t1 = []
    t2 = []
    t3 = []
    result = []
    for i in range(n):
        a.append([i for i in list(map(int, input().split()))])

    def turn(x):
        t = []
        t90 = []
        for ii in range(n):
            for iii in range(n-1, -1, -1):
                t90.append(x[iii][ii])
            t.append(t90)
            t90 = []

        return(t)
    t1 = turn(a)
    t2 = turn(t1)
    t3 = turn(t2)
    print('#{}'.format(ir+1))
    for i in range(n    ):
        for j in range(n):
            print(t1[i][j], end='')
        print(' ', end='')
        for j in range(n):
            print(t2[i][j], end='')
        print(' ', end='')
        for j in range(n):
            print(t3[i][j], end='')
        print()