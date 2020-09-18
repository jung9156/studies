N = int(input())
A = []
q2 = []
qn2 = 0
for i in range(N):
    q = list(map(int, input().split()))
    qn = q.count(0)
    if qn == 1:
        q2.append(24)
        qn2 += 24
    elif qn == 2:
        q2.append(14)
        qn2 += 14
    else:
        q2.append(9 - qn)
        qn2 += (9 - qn)
    A.append(q)
AAA = []
for i in range(N):
    hap = 0
    for j in range(N):
        if A[j][i] == 0:
            hap += 1
    AAA.append(hap)
print(AAA)
