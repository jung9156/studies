tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    A = list(map(int, input().split()))
    ea = 0
    for i in A:
        if i < 40:
            i = 40
        ea += i
    ea2 = ea // 5
    print(ea2)