from itertools import permutations



def move(com, home, p):
    global result
    re = 0
    st = com
    for i in p:
        re += abs(st[0] - i[0]) + abs(st[1] - i[1])
        st = i
        if re > result:
            return
    re += abs(st[0] - home[0]) + abs(st[1] - home[1])
    if re < result:
        result = re




for ir in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    result = 200 * N
    C = []
    com = [A[0], A[1]]
    home = [A[2], A[3]]
    for i in range(4, 4 + N * 2, 2):
        C.append([A[i], A[i + 1]])

    for p in permutations(C):
        move(com, home, p)
    print('#{} {}'.format(ir + 1, result))