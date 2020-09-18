def my_pow(n, m):
    if m == 1:
        return n
    return n * my_pow(n, m-1)
for ir in range(10):
    num = int(input())
    n, m = list(map(int, input().split()))
    result = 1
    print('#{} {}'.format(ir+1, my_pow(n, m)))