def find(x):

    for idx, i2 in enumerate(fi_a):

        if i2[0] == x[-1][1]:
            x.append(i2)
            fi_a[idx] = [0, 0]





test_case = int(input())
for ir in range(test_case):
    n = int(input())
    b = list(map(int, input().split()))
    key = []
    for i in b:
        if b.count(i) % 2 == 1:
            key.append(i)

    result = []
    a = []
    for i in range(n):
        a.append(b[i*2:i*2+2])
    fi_a = a
    for idx, ii in enumerate(fi_a):
        if ii[0] in key:
            result.append(ii)
            fi_a[idx] = [0, 0]

    while len(result) != n:
        find(result)
    re = ''
    for i in result:
        for j in range(2):
            re += ' ' + str(i[j])

    print('#{}{}'.format(ir+1,re))