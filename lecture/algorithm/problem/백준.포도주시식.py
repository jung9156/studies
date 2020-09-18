N = int(input())
A = [0]
for _ in range(N):
    A.append(int(input()))
re = [0]

if N > 2:
    re.append(A[1])
    re.append(A[1] + A[2])
    for i in range(3, N + 1):
        re.append(max([re[i - 3] + A[i - 1] + A[i], re[i - 2] + A[i], re[i - 1]]))
    print(re[N])
elif N == 1:
    print(A[1])
elif N == 2:
    print(A[1] + A[2])
