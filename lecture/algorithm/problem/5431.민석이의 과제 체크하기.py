tn = int(input())
result = []
for ir in range(tn):
    N, K = map(int, input().split())
    check = list(input().split())
    re = ''
    A = list(map(str, range(1, N+1)))
    for i in A:
        if i not in check:
            re += i + ' '
    result.append(re)
for ir2 in range(tn):
    print('#{} {}'.format(ir2+1, result[ir2]))