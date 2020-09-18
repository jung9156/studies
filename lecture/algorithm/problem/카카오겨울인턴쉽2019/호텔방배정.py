# 1
# def solution(k, room_number):
#     answer = []
#     k_list = list(0 for i in range(k+1))
#     def find_room(N):
#         if k_list[N] == 0:
#             answer.append(N)
#             k_list[N] = N + 1
#         else:
#             find_room(k_list[N])
#     for room in room_number:
#         if k_list[room] == 0:
#             answer.append(room)
#             k_list[room] = room + 1
#         elif k_list[room] != 0:
#             N = k_list[room]
#             find_room(N)
#     return answer

#2
# def solution(k, room_number):
#     answer = []
#     check = []
#     def find_r(n):
#         while n in check:
#             n += 1
#         return n
#     for room in room_number:
#         if room in check:
#             room = find_r(room)
#         answer.append(room)
#         check.append(room)
#     return answer

#3
# def solution(k, room_number):
#     answer = []
#     f_list = {}
#     def find_room(N):
#             ch = []
#             if N in f_list:
#             while N in f_list:
#                 ch.append(N)
#                 N += 1
#             ch.append(N)
#             for i in ch:
#                 f_list[i] = N + 1
#             return N
#
#     for room in room_number:
#         if room not in f_list:
#             answer.append(room)
#             f_list[room] = room + 1
#         else:
#             N = find_room(room)
#             answer.append(N)
#     return answer

#4
# def solution(k, room_number):
#     answer = []
#     N = len(room_number)
#     n = 0
#     while n < N:
#         a = room_number[n]
#         if a not in answer:
#             answer.append(a)
#             for r in range(n + 1, N):
#                 if room_number[r] == a:
#                     room_number[r] += 1
#         else:
#             while a in answer:
#                 a += 1
#             answer.append(a)
#         n += 1
#
#     return answer

# 5
# def solution(k, room_number):
#     answer = []
#     visit = list(0 for i in range(k+1))
#     for room in room_number:
#         if visit[room] == 0:
#             visit[room] = room + 1
#             answer.append(room)
#         else:
#             while visit[room] != 0:
#                 room = visit[room]
#             answer.append(room)
#             visit[room] = room + 1
#     return answer

# 6
# def solution(k, room_number):
#     answer = []
#     visit = list(0 for i in range(k+1))
#     for room in room_number:
#         if visit[room] == 0:
#             visit[room] = room + 1
#             answer.append(room)
#         else:
#             q = [room]
#             while visit[room] != 0:
#                 room = visit[room]
#                 q.append(room)
#             answer.append(room)
#             for rr in q:
#                 visit[rr] = room + 1
#     return answer