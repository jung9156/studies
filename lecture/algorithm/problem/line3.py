def solution(road, n):
    road += '0'
    answer = -1
    road_l = list(road)
    A = []
    for idx, i in enumerate(road_l):
        if i == '0':
            A.append(idx)
    if len(A) <= n:
        answer = len(road) - 1
    else:
        re = []
        for i in range(n, len(A)):
            if i == n:
                re.append(A[i])
            else:
                re.append(A[i] - A[i-(n+1)] - 1)
        answer = max(re)


    return answer