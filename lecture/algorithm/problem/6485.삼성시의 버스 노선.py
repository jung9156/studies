tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N = int(input())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    P = int(input())
    bustop = []
    for i in range(P):
        bustop.append(int(input()))
    re = [0 for i in range(5000)]
    for i in range(N):
        for j in range(A[i]-1, B[i]):
            re[j] += 1
    for i in range(P-1):
        print(re[bustop[i]-1],end=' ')
    print(re[bustop[-1]-1])