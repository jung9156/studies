N = int(input())
A = list(map(int, input().split()))
final = 0
a = 0
A.sort()
flag = 0
while a < len(A):
    D = A[a:a + A[a]]
    while len(D) < max(D):
        if a + max(D) > len(A):
            flag = 1
            break
        D = A[a:a + max(D)]
    if flag == 1:
        break
    else:
        final += 1
        a += len(D)
print(final)