re = [0]
tn = int(input())
for ir in range(tn):
    a1, b1, b2, a2 = map(int, input().split())
    q = (a1 * a2) - (b1 * b2)
    if q > 0:
        re.append('ALICE')
    elif q < 0:
        re.append('BOB')
    else:
        re.append('DRAW')

for i1 in range(1, tn+1):
    print('#{} {}'.format(i1, re[i1]))