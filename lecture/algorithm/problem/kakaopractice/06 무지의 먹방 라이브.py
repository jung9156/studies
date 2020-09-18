def solution(food_times, k):
    if sum(food_times) <= k:
        answer = -1
        return answer
    a = len(food_times)
    n1, n2 = k // a, k % a
    for i in range(a):
        food_times[i] -= n1
        if food_times[i] <= 0:
            n2 += abs(food_times[i])
            food_times[i] = 0

    k = n2
    idx = 0
    while k > 0:
        if food_times[idx] > 0:
            k -= 1
            food_times[idx] -= 1
        idx += 1
        if idx == a:
            idx = 0
    while food_times[idx] == 0:
        idx += 1
        if idx == a:
            idx = 0
    answer = idx + 1

    return answer