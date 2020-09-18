tn = int(input())
for ir in range(tn):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = [0 for i in range(N)]
    for i1 in B:
        for idx, i2 in enumerate(A):
            if i2 <= i1:
                C[idx] += 1
                break
    print('#{} {}'.format(ir+1, C.index(max(C)) + 1))