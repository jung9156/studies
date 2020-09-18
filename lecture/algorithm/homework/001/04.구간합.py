test_case = int(input())
for i in range(test_case):
    m_n = list(map(int, input().split()))
    n = m_n[0]
    m = m_n[1]
    result = []

    answer = 0
    v_in = list(map(int, input().split()))

    for j in range(m, n+1):
        result_t = 0
        for k in range(j-1, j - m - 1, -1):
            result_t += v_in[k]
        result.append(result_t)

        answer = max(result) - min(result)



    print('#{} {}'.format(i+1, answer))