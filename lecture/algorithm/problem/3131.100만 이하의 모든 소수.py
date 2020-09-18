n = list(i for i in range(2, 1000000))
k = 2

for i1 in n:
    if i1 != 0:
        k = i1
        print(k,end=' ')
        qq = k - 2
        while True:
            if qq > 999997:
                break
            n[qq] = 0
            qq += k
