from collections import deque


for ir in range(int(input())):
    N = int(input())
    A = []
    dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for i in range(N):
        a = input()
        b = []
        for i2 in a:
            b.append(int(i2))
        A.append(b)
    A_cal = list([90000 for i in range(N)] for i1 in range(N))
    A_cal[0][0],  A_cal[N-1][N-1] = 0, 9000
    visit = list([0 for i in range(N)] for i1 in range(N))

    queue = deque()
    queue.append([0, 0])
    while queue:
        vx, vy = queue.popleft()
        time = A_cal[vx][vy]
        for d in dir:
            cx, cy = vx + d[0], vy + d[1]
            if 0 <= cx < N and 0 <= cy < N:
                if time + A[cx][cy] < A_cal[cx][cy]:
                    queue.append([cx, cy])
                    A_cal[cx][cy] = time + A[cx][cy]

    print('#{} {}'.format(ir + 1, A_cal[N-1][N-1]))