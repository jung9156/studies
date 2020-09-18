tn = int(input())
for ir in range(tn):
    n, m = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]
    result = []
    for i in range(n-(m-1)):
        for j in range(n-(m-1)):
            sum = 0
            for k in range(m):
                for kk in range(m):
                    sum += a[i+k][j+kk]
            result.append(sum)
    print('#{} {}'.format(ir+1, max(result)))
