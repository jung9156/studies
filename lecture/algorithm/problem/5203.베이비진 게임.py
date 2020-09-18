def baby(p):
    q = list(0 for i in range(10))
    for i in p:
        if q[i] == 0:
            q[i] = 1
        else:
            q[i] += 1
    if max(q) >= 3:
        return 5
    st = 0
    for i in q:
        if i != 0:
            st += 1
        else:
            st = 0
        if st >= 3:
            return 5
    return 0
re = []
for ir in range(int(input())):
    A = list(map(int, input().split()))
    p1, p2 = [], []
    sc_1, sc_2 = 0, 0
    for i in range(6):
        p1.append(A.pop(0))
        p2.append(A.pop(0))
        sc_1 = baby(p1)
        sc_2 = baby(p2)
        if sc_1 == 5 or sc_2 == 5:
            if sc_1 == sc_2:
                re.append(1)
                break
            elif sc_1 > sc_2:
                re.append(1)
                break
            elif sc_1 < sc_2:
                re.append(2)
                break
    else:
        re.append(0)
for i in range(len(re)):
    print('#{} {}'.format(i+1, re[i]))