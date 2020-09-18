tn = int(input())
for ir in range(tn):
    A = list(map(int, input()))
    q = len(A)
    turn = ['B', 'A']
    n = 0
    while q != 1:
        if q == 1:
            break
        if q % 2 == 0:
            for i1 in range(q-1):
                if A[i1] + A[i1+1] < 10:
                    A[i1] = A[i1] + A[i1+1]
                    del A[i1+1]
                    q -= 1
                    break
            else:
                gn = A[-2] + A[-1]
                A[-2] = gn // 10
                A[-1] = gn % 10
        else:
            for i1 in range(q - 1):
                if A[i1] + A[i1 + 1] >= 10:
                    gn = A[i1] + A[i1+1]
                    A[i1] = gn // 10
                    A[i1+1] = gn % 10
                    break
            else:
                A[-2] = A[-2] + A[-1]
                A.pop(-1)
                q -= 1
        n = (n + 1) % 2
    print('#{} {}'.format(ir+1, turn[n]))