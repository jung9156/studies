#1
for ir in range(10):
    n = int(input())
    a = list(map(int, input().split()))
    n1 = int(input())
    b = list(input().split())
    k = []
    v = []
    n_1 = 0
    k2 = []
    k3 = []
    result = a
    while True:
        k1 = []
        for i1 in range(3):
            k1.append(b[i1])
        k.append(k1)
        del b[0:3]
        v1 = []
        for i2 in range(int(k1[2])):
            v1.append(b[i2])
        v.append(v1)
        del b[0:int(k1[2])]
        if len(b) == 0:
            break
    for idx, i3 in enumerate(k):
        N1 = int(i3[1])
        N2 = int(i3[2])
        if N1 == 0:
            result = v[idx][0:N2] + result
        else:
            result = result[0:N1] + v[idx][0:N2] + result[N1:]
    print('#{} '.format(ir+1), end='')
    for iii1 in range(10):
    	print(result[iii1], end=' ')
    print()
#2
    # for ir in range(10):
    #     n = int(input())
    #     a = list(map(int, input().split()))
    #     n1 = int(input())
    #     b = list(input().split())
    #     k = []
    #     v = []
    #     n_1 = 0
    #     k2 = []
    #     k3 = []
    #     result = a[0:10]
    #     print('#{} '.format(ir + 1), end='')
    #     for i2 in b:
    #         if n_1 >= 3:
    #             if len(k2) != 0:
    #                 k.append(k2)
    #                 k2 = []
    #                 n_2 = int(k[-1][-1])
    #             k3.append(i2)
    #             n_1 += 1
    #             if n_1 == 3 + n_2:
    #                 n_1 = 0
    #                 v.append(k3)
    #         else:
    #             k2.append(i2)
    #             n_1 += 1
    #             k3 = []
    #
    #     for idx, i5 in enumerate(k):
    #         n_5 = int(i5[1])
    #         n_6 = int(i5[2])
    #         if n_5 <= 10:
    #             if n_5 == 0:
    #                 result = v[idx][0:n_6] + result
    #             else:
    #                 result = result[0:n_5] + v[idx][0:n_6] + result[n_5:]
    #             result = result[0:10]
    #     for ila in range(10):
    #         print(int(result[ila]), end=' ')
    #     print()