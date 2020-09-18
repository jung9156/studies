for tn in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(M):
        t = A.pop(0)
        A.append(t)
    print('#{} {}'.format(tn+1, A[0]))
