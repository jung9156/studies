tn = int(input())
for i in range(tn):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    visit = [1] + [0] * sum(A)
    stack = []
    q = 0
    for ii, val in enumerate(A):
        qq = []
        for iii in range(q + 1):
            if visit[iii] == 1 and visit[iii + val] == 0:
                qq.append(iii + val)
                if q < iii + val:
                    q = iii + val
        for i3 in qq:
            visit[i3] = 1

    print('#{} {}'.format(i+1, visit.count(1)))

