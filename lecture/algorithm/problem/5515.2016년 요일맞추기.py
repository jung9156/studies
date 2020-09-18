tn = int(input())
result = []
for ir in range(tn):
    M, D = map(int, input().split())
    ch = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = [3, 4, 5, 6, 0, 1, 2]
    da = 0
    for i in range(M):
        da += ch[i]
    da = (da + D) % 7
    result.append(week[da])

for i2 in range(tn):
    print('#{} {}'.format(i2+1, result[i2]))