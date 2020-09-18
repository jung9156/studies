def solution(s):
    S = s[1:-1]
    A = []
    flag = 0
    re = []
    rre = ''
    for S1 in S:
        if S1 == '{':
            flag = 1
        elif S1 == '}':
            re += list(map(int, rre.split(',')))
            A.append(re)
            re = []
            rre = ''
            flag = 0
        elif flag == 1:
            rre += S1
    q = len(A)
    final = list([] for i in range(q))
    for i in A:
        final[len(i) - 1] += i
    stack = []
    answer = []
    for last in final:
        for last2 in last:
            if last2 not in stack:
                stack.append(last2)
                answer.append(last2)

    return answer