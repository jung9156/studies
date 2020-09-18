tn = int(input())
for ir in range(tn):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=1)
    n = N // 3
    na = 0
    result = 0
    while True:
        if na == n:
            break
        result += sum(A[na*3:na*3+2])
        na += 1


    result += sum(A[n*3:])
    print('#{} {}'.format(ir+1, result))