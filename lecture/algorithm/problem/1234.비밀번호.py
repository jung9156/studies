for ir in range(10):
    n, a = list(input().split())
    a = list(str(a))
    while True:
        endn = len(a)
        for i in range(endn-1):
            if a[i] == a[i+1]:
                del a[i:i+2]
                break

        if endn == len(a):
            break

    print('#{} '.format(ir+1), end='')
    for iii1 in range(len(a)):
    	print(a[iii1], end='')
    print()