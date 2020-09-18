tn = int(input())
result = []
for ir in range(tn):
    N = str(input())
    if int(N[-1]) % 2 == 0:
        result.append('Even')
    else:
        result.append('Odd')
for i2 in range(tn):
    print('#{} {}'.format(i2+1, result[i2]))
