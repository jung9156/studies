monda = '31,28,31,30,31,30,31,31,30,31,30,31'
monda = list(map(int, monda.split(',')))
mon_dict = {}

for i, _ in enumerate(monda):
    mon_dict[i+1] = _

test_num = int(input())
result = 0
for i in range(test_num):
    test = list(map(int, input().split(' ')))
    if test[0] == test[2]:
        result = test[3] - test[1] + 1
    else:
        for l in range(test[0], test[2]):
            result += mon_dict[l]

        result += test[3] - (test[1]-1)

    print('#{} {}'.format(i+1, result))
    result = 0
