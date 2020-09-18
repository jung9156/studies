# def solution(scoville, K):
#     answer = 0
#     idx = 0
#     scoville.sort()
#
#     while True:
#         if scoville[idx] < K:
#             if idx >= len(scoville) - 1:
#                 return -1
#             a, b = scoville[idx], scoville[idx + 1]
#             d = a + b * 2
#             answer += 1
#             for i in range(len(scoville)):
#                 if scoville[i] >= d:
#                     scoville = scoville[2:i] + [d] + scoville[i:]
#                     # print(scoville)
#                     break
#             else:
#                 scoville = scoville[2:] + [d]
#
#         else:
#             idx += 1
#         if scoville[idx] >= K:
#             return answer

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        n1 = heapq.heappop(scoville)
        if n1 < K:
            if len(scoville) == 0:
                return -1
            n2 = heapq.heappop(scoville)
            heapq.heappush(scoville, n1 + 2 * n2)
            answer += 1
        else:
            return answer

scoville = [1, 1]
K = 7
print(solution(scoville, K))