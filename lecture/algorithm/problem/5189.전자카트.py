from itertools import permutations

def doo(i_list):
    k = A[0][i_list[0]]
    for idx, i in enumerate(i_list[:N-2]):
            k += A[i][i_list[idx + 1]]
    k += A[i_list[-1]][0]
    return k

for ir in range(int(input())):
    N = int(input())
    A = list(list(map(int, input().split())) for i in range(N))
    result = 10001
    for i in permutations(list(range(1, N)), N-1):
        k = doo(i)
        if k < result:
            result = k
    print('#{} {}'.format(ir+1, result))