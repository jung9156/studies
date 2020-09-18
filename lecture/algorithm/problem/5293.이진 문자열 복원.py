for T in range(int(input())):
    q_list = list(map(int, input().split()))
    A, B, C, D = q_list[0], q_list[1], q_list[2], q_list[3]
    flag = 0
    k = B - C
    re = ''
    if abs(k) >= 2:
        flag = 1
        re = 'impossible'
    elif B == 0 and C == 0 and A >= 1 and D >= 1:
        re = 'impossible'
        flag = 1
    else:
        if k == 0:
            for i in range(A):
                re += '00'
            if B != 0:
                re += '01'
            for i in range(D):
                re += '11'
            if C != 0:
                re += '10'
            for i in range(B-1):
                re += '0110'
        elif k > 0: #B>C
            for i in range(A):
                re += '00'
            for i in range(B-1):
                re += '0110'
            re += '01'
            for i in range(D):
                re += '11'
        else:
            for i in range(D):
                re += '11'
            for i in range(C - 1):
                re += '1001'
            re += '10'
            for i in range(A):
                re += '00'
    if flag == 0:
        re2 = '' + re[0]
        for i in range(1, 2*(A+B+C+D), 2):
            re2 += re[i]
    else:
        re2 = re
    print('#{} {}'.format(T+1, re2))