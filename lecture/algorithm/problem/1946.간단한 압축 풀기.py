test_num = int(input())

test_list = []
for i in range(test_num):
    test_case = int(input())
    print('#{}'.format(i+1))
    for _ in range(test_case):

        a = list(input().split(' '))
        for _ in range(int(a[1])):
            test_list.append(a[0])
    n = 0

    for j in test_list:
        if n == 10:
            n = 0
            print()
            print(j,end='')
            n += 1
        elif n != 10:
            print('{}'.format(j),end='')
            n += 1
    n = 0
    print()
    test_list = []