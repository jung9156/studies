def scent_after(A_scent):
    global N
    for i in range(N):
        for j in range(N):
            # if type(A_scent[i][j]) == list:
            if A_scent[i][j][1] == 1:
                A_scent[i][j] = [0, 0]
            elif A_scent[i][j][1] >= 2:
                A_scent[i][j][1] -= 1


def scent(A_scent):
    global K
    for i in range(1, M + 1):
        x, y = shark_state[i][0], shark_state[i][1]
        A_scent[x][y] = [i, K]


def sm(n, d, x, y):
    dir = [[], [-1, 0], [1, 0], [0, -1], [0, 1]]
    for i in pr[n][d]:
        nx, ny = x + dir[i][0], y + dir[i][1]
        if 0 <= nx < N and 0 <= ny < N:
            if A_scent[nx][ny] == [0, 0]:
                shark_move[n] = [nx, ny]
                shark_dir[n] = i
                return

    for i in pr[n][d]:
        nx, ny = x + dir[i][0], y + dir[i][1]
        if 0 <= nx < N and 0 <= ny < N:
            if A_scent[nx][ny][0] == n:
                shark_move[n] = [nx, ny]
                shark_dir[n] = i
                return


N, M, K = map(int, input().split())
A = []

for i in range(N):
    A.append(list(map(int, input().split())))
shark_dir = [0]
shark_dir += list(map(int, input().split()))
pr = [[]]
for i in range(M):
    shark = [[]]
    for _ in range(4):
        shark.append(list(map(int, input().split())))

    pr.append(shark)
shark_state = [[] for _ in range(M + 1)]

for i in range(N):
    for j in range(N):
        q = A[i][j]
        if q != 0:
            shark_state[q] = [i, j]


A_scent = list(list([0, 0] for _ in range(N)) for __ in range(N))
scent(A_scent)

shark_move = [[] for _ in range(M + 1)] # 상어가 움직일 방향 기록하는 변수
# 상어가 움직일 방향 정하는 함수
time = 0
while time <= 1000:
    # for i in range(N):
    #     print(A_scent[i])
    # print()
    cnt = 0
    for s in shark_state:
        if s != []:
            cnt += 1
    if cnt == 1:
        break

    for _ in range(1, M + 1):
        if shark_state[_] != []:
            sm(_, shark_dir[_], shark_state[_][0], shark_state[_][1])
#죽은 4번 상어가 다시 튀어나옴!!
    #상어 움직이기#같은칸 상어 없애기
    for _ in range(M, 0, -1):
        if shark_state[_] != []:
            nx, ny = shark_state[_]
            mx, my = shark_move[_]
            now_s = A[nx][ny]
            move_s = A[mx][my]
            A[nx][ny] = 0
            A[mx][my] = now_s
            shark_state[A[nx][ny]] = []
            shark_state[A[mx][my]] = [mx, my]
        for _s in range(M, _, -1):
            if shark_state[_s] != []:
                scx, scy = shark_state[_s]
                if A[scx][scy] != _s:
                    shark_state[_s] = []
        if shark_state[_] != []:
            A_scent[mx][my] = [_, K + 1]

    scent_after(A_scent)
    #상어 냄새 줄이고, 남기기
    time += 1
if time > 1000:
    print(-1)
else:
    print(time)
