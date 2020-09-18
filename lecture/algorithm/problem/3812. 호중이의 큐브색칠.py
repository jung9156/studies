tn = int(input())
for ir in range(tn):
    X, Y, Z, A, B, C, N = map(int, input().split())
    final = [0 for i in range(N)]
    q1 = (X - A) // N
    q2 = (X - A) % N
    q3 = A // N
    q4 = A % N
    result = [0 for i in range(N)]
    result3 = []

    result2 = [q1 + q3 for i in range(N)]
    for ii in range(q2):
        result2[ii] += 1
    for ii2 in range(1, q4+1):
        result2[ii2] += 1



    q5 = (Y-B) // N
    q6 = (Y-B) % N
    q7 = B // N
    q8 = B % N

    result4 = [q5 + q7 for i in range(N)]
    for jj in range(q6):
        result4[jj] += 1
    for jj2 in range(1, q8 + 1):
        result4[jj2] += 1

    for idx, ffi in enumerate(result4):
        for i10 in range(N):
            result[(idx + i10)%N] += (result2[i10]) * ffi

    ban = sum(result)
    for i in range(N):
        new_re = []
        num = 0
        for iii in range(i, -len(result) + i, -1):
            new_re.append(result[iii])
        for fi in range((Z - C) % N):
            num += new_re[fi]
        for fi2 in range(1, (C % N) + 1):
            num += new_re[fi2]

        final[i] = num + (ban * ((Z - C) // N)) + (ban * (C//N))



    print('#{} '.format(ir+1), end='')
    for i in range(N):
        print('{}'.format(final[i]), end=' ')
    print()
