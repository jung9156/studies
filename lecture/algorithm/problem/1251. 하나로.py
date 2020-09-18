for ir in range(int(input())):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())
    A = []
    re = 0
    target = 0
    distance = [100000000000000000000 for i in range(N)]
    for i in range(N):
        A.append([X[i], Y[i]])
    visit = [0 for i in range(N)]

    for iiiii in range(N - 1):
        visit[target] = 1
        cx, cy = A[target]
        i_min = 1000000000000000000000
        for i in range(N):
            if visit[i] != 1:
                bx, by = A[i]
                l = (cx - bx) ** 2 + (cy - by) ** 2
                if distance[i] > l:
                    distance[i] = l
                if i_min > distance[i]:
                    i_min = distance[i]
                    target = i

    for i in range(1, N):
        re += distance[i]

    re = re * E
    print('#{} {}'.format(ir + 1, round(re)))