import sys
sys.stdin = open('input.txt')


for t in range(1, int(input())+1):
    N = int(input())
    x_idx = list(map(int, input().split()))
    y_idx = list(map(int, input().split()))
    tex = float(input())
    visited = [0] * N
    distance = [float('inf')] * N
    c_l, n_l, result = 0, 0, 0
    distance[c_l] = 0
    for _ in range(N-1):
        visited[c_l] = 1
        min_dis = float('inf')
        for i in range(N):
            if not visited[i]:
                temp = (x_idx[c_l]-x_idx[i])**2 + (y_idx[c_l]-y_idx[i])**2
                if distance[i] > temp:
                    distance[i] = temp
                if min_dis > distance[i]:
                    min_dis = distance[i]
                    n_l = i
        c_l = n_l
    for j in range(N):
        result += distance[j]
    print('#{} {}'.format(t, round(result*tex)))
