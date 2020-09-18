tn = int(input())
for ir in range(tn):
    n = int(input())
    result = []
    for i in range(1, n+1):
        result.append([1]*i)


    if n > 1:
        for i in range(2, n+1):

            # print(result)
            if i > 2:
                for ii in range(1, i-1):
                    result[i-1][ii] = result[i-2][ii-1] + result[i-2][ii]
    print('#{}'.format(ir+1))
    for i in range(n):
        for ii in range(i+1):
            print('{}'.format(result[i][ii]),end=' ')
        print()