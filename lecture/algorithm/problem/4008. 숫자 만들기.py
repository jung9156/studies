def cal(s, num, e):
    if e == '+':
        return s + num
    elif e == '-':
        return s - num
    elif e == '/':
        return int(s / num)
    else:
        return s * num

def ba(E, k, N, s):
    global max_n, min_n
    if k == N:
        if s > max_n:
            max_n = s
        if s < min_n:
            min_n = s
    else:
        ba(E, k + 1, N, cal(s, num[k], E[k]))
        for i in range(k, N):
            if i != k and E[i] == E[k]:
                continue
            if E[i] != E[i-1]:
                E[i], E[k] = E[k], E[i]
                ba(E, k + 1, N, cal(s, num[k], E[k]))
                E[k], E[i] = E[i], E[k]
tn = int(input())
result = []
for ir in range(tn):
    N = int(input())
    E2 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    num = num2[1:]
    Ex = ['+', '-', '*', '/']
    E = []
    max_n = -100000001
    min_n = 100000001
    for i in range(4):
        E += Ex[i] * E2[i]
    ba(E, 0, N-1, num2[0])
    result.append(max_n -min_n)
for ir2 in range(tn):
    print('#{} {}'.format(ir2+1, result[ir2]))