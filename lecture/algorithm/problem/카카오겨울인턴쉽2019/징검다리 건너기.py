# 1
# def solution(stones, k):
#     st_n = len(stones)
#     answer = 0
#     qq = []
#     N = min(stones)
#     answer += N
#     A = list(map(lambda i : i - N, stones))
#     while True:
#         jing = 0
#         for i1 in range(st_n):
#             if A[i1] == 0:
#                 if i1 not in qq:
#                     qq.append(i1)
#                 jing += 1
#                 if jing == k:
#                     return answer
#             else:
#                 jing = 0
#         for i in range(st_n):
#             if i not in qq:
#                 A[i] -= 1
#         answer += 1

# 2
# def solution(stones, k):
#     st_n = len(stones)
#     n = 0
#     answer = 200000000
#     while True:
#         if n + k > st_n:
#             return answer
#         st = stones[n:n + k]
#         stones = stones[n:]
#         st_n -= n
#         ms = max(st)
#         n = stones.index(ms) + 1
#         if answer > ms:
#             answer = ms
# stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
# print(solution(stones, k))

# 3
# def solution(stones, k):
#     st_n = len(stones)
#     n = 0
#     answer = 200000000
#     while True:
#         if n + k > st_n:
#             return answer
#         st = stones[n:n + k]
#         stones = stones[n:]
#         min_s = min(stones)
#         if answer < min_s:
#             return answer
#         st_n -= n
#         ms = max(st)
#         n = stones.index(ms) + 1
#         if answer > ms:
#             answer = ms