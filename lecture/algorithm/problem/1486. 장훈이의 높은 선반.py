def backt(a, k, n, s):
    global re
    if re >= s >= B:
        re = s
        return
    if k == n:
        return

    a[k] = 0
    backt(a, k+1, n, s)

    a[k] = 1
    backt(a, k+1, n, s + A[k])


for ir in range(int(input())):
    N, B = map(int, input().split())
    A = list(map(int, input().split()))
    a = [0 for i in range(N)]
    re = sum(A)
    backt(a, 0, len(A), 0)
    print('#{} {}'.format(ir+1, re - B))