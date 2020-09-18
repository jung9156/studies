tn = int(input())
for ir in range(tn):
    a = list(map(int, input().split()))
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    result = int(sum(a[1:9])/8 + 0.5)
    print('#{} {}'.format(ir+1, result))