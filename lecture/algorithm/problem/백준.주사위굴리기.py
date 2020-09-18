N, M, X, Y, K = list(map(int, input().split()))
A = [list(map(int, input().split())) for iii in range(N)]
order = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0] #241356 (1이 상단) 동1 서2 북3 남4
dx = [1, 0, 0, -1]        #012345
dy = [0, 1, -1, 0 ]

def dich(n):
    if n == 1: #동
        dice[1], dice[2], dice[3], dice[5]  = dice[5], dice[1], dice[2], dice[3]
    elif n == 2: #서
        dice[1], dice[2], dice[3], dice[5] = dice[2], dice[3], dice[5], dice[1]
    elif n == 3: #북
        dice[0], dice[2], dice[4], dice[5] = dice[2], dice[4], dice[5], dice[0]
    elif n == 0: #남
        dice[0], dice[5], dice[4], dice[2] = dice[5], dice[4], dice[2], dice[0]
ix, iy = X, Y
result = []
for i1 in range(len(order)):
    map_num = order[i1] % 4
    ix += dx[map_num]
    iy += dy[map_num]
    if ix < 0 or ix >= N or iy < 0 or iy >= M:
        ix -= dx[map_num]
        iy -= dy[map_num]
        continue

    dich(map_num)
    if A[ix][iy] == 0:
        A[ix][iy] = dice[5]
    else:
        dice[5] = A[ix][iy]
        A[ix][iy] = 0
    print(dice[2])
