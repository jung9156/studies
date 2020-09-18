te_c = int(input())
for ir in range(te_c):
    num = int(input())
    nl = list(map(int, input().split()))
    nlm = []
    result = [0 for i in range(num)]
    for i in range(num-1):
        min = i
        for j in range(i+1, num):
            if nl[min] > nl[j]:
                min = j
        nl[i], nl[min] = nl[min], nl[i]
    nlm = nl[::-1]
    for iii in range(num):
        if iii % 2 == 0:
            result[iii] = nlm[iii//2]
        else:
            result[iii] = nl[iii//2]
    rere = ''
    for i in range(10):
        rere += ' ' + str(result[i])

    print('#{}{}'.format(ir + 1, rere))