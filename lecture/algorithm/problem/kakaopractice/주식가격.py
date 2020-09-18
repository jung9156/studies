def solution(price):
    N = len(price)
    answer = list(0 for i in range(N))
    answer[-1] = N - 1
    visit = list(0 for i in range(N))
    Q, P = price[N - 1], N - 1
    for i in range(N - 2, -1, -1):
        if price[i] > Q:
            answer[i] = P
            Q, P = price[i], i
        elif price[i] <= Q:
            i2 = i
            while True:
                i2 += 1
                if i2 >= N - 1:
                    break
                if price[i2] < price[i]:
                    break
            answer[i] = i2
            Q, P = price[i], i
    for i in range(N):
        answer[i] -= i

    return answer
# 이렇게 해도 되는데 왜 어렵게 생각했지..?
# def solution(price):
#     N = len(price)
#     answer = list(0 for i in range(N))
#     for i in range(N):
#         i2 = i
#         while True:
#             i2 += 1
#             if i2 > N - 1:
#                 answer[i] = N - 1 - i
#                 break
#             if price[i] > price[i2]:
#                 answer[i] = i2 - i
#                 break
#     answer[-1] = 0
#     return answer