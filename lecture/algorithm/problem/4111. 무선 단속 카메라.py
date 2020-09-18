tn = int(input())
for ir in range(tn):
    N = int(input())
    K = int(input())
    A = set(map(int, input().split()))
    A = list(A)
    A.sort()
    A2 = []
    if N == 1 or N <= K:
        print('#{} {}'.format(ir+1, 0))
    else:
        for i in range(len(A)-1):
            A2.append(A[i+1] - A[i])
        for i1 in range(K-1):
            A2.pop(A2.index(max(A2)))
        print('#{} {}'.format(ir+1, sum(A2)))