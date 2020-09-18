N = int(input())
K = int(input())
A = [[1 for ii in range(N+2)]] + [list([1] + list(0 for i in range(N)) + [1]) for i1 in range(N)] + [[1 for ii in range(N+2)]]
for i in range(K):
    x, y = map(int, input().split())
    A[x][y] = 4
L = int(input())
l = []
for i in range(L):
    t, v = input().split()
    l.append([int(t), v])
A[1][1] = 1
dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
ti = 0
ve = 1
snake = [1, 1]
v = l.pop(0)
time, di = v[0], v[1]
tail = []
while True:
    ti += 1
    tail.append([snake[0], snake[1]])
    snake[0] += dir[ve][0]
    snake[1] += dir[ve][1]
    if A[snake[0]][snake[1]] == 4:
        A[snake[0]][snake[1]] = 1
    elif A[snake[0]][snake[1]] == 0:
        A[snake[0]][snake[1]] = 1
        ttt = tail.pop(0)
        tail1, tail2 = ttt[0], ttt[1]
        A[tail1][tail2] = 0
    elif A[snake[0]][snake[1]] == 1:
        print(ti)
        break
    if ti == time:
        if v[1] == 'L':
            ve = (ve + 3) % 4
        else:
            ve = (ve + 1) % 4
        if l:
            v = l.pop(0)
            time, di = v[0], v[1]
        else:
            time = 10001