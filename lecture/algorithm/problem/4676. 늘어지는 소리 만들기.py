tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    word = list(input())
    H = int(input())
    n = list(map(int, input().split()))
    N = [0 for i in range(len(word)+1)]
    result = []
    for i in n:
        N[i] += 1
    for i in range(len(word)):
        result += ['-' * N[i]]
        result += word[i]

    result += ['-' * N[len(word)]]
    re = ''.join(result)
    print(re)
