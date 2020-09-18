tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    N = int(input())
    an = 0
    A = []
    while True:
        A1 = list(input())
        an += A1.count('.') + A1.count('?') + A1.count('!')
        A += A1
        if an == N:
            break

    D = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = 'abcdefghijklmnopqrstuvwxyz'


    result = []
    end_l = '.?!'
    flag = 0
    stack = []
    cnt = 0
    for i in A:
        stack.append(i)
        if i == ' ' or i in end_l:
            stack.pop(-1)
            if len(stack) != 0 and stack[0] in D:
                for i1 in range(1, len(stack)):
                    if stack[i1] not in d:
                        break
                else:
                    cnt += 1
            stack = []
        if i in end_l:
            result.append(cnt)
            cnt = 0
    print(*result)