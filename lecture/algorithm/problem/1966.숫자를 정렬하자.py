test_num = int(input())
for ir in range(test_num):
    n = int(input())
    a = list(map(int, input().split()))

    for i in range(n-1):
        min = i
        for j in range(i, n):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    print('#{} '.format(ir+1),end='')
    for i in a:
        print(i,end=' ')
    print()

