a = 10
result = []
for i in range(a):
    test_num = int(input())
    test_in = list(map(int, input().split()))
    k = 2
    check = 0
    result_apt = 0
    while k <= test_num-3:
        check = max(test_in[k-2], test_in[k-1], test_in[k+1], test_in[k+2])
        if test_in[k] <= check:
            k += 1
        elif test_in[k] > check:
            result_apt += (test_in[k] - check)
            k += 3
    result.append(result_apt)
for i in range(a):
    print('#{} {}'.format(i+1, result[i]))