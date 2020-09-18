tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N = int(input())
    S1 = ((N+1) * (N) // 2)
    S3 = 2 * S1
    S2 = S3 - N
    print('{} {} {}'.format(S1, S2, S3))