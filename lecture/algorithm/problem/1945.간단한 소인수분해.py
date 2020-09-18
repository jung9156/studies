test_num = int(input())

for i in range(test_num):
    test_q = int(input())
    result = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    while test_q != 1:
        for key, val in result.items():
            if test_q % key == 0:
                test_q //= key
                result[key] += 1
    print('#{} {} {} {} {} {}'.format(i+1, result[2], result[3], result[5], result[7], result[11]))