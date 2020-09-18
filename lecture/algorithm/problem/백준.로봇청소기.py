N, M = map(int, input().split())
r, c, d = map(int, input().split())
A = list(list(map(int, input().split())) for i in range(N))
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
result = 0
while True:
    if A[r][c] == 0:
        A[r][c] = 3
        result += 1

    for i in range(4):
        d = (d + 3) % 4
        v = dir[d]
        if A[r + v[0]][c + v[1]] == 0:
            r, c = r + v[0], c + v[1]
            break
    else:
        d2 = (d + 2) % 4
        r, c = r + dir[d2][0], c + dir[d2][1]
        if A[r][c] == 1:
            break
print(result)