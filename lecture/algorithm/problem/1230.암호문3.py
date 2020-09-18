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
        if b[0] == 'I':
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
        elif b[0] == 'D':
            k1 = []
            for i1 in range(3):
                k1.append(b[i1])
            k.append(k1)
            del b[0:3]
        elif b[0] == 'A':
            k1 = []
            for i1 in range(2):
                k1.append(b[i1])
            k.append(k1)
            del b[0:2]
            v1 = []
            for i2 in range(int(k1[1])):
                v1.append(b[i2])
            v.append(v1)
            del b[0:int(k1[1])]
        if len(b) == 0:
            break
    newnum = 0
    for idx, i3 in enumerate(k):
        if i3[0] == 'I':
            N1 = int(i3[1])
            N2 = int(i3[2])
            if N1 == 0:
                result = v[newnum][0:N2] + result
            else:
                result = result[0:N1] + v[newnum][0:N2] + result[N1:]
            newnum += 1
        elif i3[0] == 'D':
            N1 = int(i3[1])
            N2 = int(i3[2])
            del result[N1:N1+N2]
        elif i3[0] == 'A':
            N1 = int(i3[1])
            result = result + v[newnum][0:N1]
            newnum += 1
    print('#{} '.format(ir+1), end='')
    for iii1 in range(10):
    	print(result[iii1], end=' ')
    print()