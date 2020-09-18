T = int(input())
total_result = []
test_n = []
for i in range(T):
    T2 = int(input())
    test_n.append(T2)
    test_score = list(map(int, input().split()))

    freq_list = [0 for i in range(101)]
    for score, val in enumerate(test_score):
        freq_list[val] += 1
    score_list = []
    for score, val in enumerate(freq_list):
        if val == max(freq_list):
            score_list.append(score)
    total_result.append(max(score_list))

for i in range(T):
    print('#{} {}'.format(test_n[i], total_result[i]))