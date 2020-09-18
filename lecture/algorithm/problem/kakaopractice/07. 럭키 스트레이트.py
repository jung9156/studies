AAA = input()
A = []
for _ in AAA:
    A.append(int(_))

n = len(A)
B = sum(A[:n // 2])
C = sum(A[n // 2:])
if B == C:
    print('LUCKY')
else:
    print('READY')