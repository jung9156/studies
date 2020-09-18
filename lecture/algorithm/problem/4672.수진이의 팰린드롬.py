def pal(x):
    global cnt
    N = len(x)

    for i in range(1, N//2+1):
        if x[i-1] != x[-i]:
            return
    else:
        cnt += 1
    # if N % 2 == 0:
    #     if x[:N//2] == x[n//2:]:
    #         cnt += 1
    # else:
    #     if x[:N//2] == x[n//2+1:]:
tn = int(input())
for ir in range(tn):
    A = input()
    A_d = {}
    for i in A:
        if i not in A_d:
            A_d[i] = 1
        else:
            A_d[i] += 1
    word = ''
    for i1, i2 in A_d.items():
        word += i1 * i2
    cnt = 0
    for i3 in range(1, len(word)+1):
        for i4 in range(0, len(word)+1-i3):
            pal(word[i4:i4+i3])
    print('#{} {}'.format(ir+1, cnt))
