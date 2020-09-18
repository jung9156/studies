N = int(input())
one = [0] * N
zero = [0] * N
one[0] = 1

for i in range(1, N):
    zero[i] += one[i - 1]
    zero[i] += zero[i - 1]
    one[i] += zero[i - 1]
print(zero[-1] + one[-1])