tn = int(input())
for ir in range(tn):
    print('#{} '.format(ir+1),end='')
    a = list(map(int, input().split()))
    if a[0] == a[1]:
        print(a[2])
    elif a[0] == a[2]:
        print(a[1])
    else:
        print(a[0])