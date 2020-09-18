def solution(board, moves):
    xn = len(board)
    yn = len(board[0])
    board_t = []

    for i in range(xn):
        b_i = []
        for j in range(yn):
            b_i.append(board[(xn - 1) - j][i])
        board_t.append(b_i)
    answer = 0
    A = []
    for m in moves:
        qn = board_t[m - 1].count(0)
        if qn != 0:
            q = board_t[m - 1].index(0)
        else:
            q = xn
        if q != 0:
            A.append(board_t[m - 1][q - 1])
            board_t[m - 1][q - 1] = 0
    result = [0]
    for nnn in range(len(A)):
        a = A.pop(0)

        if result[-1] == a:
            answer += 2
            result.pop(-1)
        else:
            result.append(a)
    return answer