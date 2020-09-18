def fee(x):
    A = 0
    B = 0
    A = x[0] * x[4]
    if x[4] <= x[2]:
        B = x[1]
    else :
        B = x[1] + (x[4]-x[2]) * x[3]
    if A < B:
        return A
    elif A > B:
        return B

a = int(input())
result = []
for i in range(a):
    test_in = list(map(int, input().split(' ')))
    result.append(fee(test_in))
for i in range(a):
    print('#{} {}'.format(i+1, result[i]))