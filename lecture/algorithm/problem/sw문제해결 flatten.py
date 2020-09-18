result = []

for i in range(10):
    dump_num = int(input())
    box_h = list(map(int, input().split()))
    check_box = 0
    aver_h = sum(box_h) // 100 + 1
    check2 = sum(box_h) % 100
    a = 0
    if check2 == 0:
        a = 0
    else:
        a = 1

    for i in box_h:
        if i > aver_h:
            check_box += (i - aver_h)
    if check_box < dump_num:
        result.append(a)
    else:
        while dump_num > 0:
            box_h[box_h.index(max(box_h))] -= 1
            box_h[box_h.index(min(box_h))] += 1
            dump_num -= 1
        result.append(max(box_h) - min(box_h))

for i in range(10):
    print('#{} {}'.format(i + 1, result[i]))
