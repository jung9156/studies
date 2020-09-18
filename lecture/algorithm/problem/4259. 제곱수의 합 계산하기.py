tn = int(input())
for ir in range(tn):
    N = int(input())
    A = list(input().split())
    re = 0
    for i1 in range(N):
        re += int(A[i1][:-1]) ** int(A[i1][-1])
    print('#{} {}'.format(ir+1, re))