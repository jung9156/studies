test_case = int(input())
for i in range(test_case):
    count_list = [0 for k in range(10)]
    test_num = int(input())
    test_card = list(input())
    result = 0
    result_card = 0

    for k in test_card:
        count_list[int(k)] += 1
    for k in range(10):
        if result <= count_list[k]:
            result = count_list[k]
            result_card = k

    print('#{} {} {}'.format(i+1, result_card, result))