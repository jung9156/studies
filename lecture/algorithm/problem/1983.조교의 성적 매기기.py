tn = int(input())
for ir in range(tn):
    n, k = list(map(int, input().split()))
    result = []
    k2 = 0
    s_dict = {}
    for i in range(n):
        ts = 0
        s1, s2, s3 = list(map(int, input().split()))
        ts = ((int((s1 * 0.35 + s2 * 0.45 + s3 * 0.2)*100) + 5)/100)
        result.append(ts)
    k2 = result[k-1]

    result.sort(reverse=True)
    score = n // 10
    hak = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    ha = []
    for i in hak:
        for j in range(score):
            ha.append(i)

    for ii in range(len(result)):
        s_dict[result[ii]] = ha[ii]

    print('#{} {}'.format(ir+1, s_dict[k2]))