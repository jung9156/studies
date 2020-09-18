def solution(user_id, banned_id):

    def check(b_id, user):
        for s in range(len(b_id)):
            if b_id[s] != '*':
                if b_id[s] != user[s]:
                    return False
            elif b_id[s] == '*':
                continue
        else:
            return True

    def back(u, b, N1, N2):
        if b == N2:
            if u not in result:
                result.append(u[:])
            return
        for i in range(N1):
            if u[i] == 0 and len(banned_id[b]) == len(user_id[i]):
                if check(banned_id[b], user_id[i]) == True:
                    u[i] = 1
                    back(u[:], b + 1, N1, N2)
                    u[i] = 0


    answer = 0
    result = []
    N1 = len(user_id)
    N2 = len(banned_id)
    u = [0 for ii in range(N1)]
    back(u, 0, N1, N2)
    answer = len(result)
    return answer