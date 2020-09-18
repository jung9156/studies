def solution(stones, k):
    st_n = len(stones)
    answer = 0
    jing = []
    pass_l = []
    while True:
        N = min(stones)
        answer += N
        A = list(map(lambda i : i - N, stones))
        stones = A[:]
        for i1 in range(st_n):
            if i1 == 0:
                pass_l.append(i1)
            else:
                jing = 0
            if jing == k:
                return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))