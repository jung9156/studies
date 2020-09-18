tn = int(input())
result = []
for ir in range(tn):
    N, Q = map(int, input().split())
    N_box = list('0' for i in range(N))
    L = []
    R = []
    for i in range(Q):
        l, r = map(int, input().split())
        L.append(l)
        R.append(r)
    for i in range(Q):
        for i2 in range(L[i], R[i]+1):
            N_box[i2-1] = str(i+1)
    re2 = ' '.join(N_box)
    result.append(re2)

for i2 in range(tn):
    print('#{} {}'.format(i2+1, result[i2]))