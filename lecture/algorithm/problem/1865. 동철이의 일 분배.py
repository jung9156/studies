result2 = []

def boo(a, k, N, s):
    global result
    if s < result:
        return
    if k == N:
        if result < s:
            result = s
    for i in range(N):
        if a[i] == 0:
            if A[k][i] == 0:
                continue
            a[i] = 1
            boo(a, k+1, N, s * A[k][i])
            a[i] = 0

tn = int(input())
for ir in range(tn):
    N = int(input())
    A = [list(map(lambda i: int(i)/100, input().split())) for ii in range(N)]
    a = [0] * N
    result = 0
    boo(a, 0, N, 1)
    result2.append(result*100)

for ii in range(tn):
    print('#{} {:.6f}'.format(ii+1, result2[ii]))