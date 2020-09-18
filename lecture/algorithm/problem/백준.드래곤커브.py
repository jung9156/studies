def dragon(a):
    q = len(a)
    for i in range((q-1), -1, -1):
        a.append((a[i] + 1) % 4)


def check(x):
    fi, fj = x[0], x[1]
    dir2 = [[0, 1], [1, 1], [1, 0]]
    for i in range(3):
        qq = (fi + dir2[i][0], fj + dir2[i][1])
        if qq not in final:
            return False
    else:
        return True



N = int(input())
A = []
re = 0
for i in range(N):
    A.append(list(map(int, input().split())))
final = set()
dir = [[0, 1], [-1, 0], [0, -1], [1, 0]]
for i1 in range(len(A)):
    X, Y, d, g = A[i1]
    a = [d]
    final.add((Y, X))
    for d1 in range(g):
        dragon(a)

    for go in a:
        Y, X = Y + dir[go][0], X + dir[go][1]
        if 0 <= Y <= 100 and 0 <= X <= 100:
            final.add((Y, X))


final = list(final)
for ii in range(len(final)):
    if check(final[ii]) == True:
        re += 1
print(re)
