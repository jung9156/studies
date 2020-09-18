tn = int(input())
for ir in range(tn):
    n = int(input())
    a = [list(map(int, list(input()))) for ii in range(n)]
    result = 0

    if n == 1:
        result = a[0][0]
    else:

        N = (n // 2)
        for i1 in range(n):
            for j1 in range(n):
                if (abs(N - i1) + abs(N - j1)) <= N :
                    result += a[i1][j1]

    print('#{} {}'.format(ir+1, result))