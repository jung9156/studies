test_case = int(input())
result = []
for i in range(test_case):
    test_num = int(input())
    n = 1
    check = set()
    test_checknum = 1
    while True:
        test_checknum = test_num * n
        for i in str(test_checknum):
            check.add(i)

        if len(check) == 10:
            result.append(test_checknum)
            break

        n += 1
for i in range(test_case):
    print('#{} {}'.format(i + 1, result[i]))