def soon(a, k, n):
    global N, result, u
    if k == n:
        a.insert(3, 0)
        final.append(a[:])
        a.pop(3)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            soon(a, k+1, n)
            a[k], a[i] = a[i], a[k]

N = int(input())
A = [list(map(int, input().split())) for i in range(N)]
result = 0
final = []
soon([1, 2, 3, 4, 5, 6, 7, 8], 0, 8)
for a1 in final:
    re = 0
    ta = 0
    for i7 in A:
        out = 0
        r1, r2, r3 = 0, 0, 0
        while out != 3:
            if i7[a1[ta]] == 0:
                out += 1
            elif i7[a1[ta]] == 1:
                re += r3
                r3, r2, r1 = r2, r1, 1
            elif i7[a1[ta]] == 2:
                re += r3 + r2
                r3, r2, r1 = r1, 1, 0
            elif i7[a1[ta]] == 3:
                re += r3 + r2 + r1
                r3, r2, r1 = 1, 0, 0
            else:
                re += 1 + r1 + r2 + r3
                r1, r2, r3 = 0, 0, 0

            ta = (ta + 1) % 9
    result = max(result, re)

print(result)