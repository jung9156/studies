N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
result = 0
for i in range(N):
    re = A[i]
    re -= B
    result += 1
    if re > 0:
        if re % C == 0:
            result += re // C
        else:
            result += (re // C) + 1
print(result)

