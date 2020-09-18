tn = int(input())
for ir in range(tn):
    result = 0
    a = int(input())
    if a % 2 == 1:
        result = (a // 2) + 1
    else:
        result = -(a // 2)
    print('#{} {}'.format(ir+1, result))