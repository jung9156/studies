import copy

def safe(w1, w2, w3):
    A_fake = copy.deepcopy(A)
    A_fake[wall[w1][0]][wall[w1][1]] = 1
    A_fake[wall[w2][0]][wall[w2][1]] = 1
    A_fake[wall[w3][0]][wall[w3][1]] = 1
    virus(A_fake)

def virus(x):
    global vi, result
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    stack = []
    stack += vi
    while stack:
        v = stack.pop(-1)
        x[v[0]][v[1]] = 2
        for i1 in range(4):
            if v[0]+dx[i1] >=0 and v[0]+dx[i1] < x1 and v[1]+dy[i1] >= 0 and v[1]+dy[i1] < y1:
                if x[v[0]+dx[i1]][v[1]+dy[i1]] == 0:
                    x[v[0] + dx[i1]][v[1] + dy[i1]] = 2
                    stack.append([v[0] + dx[i1], v[1] + dy[i1]])
    cnt = 0
    for i in range(len(x)):
        cnt += x[i].count(0)
    if cnt > result:
        result = cnt



x1, y1 = map(int, input().split())
A = [list(map(int, input().split())) for ii in range(x1)]
vi = []
wall = []
result = 0
for i1 in range(x1):
    for j1 in range(y1):
        if A[i1][j1] == 2:
            vi.append([i1, j1])
        if A[i1][j1] == 0:
            wall.append([i1, j1])

wnum = len(wall)
for w1 in range(wnum-2):
    for w2 in range(w1+1, wnum-1):
        for w3 in range(w2+1, wnum):
            safe(w1, w2, w3)
            # 안전 판별
            # 최대값 비교
            # 원상태로 복귀
print(result)